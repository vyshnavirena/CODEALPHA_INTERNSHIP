from flask import Flask, render_template, request
import os 

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Secure Coding Review Project</h1><p>Application is running!</p>"

@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        admin_username = os.getenv("ADMIN_USERNAME", "admin")
        admin_password = os.getenv("ADMIN_PASSWORD", "admin123")

        if not username or not password:
            message = "Username and password are required!"
        elif len(username) > 30 or len(password) > 100:
            message = "Input is too long!"
        elif username == admin_username and password == admin_password:
            message = "Login successful!"
        else:
            message = "Invalid username or password!"

    return render_template("login.html", message=message)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            return "Username and password are required!"

        if len(username) > 30 or len(password) > 100:
            return "Input is too long!"

        return "Registration successful!"

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=False)