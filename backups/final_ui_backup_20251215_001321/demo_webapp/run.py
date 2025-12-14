# run.py
"""
Robust Flask runner.
Tries to import a Flask `app` or `create_app()` from common modules.
Reads FLASK_RUN_HOST, FLASK_RUN_PORT, FLASK_DEBUG environment vars.
"""

import os
import importlib
from types import ModuleType

CANDIDATE_MODULES = [
    "app",                 # app.py -> app variable or create_app
    "run_app",             # optional
    "demo_webapp",         # package name if you used folder name
    "wsgi",                # common wsgi entry
]

def try_import(module_name: str) -> ModuleType | None:
    try:
        return importlib.import_module(module_name)
    except Exception:
        return None

def get_app_from_module(mod: ModuleType):
    # prefer `app` variable
    app = getattr(mod, "app", None)
    if app:
        return app
    # prefer create_app factory
    factory = getattr(mod, "create_app", None)
    if callable(factory):
        return factory()
    return None

def find_flask_app():
    # 1) check top-level modules
    for name in CANDIDATE_MODULES:
        mod = try_import(name)
        if mod:
            a = get_app_from_module(mod)
            if a:
                return a
    # 2) fallback: try importing from package root (this file's dir)
    # (useful if your app is structured differently)
    # If nothing found, raise helpful error
    raise RuntimeError(
        "Couldn't locate a Flask application.\n"
        "Make sure you have either:\n"
        " - an `app` Flask instance in app.py (e.g. app = Flask(__name__))\n"
        " - or a `create_app()` factory function that returns a Flask app.\n"
        "If your entry module has a different name, edit run.py to add it to CANDIDATE_MODULES."
    )

app = find_flask_app()

if __name__ == "__main__":
    host = os.environ.get("FLASK_RUN_HOST", "127.0.0.1")
    port = int(os.environ.get("FLASK_RUN_PORT", "5000"))
    debug = os.environ.get("FLASK_DEBUG", "1") in ("1", "true", "True", "yes")
    # Only enable debug when running this script directly - safe for local dev
    app.run(debug=True, host="127.0.0.1", port=5000)
