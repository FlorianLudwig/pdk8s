from typing import Optional

import pydantic


def _set_name(metadata, value):
    if metadata is None:
        return {"name": value}

    if isinstance(metadata, dict):
        metadata["name"] = value
    else:
        metadata.name = value

    return metadata


class NamedModel(pydantic.BaseModel):
    def _get_name(self) -> Optional[str]:
        if not self.metadata:
            return None
        return self.metadata.name

    name = property(_get_name)

    def __setattr__(self, name, value):
        if name == "name":
            self.metadata = _set_name(self.metadata, value)
        else:
            super().__setattr__(name, value)

    @pydantic.root_validator(pre=True)
    def extract_name(cls, values):
        if "name" in values:
            values["metadata"] = _set_name(values.get("metadata"), values["name"])
            del values["name"]

        return values
