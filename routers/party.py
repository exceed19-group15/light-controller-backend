from fastapi import APIRouter

from core.database import collection, db
from models.party import PartyModel

router = APIRouter(prefix="/party")


@router.get("/")
def get_party():
    pass


@router.put("/")
def post_party():
    pass
