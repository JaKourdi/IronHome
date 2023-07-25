from bson import ObjectId
from marshmallow import Schema, fields


# Proper handling of MongoDB ObjectId data.
class ObjectIdField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return str(value)

    def _deserialize(self, value, attr, data, **kwargs):
        if value is None:
            return None
        try:
            return ObjectId(value)
        except Exception as exc:
            raise self.make_error('invalid', input=value, obj_type=type(data))


class OrderItemSchema(Schema):
    itemId = fields.String(required=True)


class OrderSchema(Schema):
    name = fields.String(required=True)
    description = fields.String()
    total = fields.Float(required=True)
    items = fields.List(fields.Nested(OrderItemSchema()), required=True)