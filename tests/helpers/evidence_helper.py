# tests/helpers/evidence_helper.py
import os
from datetime import datetime

EVIDENCE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "evidence"))
SCREEN_DIR = os.path.join(EVIDENCE_DIR, "screens")
VIDEO_DIR = os.path.join(EVIDENCE_DIR, "videos")

os.makedirs(SCREEN_DIR, exist_ok=True)
os.makedirs(VIDEO_DIR, exist_ok=True)

def save_html_snapshot(name: str, html_content: str):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{ts}_{name}.html"
    path = os.path.join(SCREEN_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_content)
    return path
