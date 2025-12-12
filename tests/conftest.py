# tests/conftest.py
import os
import sys
import pytest
from datetime import datetime

# Ensure repo root is first on sys.path so "import demo_webapp" works
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Import your Flask app (demo_webapp/app.py should define `app`)
from demo_webapp.app import app as flask_app

# Evidence helper
def ensure_dir(path):
    os.makedirs(path, exist_ok=True)
    return path

@pytest.fixture(scope='session')
def app():
    flask_app.config['TESTING'] = True
    yield flask_app

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()

@pytest.fixture
def evidence():
    ev_root = ensure_dir(os.path.join(ROOT, 'evidence'))
    screens = ensure_dir(os.path.join(ev_root, 'screens'))
    videos = ensure_dir(os.path.join(ev_root, 'videos'))

    class Evidence:
        def save(self, name, data, suffix='html'):
            ts = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
            filename = f"{name}_{ts}.{suffix}"
            path = os.path.join(screens if suffix != "mp4" else videos, filename)
            mode = 'wb' if isinstance(data, (bytes, bytearray)) else 'w'
            with open(path, mode) as fh:
                fh.write(data)
            return path

    return Evidence()
