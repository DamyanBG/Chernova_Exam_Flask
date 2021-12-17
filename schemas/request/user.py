from marshmallow import Schema, fields, validate


class BaseUserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=255))


class CustomerLoginRequestSchema(BaseUserSchema):
    pass


class CustomerRegisterRequestSchema(BaseUserSchema):
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    phone = fields.String(required=True, validate=validate.Length(min=9, max=20))


class RequestCreateAdminSchema(BaseUserSchema):
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    phone = fields.String(required=True, validate=validate.Length(min=9, max=20))


class AdminLoginRequestSchema(BaseUserSchema):
    pass


class RequestCreateWorkerSchema(BaseUserSchema):
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    phone = fields.String(required=True, validate=validate.Length(min=9, max=20))


class WorkerLoginRequestSchema(BaseUserSchema):
    pass
