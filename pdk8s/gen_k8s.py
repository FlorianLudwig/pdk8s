import pathlib
import datetime
import os
import json
import re
from typing import (
    IO,
    Any,
    Callable,
    DefaultDict,
    Dict,
    Iterator,
    Optional,
    Type,
    TypeVar,
)



VERSION = re.compile("v[0-9]+[a-z0-9]*$")


def update_schema(schema: dict):
    """Adapt the kubernetes OpenAPI schema to our needs
    """
    for name, definition in schema["definitions"].items():
        version = name.split(".")[-2]

        if not VERSION.match(version):
            version = None

        if "properties" in definition:
            for prop_name, prop in definition["properties"].items():
                # set the default of properties that are enums
                # with only one possible value to that value
                # This sets the `kind` property on all objects.
                if "enum" in prop and len(prop["enum"]) == 1:
                    prop.setdefault("default", prop["enum"][0])
                
                # set api version
                if prop_name == "apiVersion":
                    assert version is not None, f"Unkown api version for {name}"
                    prop.setdefault("default", version)
