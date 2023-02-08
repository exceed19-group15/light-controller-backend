from pydantic import BaseModel, validator


class PartyModel(BaseModel):
    party: bool
