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

    asset_id = db.Column(db.String(20), unique=True, nullable=False)
    asset_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    purchase_date = db.Column(db.String(20))

    assigned_to = db.Column(db.String(100), default="Not Assigned")

    status = db.Column(db.String(30), default="Available")