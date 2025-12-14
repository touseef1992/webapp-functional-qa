# ============================================================
# CLEAN PRODUCTION-READY FLASK APP FOR demo_webapp
# ============================================================

from flask import (
    Flask, render_template, request,
    redirect, url_for, session, current_app
)
import logging
from datetime import datetime
import time

# TEMPORARY IN-MEMORY USER STORE (REPLACE WITH DATABASE LATER)
USER_DB = {}  
# Format: USER_DB[email] = {"password": "1234"}

# ------------------------------------------------------------
# CREATE FLASK APP
# ------------------------------------------------------------
app = Flask(__name__)
app.secret_key = "your-secret-key"   # TODO: replace with environment secret

# ------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------
app.config["SESSION_TIMEOUT_SECONDS"] = 4 * 60 * 60  # 4 hours
app.config.setdefault("DEFAULT_THEME", "dark")

# Example placeholder session map data (UI uses this)
app.config["SESSIONS_LIST"] = [
    {"label": "North America", "count": 14, "pct": "43%"},
    {"label": "Europe",        "count": 10, "pct": "31%"},
    {"label": "India",         "count": 6,  "pct": "18%"},
    {"label": "SEA",           "count": 2,  "pct": "6%"},
]

# Placeholder dashboard stats
app.config["DASHBOARD_STATS"] = {
    "total_users": 3,
    "active_sessions": 4,
    "signups_today": 2,
    "open_issues": 5,
}

# ------------------------------------------------------------
# LOGGING
# ------------------------------------------------------------
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# ------------------------------------------------------------
# SESSION TIMEOUT HANDLER (before_request)
# ------------------------------------------------------------
@app.before_request
def update_last_activity():
    """
    Auto-logout after 4 hours of inactivity.
    Must run *after* imports and app creation.
    """
    try:
        # If user already has activity stored
        if "last_activity" in session:
            inactive_seconds = time.time() - session["last_activity"]
            if inactive_seconds > app.config["SESSION_TIMEOUT_SECONDS"]:
                logger.info("Session expired — logging user out.")
                session.clear()
                return redirect(url_for("login"))

        # Update last activity timestamp
        session["last_activity"] = time.time()

    except Exception as e:
        logger.error(f"Session timeout error: {e}")


# ------------------------------------------------------------
# HELPERS
# ------------------------------------------------------------
def get_safe_sessions():
    """
    Returns a safe list of session-info dicts for the UI.
    Avoids crashes if config values are None.
    """
    try:
        sessions = current_app.config.get("SESSIONS_LIST", [])
        if not sessions:
            return []
        return sessions
    except Exception:
        logger.exception("Failed to load sessions list")
        return []


def get_safe_stats():
    """
    Returns safe dashboard stats.
    """
    try:
        stats = current_app.config.get("DASHBOARD_STATS", None)
        if not stats:
            return {
                "total_users": 0,
                "active_sessions": 0,
                "signups_today": 0,
                "open_issues": 0,
            }
        return stats
    except Exception:
        logger.exception("Failed to load stats")
        return {}


# ------------------------------------------------------------
# ROUTES
# ------------------------------------------------------------

# ---------- SIGNUP ----------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()

        if not email or not password:
            return render_template("signup.html", error="Email and password are required.")

        if email in USER_DB:
            return render_template("signup.html", error="Email already registered.")

        # Store user
        USER_DB[email] = {"password": password}
        session["user_email"] = email

        return redirect(url_for("dashboard"))

    return render_template("signup.html")

# ---------- LOGIN ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()

        if not email or not password:
            return render_template("login.html", error="Email and password are required.")

        user = USER_DB.get(email)

        if not user:
            return render_template("login.html", error="User not found.")

        if user["password"] != password:
            return render_template("login.html", error="Incorrect password.")

        # Login successful
        session["user_email"] = email
        return redirect(url_for("dashboard"))

    return render_template("login.html")


# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ---------- DASHBOARD ----------
@app.route("/dashboard")
def dashboard():
    """
    Dashboard page:
      - Requires login
      - Shows stats
      - Shows session map data
      - Shows user email and theme
    """
    # Require login
    user_email = session.get("user_email")
    if not user_email:
        return redirect(url_for("login"))

    # Load stats + session map
    stats = get_safe_stats()
    sessions_list = get_safe_sessions()

    theme = session.get("theme", "dark")
    server_time = datetime.utcnow().isoformat() + "Z"

    logger.debug(
        "Dashboard render — stats=%s, sessions=%d, theme=%s, user=%s",
        stats, len(sessions_list), theme, user_email
    )

    return render_template(
        "dashboard.html",
        stats=stats,
        sessions=sessions_list,
        theme=theme,
        user_email=user_email,
        server_time=server_time,
    )


# ---------- HOME REDIRECT ----------
@app.route("/")
def home():
    return redirect(url_for("login"))


# ------------------------------------------------------------
# MAIN ENTRY
# ------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
