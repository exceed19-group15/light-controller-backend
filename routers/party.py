from typing import Dict

from fastapi import APIRouter

from models.party import PartyPutModel

router = APIRouter(prefix="/party")
party_state: bool = False


@router.get("/")
def get_party() -> Dict[str, bool]:
    return {"party": party_state}


@router.put("/")
def put_party(party: PartyPutModel) -> Dict[str, str]:
    body = party.dict()
    global party_state
    party_state = body["party"]
    return {"message": "Update successful"}
