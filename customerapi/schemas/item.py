from marshmallow import Schema, fields


class ItemSchema(Schema):
    name = fields.String(required=True)
    description = fields.String()
    available = fields.Boolean(required=True, default=True)
    cost = fields.Float(required=True)
