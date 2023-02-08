from typing import Dict, List

from fastapi import APIRouter

from core.database import collection
from models.bulb import BulbModel, BulbPutModel

router = APIRouter(prefix="/bulb")


@router.get("/")
def get_all_bulb() -> List[BulbModel]:
    return list(collection.find({}, {"_id": 0}))


@router.get("/{bulb_id}")
def get_bulb(bulb_id: int) -> BulbModel:
    return collection.find_one({"bulb_id": bulb_id}, {"_id": 0})


@router.put("/{bulb_id}")
def put_bulb(bulb_id: int, bulb_body: BulbPutModel) -> Dict[str, str]:
    update_body = bulb_body.dict()

    for k in tuple(update_body.keys()):
        if update_body[k] is None:
            del update_body[k]

    collection.update_one({"bulb_id": bulb_id}, {"$set": update_body})
    return {"message": "Update successful"}
