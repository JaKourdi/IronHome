import base64
from json import JSONDecodeError

from bson import ObjectId
from flask import request, Blueprint, jsonify
from bson.json_util import dumps, loads
import logging

from schemas.order import OrderSchema
from utils import db
from auth_middleware import token_required

bp = Blueprint("order", __name__, url_prefix="/order")
logger = logging.getLogger(__name__)


@bp.route("/list")
@token_required
def list_order(user_id):
    logger.info("Request to /list received userid %s" % user_id)
    order_collection = db.get_collection("order")
    order_data = list(order_collection.find(
        {"usernameId": ObjectId(user_id['_id'])}
    ))
    json_purchases_data = dumps(order_data)
    return json_purchases_data


@bp.route("/write", methods=['POST'])
@token_required
def add_order(user_id):
    # Adding a Purchase
    logger.info("Request to /add received %s" % (list(request.json)))
    # Validate the incoming JSON data against the JSON schema
    validation_errors = OrderSchema().validate(data=request.json)
    if validation_errors:
        return f"%s" % validation_errors, 400
    purchases_collection = db.get_collection("order")
    logger.info(type(request.json))
    # add userid to order - user already authenticated
    request.json['usernameId'] = user_id['_id']
    inserted_id = purchases_collection.insert_one(request.json).inserted_id
    return f"purchase was inserted with id %s" % inserted_id, 200


@bp.route("/read", methods=['GET'])
def search_order():
    # Searching a order with various references - json is encoded in GET as parameter
    encoded_data = request.values.get("data")
    try:
        # Decode the Base64 string to bytes
        decoded_bytes = base64.urlsafe_b64decode(encoded_data)
        json_str = decoded_bytes.decode('utf-8')
    except base64.binascii.Error as e:
        logger.error("Base64 decoding error: %s" % str(e))
        return f"error during decoding", 400
    except UnicodeDecodeError as e:
        logger.error("UTF-8 decoding error: %s" % str(e))
        return f"error during decoding", 400
    except JSONDecodeError as e:
        logger.error("JSON decoding error: %s" % str(e))
        return f"error during decoding", 400
    except Exception as e:
        logger.error("Unexpected error: %s" % str(e))
        return f"error during decoding", 400

    json_data = loads(json_str)
    order_collection = db.get_collection("order")
    order_data = order_collection.find(json_data)
    return jsonify(dumps(order_data))

