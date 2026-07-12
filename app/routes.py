from flask import Blueprint, render_template, redirect, request
from .models import Employee, Asset, Maintenance
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

    total_employees = Employee.query.count()

    total_assets = Asset.query.count()

    available_assets = Asset.query.filter_by(status="Available").count()

    assigned_assets = Asset.query.filter_by(status="Assigned").count()

    return render_template(
        "dashboard.html",
        total_employees=total_employees,
        total_assets=total_assets,
        available_assets=available_assets,
        assigned_assets=assigned_assets
    )


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

@main.route("/assets")
def assets():

    assets = Asset.query.all()

    return render_template(
        "assets.html",
        assets=assets
    )


@main.route("/add_asset", methods=["GET", "POST"])
def add_asset():

    if request.method == "POST":

        asset = Asset(
            asset_id=request.form["asset_id"],
            asset_name=request.form["asset_name"],
            category=request.form["category"],
            purchase_date=request.form["purchase_date"],
            status="Available"
        )

        db.session.add(asset)
        db.session.commit()

        return redirect("/assets")

    return render_template("add_asset.html")


@main.route("/assign_asset/<int:id>", methods=["GET", "POST"])
def assign_asset(id):

    asset = Asset.query.get_or_404(id)
    employees = Employee.query.all()

    if request.method == "POST":
        asset.assigned_to = request.form["employee"]
        asset.status = "Assigned"

        db.session.commit()

        return redirect("/assets")

    return render_template(
        "assign_asset.html",
        asset=asset,
        employees=employees
    )
@main.route("/edit_asset/<int:id>", methods=["GET", "POST"])
def edit_asset(id):

    asset = Asset.query.get_or_404(id)

    if request.method == "POST":

        asset.asset_id = request.form["asset_id"]
        asset.asset_name = request.form["asset_name"]
        asset.category = request.form["category"]
        asset.purchase_date = request.form["purchase_date"]

        db.session.commit()

        return redirect("/assets")

    return render_template(
        "edit_asset.html",
        asset=asset
    )
@main.route("/delete_asset/<int:id>")
def delete_asset(id):

    asset = Asset.query.get_or_404(id)

    db.session.delete(asset)

    db.session.commit()

    return redirect("/assets")
@main.route("/edit_employee/<int:id>", methods=["GET", "POST"])
def edit_employee(id):

    employee = Employee.query.get_or_404(id)

    if request.method == "POST":

        employee.emp_id = request.form["emp_id"]
        employee.name = request.form["name"]
        employee.department = request.form["department"]
        employee.email = request.form["email"]

        db.session.commit()

        return redirect("/employees")

    return render_template("edit_employee.html", employee=employee)


@main.route("/delete_employee/<int:id>")
def delete_employee(id):

    employee = Employee.query.get_or_404(id)

    db.session.delete(employee)

    db.session.commit()

    return redirect("/employees")
@main.route("/maintenance")
def maintenance():

    records = Maintenance.query.all()

    return render_template(
        "maintenance.html",
        records=records
    )


@main.route("/add_maintenance", methods=["GET", "POST"])
def add_maintenance():

    if request.method == "POST":

        maintenance = Maintenance(
            asset_name=request.form["asset_name"],
            issue=request.form["issue"],
            request_date=request.form["request_date"],
            status="Pending"
        )

        db.session.add(maintenance)
        db.session.commit()

        return redirect("/maintenance")

    return render_template("add_maintenance.html")