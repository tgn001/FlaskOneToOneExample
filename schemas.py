from marshmallow import Schema, fields

class EmpDetailsSchema(Schema):
    id = fields.Str(dump_only=True)
    emp_id = fields.Str(dump_only=True)
    empcard = fields.Str(required=True)


class EmpDetailsUpdateSchema(Schema):
    empcard = fields.Str()


class EmployeeSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    role = fields.Str(required=True)
    empdetails = EmpDetailsSchema

class EmployeeUpdateSchema(Schema):
    name = fields.Str()
    role = fields.Str()
