from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import EmpDetailsModel
from schemas import EmpDetailsSchema, EmpDetailsUpdateSchema

empdetailsblueprint = Blueprint("EmpDetails", "empdetails", description="TechGeekNext - Employee Details CRUD operations")


@empdetailsblueprint.route("/employee/<string:emp_id>/empdetails")
class EmployeeAdd(MethodView):

    @empdetailsblueprint.arguments(EmpDetailsSchema)
    @empdetailsblueprint.response(201, EmpDetailsSchema)
    def post(self, empdetails_data, emp_id):
        detail = EmpDetailsModel(**empdetails_data, emp_id=emp_id)
        try:
            db.session.add(detail)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while creating an employee details.")

        return


@empdetailsblueprint.route("/empdetails/<string:emp_id>")
class EmpDetails(MethodView):
    @empdetailsblueprint.response(200, EmpDetailsSchema)
    def get(self, emp_id):
        return EmpDetailsModel.query.get_or_404(emp_id)


    def delete(self, emp_id):
        emp = EmpDetailsModel.query.get_or_404(emp_id)
        db.session.delete(emp)
        db.session.commit()
        return {"message": "Employee Details deleted."}


@empdetailsblueprint.route("/empdetails")
class GetAllEmpDetails(MethodView):
    @empdetailsblueprint.response(200, EmpDetailsSchema(many=True))
    def get(self):
        return EmpDetailsModel.query.all()

