import io
from pathlib import Path
import pytest
from fastapi.testclient import TestClient
from PIL import Image

from backend.app.main import app

client = TestClient(app)


def create_test_image_bytes() -> io.BytesIO:
    """Helper to generate a dummy valid RGB JPEG image in memory."""
    img = Image.new("RGB", (224, 224), color=(200, 100, 100))
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    buf.seek(0)
    return buf


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert "disclaimer" in data


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["model_loaded"] is True
    assert "device" in data


def test_model_info_endpoint():
    response = client.get("/model-info")
    assert response.status_code == 200
    data = response.json()
    assert "model_name" in data
    assert len(data["classes"]) == 7
    assert data["image_size"] == 224


def test_predict_endpoint():
    buf = create_test_image_bytes()
    response = client.post(
        "/predict",
        files={"file": ("test.jpg", buf, "image/jpeg")},
    )
    assert response.status_code == 200
    data = response.json()
    assert "predicted_class" in data
    assert "confidence" in data
    assert "top_predictions" in data
    assert "disclaimer" in data


def test_predict_top_k_endpoint():
    buf = create_test_image_bytes()
    response = client.post(
        "/predict/top-k",
        data={"k": 3},
        files={"file": ("test.jpg", buf, "image/jpeg")},
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data["top_predictions"]) == 3


def test_explain_endpoint():
    buf = create_test_image_bytes()
    response = client.post(
        "/explain",
        files={"file": ("test.jpg", buf, "image/jpeg")},
    )
    assert response.status_code == 200
    data = response.json()
    assert "overlay_base64" in data
    assert data["overlay_base64"].startswith("data:image/png;base64,")
    assert "prediction" in data


def test_invalid_file_extension():
    buf = io.BytesIO(b"dummy text")
    response = client.post(
        "/predict",
        files={"file": ("test.txt", buf, "text/plain")},
    )
    assert response.status_code == 400
