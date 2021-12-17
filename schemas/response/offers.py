from marshmallow import Schema, fields, validate
from marshmallow_enum import EnumField

from models import State


class OfferCreateResponseSchema(Schema):
    pk = fields.Integer(required=True)
    title = fields.String(required=True, validate=validate.Length(max=100))
    amount = fields.Float(required=True)
    order_pk = fields.Integer(required=True)
    create_on = fields.DateTime(required=True)
    status = EnumField(State, by_value=True)
