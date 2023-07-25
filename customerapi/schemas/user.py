from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)
    account_id = fields.Integer(required=True)
    description = fields.String(required=True)
    password = fields.String(required=True)