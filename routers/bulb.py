from fastapi import APIRouter

from models.bulb import BulbModel, BulbPutModel
from core.database import collection
from typing import List, Dict

router = APIRouter(prefix="/bulb")


@router.get("/")
def get_all_bulb() -> List[BulbModel]:
    return list(collection.find({}, {"_id": 0}))


@router.get("/{bulb_id}")
def get_bulb(bulb_id: int) -> BulbModel:
    return collection.find_one({"bulb_id": bulb_id}, {"_id": 0})


@router.put("/{bulb_id}")
def put_bulb(bulb_id: int, bulb_body: BulbPutModel) -> Dict[str, str]:
    collection.update_one({"bulb_id": bulb_id}, {"$set": bulb_body.dict()})
    return {"message": "Update successful"}
