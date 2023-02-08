from fastapi import APIRouter

from core.database import collection, db
from models.bulb import BulbModel, BulbPutModel

router = APIRouter(prefix="/bulb")


@router.get("/")
def get_all_bulb():
    pass


@router.get("/{bulb_id}")
def get_bulb():
    pass


@router.put("/{bulb_id}")
def put_bulb():
    pass
