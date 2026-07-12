from . import db

# ---------------- Employee ----------------

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    emp_id = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.String(20), default="Active")


# ---------------- Asset ----------------

class Asset(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    asset_id = db.Column(db.String(50), unique=True)

    asset_name = db.Column(db.String(100))

    category = db.Column(db.String(100))

    purchase_date = db.Column(db.String(20))

    assigned_to = db.Column(db.String(100), default="")

    expected_return = db.Column(db.String(20), default="")

    status = db.Column(db.String(30), default="Available")

    transfer_requested = db.Column(db.Boolean, default=False)

    transfer_to = db.Column(db.String(100), default="")

    transfer_status = db.Column(db.String(30), default="None")
class Maintenance(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    asset_name = db.Column(db.String(100), nullable=False)
    issue = db.Column(db.String(300), nullable=False)
    request_date = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(30), default="Pending")
class Department(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), unique=True)

    head = db.Column(db.String(100))

    status = db.Column(db.String(20), default="Active")


class Category(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), unique=True)

    description = db.Column(db.String(200))





    # ---------------- Booking ----------------

class Booking(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    asset_name = db.Column(db.String(100))

    employee = db.Column(db.String(100))

    booking_date = db.Column(db.String(20))

    start_time = db.Column(db.String(20))

    end_time = db.Column(db.String(20))

    status = db.Column(db.String(30), default="Upcoming")









    # ---------------- Notifications ----------------

class Notification(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    message = db.Column(db.String(300))

    created_at = db.Column(db.String(30))

    status = db.Column(db.String(20), default="Unread")









    # ---------------- Audit Logs ----------------

class AuditLog(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    action = db.Column(db.String(300))

    user = db.Column(db.String(100))

    created_at = db.Column(db.String(30))