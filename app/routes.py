from flask import Blueprint, render_template, redirect

main = Blueprint("main", __name__)

@main.route("/")
def login():
    return render_template("index.html")

@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@main.route("/login")
def login_redirect():
    return redirect("/dashboard")