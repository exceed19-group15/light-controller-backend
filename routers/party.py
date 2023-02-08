from fastapi import APIRouter

from models.party import PartyModel

router = APIRouter(prefix="/party")
party_state: bool = False


@router.get("/")
def get_party():
    return {"party": party_state}


@router.put("/")
def put_party(party: PartyModel):
    body = party.dict()
    global party_state
    party_state = body["party"]
    return "Update successful"
