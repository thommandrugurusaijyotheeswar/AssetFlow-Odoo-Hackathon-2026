from flask import Blueprint, render_template, redirect, request
from datetime import datetime
from .models import Employee, Asset, Maintenance, Department, Category, Booking, Notification, AuditLog
from . import db


main = Blueprint("main", __name__)



# ---------------- Login ----------------

@main.route("/")
def login():
    return render_template("index.html")


@main.route("/login", methods=["POST"])
def login_redirect():

    email = request.form["email"]
    password = request.form["password"]

    if email == "admin@gmail.com" and password == "Admin@123":

        return redirect("/dashboard")

    return """
    <h2>Invalid Email or Password</h2>

    <a href="/">Try Again</a>
    """


# ---------------- Dashboard ----------------

@main.route("/dashboard")
def dashboard():

    total_employees = Employee.query.count()

    total_assets = Asset.query.count()

    available_assets = Asset.query.filter_by(status="Available").count()

    assigned_assets = Asset.query.filter_by(status="Assigned").count()

    maintenance_assets = Maintenance.query.count()

    total_bookings = Booking.query.count()

    return render_template(
        "dashboard.html",
        total_employees=total_employees,
        total_assets=total_assets,
        available_assets=available_assets,
        assigned_assets=assigned_assets,
        maintenance_assets=maintenance_assets,
        total_bookings=total_bookings
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

        notification = Notification(
        message=f"Employee '{employee.name}' added successfully",
        created_at=datetime.now().strftime("%d-%m-%Y %H:%M")
    )

        db.session.add(notification)

        audit = AuditLog(
            action=f"Employee Added: {employee.name}",
            user="Admin",
            created_at=datetime.now().strftime("%d-%m-%Y %H:%M")
        )

        db.session.add(audit)

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

        notification = Notification(
             message=f"Asset '{asset.asset_name}' registered",
            created_at=datetime.now().strftime("%d-%m-%Y %H:%M")
        )
        db.session.add(notification)

        audit = AuditLog(
            action=f"Asset Added: {asset.asset_name}",
            user="Admin",
            created_at=datetime.now().strftime("%d-%m-%Y %H:%M")
        )

        db.session.add(audit)

        db.session.commit()
 



        return redirect("/assets")

    return render_template("add_asset.html")



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

        notification = Notification(
            message=f"Maintenance request raised for {maintenance.asset_name}",
            created_at=datetime.now().strftime("%d-%m-%Y %H:%M")
        )

        db.session.add(notification)

        audit = AuditLog(
            action=f"Maintenance Requested: {maintenance.asset_name}",
            user="Employee",
            created_at=datetime.now().strftime("%d-%m-%Y %H:%M")
        )

        db.session.add(audit)

        db.session.commit()

        return redirect("/maintenance")

    return render_template("add_maintenance.html")

@main.route("/organization")
def organization():
    return render_template("organization.html")
@main.route("/departments")
def departments():

    departments = Department.query.all()

    return render_template(
        "departments.html",
        departments=departments
    )
@main.route("/add_department", methods=["GET", "POST"])
def add_department():

    if request.method == "POST":

        department = Department(
            name=request.form["name"],
            head=request.form["head"],
            status=request.form["status"]
        )

        db.session.add(department)
        db.session.commit()

        return redirect("/departments")

    return render_template("add_department.html")
@main.route("/categories")
def categories():

    categories = Category.query.all()

    return render_template(
        "categories.html",
        categories=categories
    )
@main.route("/add_category", methods=["GET", "POST"])
def add_category():

    if request.method == "POST":

        category = Category(
            name=request.form["name"],
            description=request.form["description"]
        )

        db.session.add(category)
        db.session.commit()

        return redirect("/categories")

    return render_template("add_category.html")

@main.route("/assign_asset/<int:id>", methods=["GET", "POST"])
def assign_asset(id):

    asset = Asset.query.get_or_404(id)

    if request.method == "POST":

        if asset.status == "Assigned":
            return "Asset already assigned. Please use Transfer Request."

        asset.assigned_to = request.form["assigned_to"]
        asset.expected_return = request.form["expected_return"]
        asset.status = "Assigned"

        notification = Notification(
            message=f"Asset '{asset.asset_name}' assigned to {asset.assigned_to}",
            created_at=datetime.now().strftime("%d-%m-%Y %H:%M")
        )

        db.session.add(notification)

        audit = AuditLog(
            action=f"Assigned {asset.asset_name} to {asset.assigned_to}",
            user="Admin",
            created_at=datetime.now().strftime("%d-%m-%Y %H:%M")
        )

        db.session.add(audit)

        db.session.commit()

        return redirect("/assets")

    return render_template(
        "allocate_asset.html",
        asset=asset
    )
@main.route("/transfer_asset/<int:id>", methods=["GET", "POST"])
def transfer_asset(id):

    asset = Asset.query.get_or_404(id)
    
    if request.method == "POST":

        asset.transfer_requested = True
        asset.transfer_to = request.form["employee"]
        asset.transfer_status = "Pending"

        db.session.commit()

        return redirect("/assets")

    return render_template(
        "transfer_asset.html",
        asset=asset
    )


@main.route("/approve_transfer/<int:id>")
def approve_transfer(id):

    asset = Asset.query.get_or_404(id)

    asset.assigned_to = asset.transfer_to
    asset.transfer_requested = False
    asset.transfer_status = "Approved"
    asset.transfer_to = ""

    audit = AuditLog(
        action=f"Transfer Approved: {asset.asset_name}",
        user="Asset Manager",
        created_at=datetime.now().strftime("%d-%m-%Y %H:%M")
    )

    db.session.add(audit)

    db.session.commit()

    return redirect("/assets")
    return redirect("/assets")
















# ---------------- Bookings ----------------

@main.route("/bookings")
def bookings():

    bookings = Booking.query.all()

    return render_template(
        "bookings.html",
        bookings=bookings
    )


@main.route("/add_booking", methods=["GET", "POST"])
def add_booking():

    if request.method == "POST":

        asset_name = request.form["asset_name"]
        booking_date = request.form["booking_date"]
        start_time = request.form["start_time"]
        end_time = request.form["end_time"]

        # Check for booking conflict
        existing = Booking.query.filter_by(
            asset_name=asset_name,
            booking_date=booking_date
        ).all()

        for booking in existing:

            if not (
                end_time <= booking.start_time or
                start_time >= booking.end_time
            ):
                return "Booking Conflict! This asset is already booked."

        booking = Booking(
            asset_name=asset_name,
            employee=request.form["employee"],
            booking_date=booking_date,
            start_time=start_time,
            end_time=end_time,
            status="Upcoming"
        )

        db.session.add(booking)

        notification = Notification(
            message=f"Booking created for {booking.asset_name}",
            created_at=datetime.now().strftime("%d-%m-%Y %H:%M")
        )

        db.session.add(notification)

        audit = AuditLog(
            action=f"Booking Created: {booking.asset_name}",
            user=booking.employee,
            created_at=datetime.now().strftime("%d-%m-%Y %H:%M")
        )

        db.session.add(audit)

        db.session.commit()

        return redirect("/bookings")

    return render_template("add_booking.html")
@main.route("/reports")
def reports():

    return render_template(
        "reports.html",

        total_assets=Asset.query.count(),

        available_assets=Asset.query.filter_by(status="Available").count(),

        assigned_assets=Asset.query.filter_by(status="Assigned").count(),

        total_employees=Employee.query.count(),

        total_bookings=Booking.query.count(),

        maintenance_requests=Maintenance.query.count()
    )




@main.route("/notifications")
def notifications():

    notifications = Notification.query.order_by(Notification.id.desc()).all()

    return render_template(
        "notifications.html",
        notifications=notifications
    )



@main.route("/audit_logs")
def audit_logs():

    logs = AuditLog.query.order_by(AuditLog.id.desc()).all()

    return render_template(
        "audit_logs.html",
        logs=logs
    )


@main.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "POST":

        email = request.form["email"]

        return f"""
        <h2>Password Reset Request</h2>

        <p>Password reset link sent to:</p>

        <b>{email}</b>

        <br><br>

        <a href="/">Back to Login</a>
        """

    return render_template("forgot_password.html")