from marshmallow import Schema, fields, validate


class OrderCreateRequestSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(max=100))
    description = fields.String(required=True, validate=validate.Length(max=255))
    stl_url = fields.String(required=True, validate=validate.Length(max=255))
    address = fields.String(required=True, validate=validate.Length(max=255))
