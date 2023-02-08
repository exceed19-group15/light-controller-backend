from typing import Optional

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
    is_on: Optional[bool]
    is_auto: Optional[bool]
    light_level: Optional[int]

    # at least 1 attribute must be present
    @validator("light_level")
    def valid_light_level(light_level: int, values: dict):
        if light_level > 100 or light_level < 0:
            raise ValueError("Light level can't be above 100 or below 0")

        if (
            light_level is None
            and values.get("is_on") is None
            and values.get("is_auto") is None
        ):
            raise ValueError("At least one attribute must be present")

        return light_level

    @validator("is_on")
    def valid_is_on(is_on: bool, values: dict):
        if is_on is None and values.get("light_level") is None:
            raise ValueError("At least one attribute must be present")
        return is_on

    @validator("is_auto")
    def valid_is_auto(is_auto: bool, values: dict):
        if is_auto is None and values.get("light_level") is None:
            raise ValueError("At least one attribute must be present")
        return is_auto
