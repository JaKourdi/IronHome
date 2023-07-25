import os
import urllib

from bson import CodecOptions
from bson.raw_bson import RawBSONDocument
from pymongo import MongoClient


def get_client():
    mongodb_host = os.environ.get('MONGODB_HOSTNAME', 'localhost')
    mongodb_username = os.environ.get('MONGO_USERNAME', 'root')
    mongodb_password = os.environ.get('MONGO_PASSWORD', 'mongoadmin')
    mongodb_port = int(os.environ.get('MONGO_PORT', '27017'))

    # https://api.mongodb.com/python/3.5.0/examples/authentication.html#percent-escaping-username-and-password
    username = urllib.parse.quote_plus(mongodb_username)
    password = urllib.parse.quote_plus(mongodb_password)
    return MongoClient('mongodb://%s:%s@%s:%s' % (username, password, mongodb_host, mongodb_port))


def get_db():
    return get_client().get_database("customermgmt")


def get_collection(collection_name="purchase"):
    return get_db().get_collection(collection_name)
