from pydantic import BaseModel, validator


class BulbModel(BaseModel):
    bulb_id: int
    room_name: str
    is_on: bool
    is_auto: bool
    light_level: int

    @validator("light_level")
    def valid_light_level(light_level: int):
        if light_level > 100 or light_level < 0:
            raise ValueError("Light level can't be above 100 or below 0")
        return light_level


class BulbPutModel(BaseModel):
    is_on: bool
    is_auto: bool
    light_level: int

    @validator("light_level")
    def valid_light_level(light_level: int):
        if light_level > 100 or light_level < 0:
            raise ValueError("Light level can't be above 100 or below 0")
        return light_level
