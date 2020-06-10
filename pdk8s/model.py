import pydantic


class NamedModel(pydantic.BaseModel):
    @pydantic.root_validator(pre=True)
    def extract_name(cls, values):
        if "name" in values:
            if "metadata" in values:
                raise NotImplementedError("provide name or metadata")
            
            values["metadata"] = {"name": values["name"]}
            del values["name"]

        return values

