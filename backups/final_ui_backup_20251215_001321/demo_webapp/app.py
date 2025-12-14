from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    make_response
)

app = Flask(__name__)
app.secret_key = "testsecretkey"

# Temporary in-memory user store (QA demo)
users = {}


@app.route("/")
def home():
    return "Demo Web App Home — <a href='/login'>Login</a> / <a href='/signup'>Signup</a>"


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        # Server-side validations
        if not email:
            flash("Email is required", "error")
            return redirect(url_for("signup"))

        if "@" not in email:
            flash("Invalid email format", "error")
            return redirect(url_for("signup"))

        if not password:
            flash("Password is required", "error")
            return redirect(url_for("signup"))

        if len(password) < 8:
            flash("Password must be at least 8 characters", "error")
            return redirect(url_for("signup"))

        # Existing user check
        if email in users:
            flash("User already exists. Do you want to sign in?", "warning")
            return redirect(url_for("login"))

        users[email] = password
        flash("Signup successful! Please login.", "success")
        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if email not in users or users[email] != password:
            flash("Invalid email or password", "error")
            return redirect(url_for("login"))

        session["user"] = email
        flash("Logged in successfully!", "success")
        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        flash("Please login first", "warning")
        return redirect(url_for("login"))

    response = make_response(render_template("dashboard.html"))
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    return response

    stats = {
        "total_users": 3,
        "active_sessions": 4,
        "signups_today": 2,
        "open_issues": 5,
        "total_sessions": 32,
    }

    return render_template(
        "dashboard.html",
        user=session["user"],
        stats=stats
    )


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("You have been logged out successfully.", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
