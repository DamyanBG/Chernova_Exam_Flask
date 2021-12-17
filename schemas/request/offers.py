from marshmallow import Schema, fields, validate


class OfferCreateRequestSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(max=100))
    amount = fields.Float(required=True)
    order_pk = fields.Integer(required=True)
