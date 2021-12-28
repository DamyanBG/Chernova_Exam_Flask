from marshmallow import Schema, fields, validate
from schemas.bases import BaseOrderSchema


class OrderCreateResponseSchema(BaseOrderSchema):
    pk = fields.Integer(required=True)
    stl_url = fields.String(required=True, validate=validate.Length(max=255))
    create_on = fields.DateTime(required=True)
