from marshmallow import Schema, fields
from marshmallow_enum import EnumField
from schemas.bases import BaseOfferSchema

from models import State


class OfferCreateResponseSchema(BaseOfferSchema):
    pk = fields.Integer(required=True)
    create_on = fields.DateTime(required=True)
    status = EnumField(State, by_value=True)
