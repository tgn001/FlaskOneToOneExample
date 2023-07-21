from db import db

class EmpDetailsModel(db.Model):
    __tablename__ = "empdetails"

    id = db.Column(db.Integer, primary_key=True)
    empcard = db.Column(db.Integer, unique=True, nullable=False)
    emp_id = db.Column(db.Integer, db.ForeignKey("employees.id"),  nullable=False, unique=True)

