"""Application Models"""
import logging

import bson

from utils import db
from werkzeug.security import generate_password_hash, check_password_hash

client = db.get_client()
mydb = db.get_collection("user")
logger = logging.getLogger(__name__)


class User:
    def __init__(self):
        return

    def create(self, username, password):
        user = self.get_by_username(username)
        logger.info("res  %s " % user)
        if user:
            logger.info("already exist %s " % user)
            return
        new_user = mydb.insert_one(
            {
                "username": username,
                "password": self.encrypt_password(password),
                "active": True
            },
        )

        inserted_id = new_user.inserted_id
        logging.info("sasa %s" % inserted_id)
        return self.get_by_id(inserted_id)

    def get_all(self):
        users = mydb.find({"active": True})
        return [{**user, "_id": str(user["_id"])} for user in users]

    def get_by_id(self, user_id):
        user = mydb.find_one({"_id": bson.ObjectId(user_id), "active": True})
        if not user:
            return
        user["_id"] = str(user["_id"])
        user.pop("password")
        return user

    def get_by_username(self, username):
        user = mydb.find_one({"username": username, "active": True})
        if not user:
            return
        user["_id"] = str(user["_id"])
        return user

    def delete(self, user_id):
        # TODO: cascade delete other items related to user.
        user = mydb.delete_one({"_id": bson.ObjectId(user_id)})

    def disable_account(self, user_id):
        user = mydb.update_one(
            {"_id": bson.ObjectId(user_id)},
            {"$set": {"active": False}}
        )
        user = self.get_by_id(user_id)
        return user

    def encrypt_password(self, password):
        return generate_password_hash(password)

    def login(self, username, password):
        user = self.get_by_username(username)
        if not user or not check_password_hash(user["password"], password):
            return
        user.pop("password")
        return user
