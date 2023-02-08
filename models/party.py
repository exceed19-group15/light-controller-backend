from pydantic import BaseModel


class PartyPutModel(BaseModel):
    party: bool
