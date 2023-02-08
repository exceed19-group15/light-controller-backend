import os

from pymongo import MongoClient

from .constants import *

client = MongoClient(
    f"mongodb://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@{MONGO_DB_HOST}:{MONGO_DB_PORT}"
)

db = client["exceed15"]

if "light_bulb" not in db.list_collection_names():
    db.create_collection("light_bulb")

collection = db["light_bulb"]
