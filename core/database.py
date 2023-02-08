import os

from pymongo import MongoClient

client = MongoClient(
    f"mongodb://{os.getenv('mongo_username')}:{os.getenv('mongo_password')}@{os.getenv('mongo_host')}:{os.getenv('mongo_port')}"
)

db = client["exceed15"]

if "light_bulb" not in db.list_collection_names():
    db.create_collection("light_bulb")

collection = db["light_bulb"]
