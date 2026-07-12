from flask import Blueprint, render_template, redirect, request
from .models import Employee
from . import db

main = Blueprint("main", __name__)

# ---------------- Login ----------------

@main.route("/")
def login():
    return render_template("index.html")


@main.route("/login")
def login_redirect():
    return redirect("/dashboard")


# ---------------- Dashboard ----------------

@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------------- Employees ----------------

@main.route("/employees")
def employees():

    employees = Employee.query.all()

    return render_template(
        "employees.html",
        employees=employees
    )


# ---------------- Add Employee ----------------

@main.route("/add_employee", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        employee = Employee(
            emp_id=request.form["emp_id"],
            name=request.form["name"],
            department=request.form["department"],
            email=request.form["email"],
            status="Active"
        )

        db.session.add(employee)
        db.session.commit()

        return redirect("/employees")

    return render_template("add_employee.html")