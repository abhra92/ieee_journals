import base64
import glob
import json
import os
from pathlib import Path


def generate_colab_sync_code() -> str:
    files = glob.glob("ml/src/*.py")
    file_dict = {}
    for f in sorted(files):
        name = Path(f).name
        with open(f, "rb") as fh:
            content = fh.read()
        file_dict[name] = base64.b64encode(content).decode("utf-8")

    code = f'''import os, base64
print("Syncing Single Source of Truth ml/src/ modules into Colab...")
os.makedirs("ml/src", exist_ok=True)
os.makedirs("ml/configs", exist_ok=True)
os.makedirs("ml/data/splits", exist_ok=True)
os.makedirs("ml/checkpoints", exist_ok=True)
os.makedirs("ml/reports", exist_ok=True)
os.makedirs("models", exist_ok=True)

modules = {json.dumps(file_dict, indent=2)}

for fname, b64_str in modules.items():
    dest = os.path.join("ml/src", fname)
    with open(dest, "wb") as f:
        f.write(base64.b64decode(b64_str))
    print(f"  Wrote {{dest}}")

import sys
if "." not in sys.path:
    sys.path.insert(0, ".")
print("ml/src modules synced successfully and available in sys.path!")
'''
    return code


if __name__ == "__main__":
    code = generate_colab_sync_code()
    with open("sync_code.py", "w", encoding="utf-8") as f:
        f.write(code)
    print("Generated sync_code.py successfully.")
