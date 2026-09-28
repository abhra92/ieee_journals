import io
from pathlib import Path
from typing import Tuple
from fastapi import HTTPException, UploadFile, status
from PIL import Image

from backend.app.config import settings


async def validate_and_load_image(file: UploadFile) -> Image.Image:
    """
    Validate uploaded image:
    1. Checks filename extension
    2. Checks content-type header
    3. Checks file byte size limit
    4. Validates PIL decode integrity without executing arbitrary payloads
    """
    # Check extension
    ext = Path(file.filename or "").suffix.lower()
    if ext not in settings.ALLOWED_IMAGE_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid file extension '{ext}'. Allowed: {list(settings.ALLOWED_IMAGE_EXTENSIONS)}",
        )

    # Check content type if supplied
    if file.content_type and file.content_type not in settings.ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid content-type '{file.content_type}'. Must be a valid image.",
        )

    content = await file.read()
    if len(content) > settings.MAX_UPLOAD_SIZE_BYTES:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File exceeds max upload size of {settings.MAX_UPLOAD_SIZE_BYTES // (1024*1024)} MB.",
        )

    try:
        image = Image.open(io.BytesIO(content)).convert("RGB")
        image.verify()  # Check for corruption
        # Reopen after verify
        image = Image.open(io.BytesIO(content)).convert("RGB")
        return image
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Corrupted or invalid image file: {str(e)}",
        )
