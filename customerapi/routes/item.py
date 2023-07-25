from flask import request, Blueprint
from bson.json_util import dumps
import logging

from schemas.purchase import PurchaseSchema
from utils import db

from auth_middleware import token_required

bp = Blueprint("item", __name__, url_prefix="/item")

logger = logging.getLogger(__name__)


@bp.route("/list")
@token_required
def list_items(user_id):
    logger.info("Request to /list received")
    purchases_collection = db.get_collection("item")
    purchases_data = list(purchases_collection.find(
        # list only available items
        {"available": True}
    ))
    json_purchases_data = dumps(purchases_data)
    return json_purchases_data


@bp.route("/buy", methods=['POST'])
@token_required
def buy(user_id):
    # Adding a Purchase
    logger.info("Request to /buy received %s" % (list(request.json)))
    # Validate the incoming JSON data against the JSON schema
    validation_errors = ItemSchema().validate(data=request.json)
    if validation_errors:
        return f"%s" % validation_errors, 400
    purchases_collection = db.get_collection("purchase")
    inserted_id = purchases_collection.insert_one(request.json).inserted_id
    return f"purchase was inserted with id %s" % inserted_id, 200
