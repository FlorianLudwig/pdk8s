# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from pydantic import BaseModel


class Info(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    build_date: str = Field(..., alias="buildDate")
    compiler: str
    git_commit: str = Field(..., alias="gitCommit")
    git_tree_state: str = Field(..., alias="gitTreeState")
    git_version: str = Field(..., alias="gitVersion")
    go_version: str = Field(..., alias="goVersion")
    major: str
    minor: str
    platform: str
