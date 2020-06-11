# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from pydantic import BaseModel


class RawExtension(BaseModel):
    pass

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"
