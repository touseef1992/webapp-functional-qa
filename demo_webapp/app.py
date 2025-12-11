from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "testsecretkey"

# Temporary in-memory database
users = {}

@app.route("/")
def home():
    return "Demo Web App Home — <a href='/login'>login</a> / <a href='/signup'>signup</a> / <a href='/dashboard'>dashboard</a>"

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        # Validation examples
        if not email:
            flash("Email is required", "error")
            return redirect(url_for("signup"))
        
        if "@" not in email:
            flash("Invalid email format", "error")
            return redirect(url_for("signup"))

        if email in users:
            flash("Email already exists", "error")
            return redirect(url_for("signup"))
        
        users[email] = password
        flash("Signup successful! Please login.", "success")
        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email not in users:
            flash("Invalid email or password", "error")
            return redirect(url_for("login"))

        if users[email] != password:
            flash("Invalid email or password", "error")
            return redirect(url_for("login"))
        
        session["user"] = email
        flash("Logged in successfully!", "success")
        return redirect(url_for("dashboard"))
    
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        flash("Please login first", "error")
        return redirect(url_for("login"))
    
    return render_template("dashboard.html", user=session["user"])


@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
