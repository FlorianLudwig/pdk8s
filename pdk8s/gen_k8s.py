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


import datamodel_code_generator
import datamodel_code_generator.format
import datamodel_code_generator.imports

from datamodel_code_generator.parser.jsonschema import JsonSchemaParser
from datamodel_code_generator.parser.openapi import OpenAPIParser
from datamodel_code_generator import (
    DEFAULT_BASE_CLASS,
    Error,
    InputFileType,
    enable_debug_message,
)

from datamodel_code_generator.model.pydantic import (
    BaseModel,
    CustomRootType,
    DataModelField,
    dump_resolve_reference_action,
)


_underscorer1 = re.compile(r"(.)([A-Z][a-z]+)")
_underscorer2 = re.compile("([a-z0-9])([A-Z])")


def camel_to_snake(string):
    subbed = _underscorer1.sub(r"\1_\2", string)
    return _underscorer2.sub(r"\1_\2", subbed).lower()


VERSION = re.compile("v[0-9]+[a-z0-9]*$")


def make_named_class(model: BaseModel):
    model.base_class = "pdk8s.model.NamedModel"
    model.BASE_CLASS = "pdk8s.model.NamedModel"
    cls_import = datamodel_code_generator.imports.Import(import_="pdk8s.model")
    model.imports.append(cls_import)


def snakify_field(field: datamodel_code_generator.model.pydantic.DataModelField):
    original_name = field.name
    field.name = camel_to_snake(original_name)
    if field.name != original_name:
        field.alias = original_name


def remove_int_or_str(
    model, field: datamodel_code_generator.model.pydantic.DataModelField
):
    # the type_hint is cached and not recalculated - in the case
    # luckily as the data structure does not support the needed type hint
    # see also https://github.com/koxudaxi/datamodel-code-generator/issues/142

    union_import = datamodel_code_generator.imports.Import(
        from_="typing", import_="Union"
    )
    optional_import = datamodel_code_generator.imports.Import(
        from_="typing", import_="Optional"
    )
    if field.required:
        field.type_hint = "Union[int, str]"
        field.imports = [union_import]
    else:
        field.type_hint = "Optional[Union[int, str]]"
        field.imports = [union_import, optional_import]

    # cleanup model imports
    to_remove = []
    for import_ in model.imports:
        if "IntOrString" in import_.import_:
            to_remove.append(import_)

    for import_ in to_remove:
        model.imports.remove(import_)

    model.imports.extend(field.imports)


class K8SParser(JsonSchemaParser):
    def parse_raw(self):
        super(K8SParser, self).parse_raw()

        # self._classes_by_name = {}
        # self._single_value_enum = {}
        # for result in self.results:
        #     if result.base_class == "Enum":
        #         if len(result.fields) == 1:
        #             name = result.class_name
        #             assert name not in self._single_value_enum
        #             self._single_value_enum[name] = result.fields[0].name
        #         else:
        #             breakpoint
        # name = result.class_name
        # assert name not in self._classes_by_name
        # self._classes_by_name[name] = result

        new_results = []
        for result in self.results:
            self._mutate_class(result)
            new_results.append(result)

        self.results = new_results

    # top level objects:
    # x-kubernetes-group-version-kind

    def _mutate_class(self, model: datamodel_code_generator.model.DataModel):
        if model.class_name == "Model":
            return

        if len(model.fields) == 1 and model.fields[0].name is None:
            # defintion of a basic type, skip
            return

        if model.class_name == "IntOrString":
            # TODO
            return

        extra = '"forbid"'

        for field in model.fields:
            if field.name == "metadata":
                # For named classes we allow extra fields
                # so we have a nicer API with cls(name="Foo")
                # even with no actual field "name" existing.
                extra = '"allow"'
                make_named_class(model)

            if (
                len(field.data_types) == 1
                and field.data_types[0].type
                == "io.k8s.apimachinery.pkg.util.intstr.IntOrString"
            ):
                remove_int_or_str(model, field)

            snakify_field(field)

        model.extra_template_data["config"] = {"extra": extra}


def update_field(field):
    field_arguments = [
        f"{k}={field.get_valid_argument(v)}"
        for k, v in field.dict(include=field._FIELDS_KEYS).items()
        if v is not None
    ]
    field.field = f'Field({"..." if field.required else field.get_valid_argument(field.default)}, {",".join(field_arguments)})'


def add_init_py(path):
    for dirname, sub_dirs, filenames in os.walk(path):
        if "./" in dirname:
            # ignore hidden directories
            continue

        if "__init__.py" in filenames:
            continue

        open(os.path.join(dirname, "__init__.py"), "w").close()


def generate_models(output, input_text) -> None:
    """based on datamodel_code_generator.generate"""
    py37 = datamodel_code_generator.format.PythonVersion.PY_37
    target_python_version = py37

    validation = True
    base_class = "pydantic.BaseModel"
    custom_template_dir = None  # TODO seems not tot work, see https://github.com/koxudaxi/datamodel-code-generator/issues/144
    extra_template_data = None

    parser_class = K8SParser

    parser = parser_class(
        BaseModel,
        CustomRootType,
        DataModelField,
        base_class=base_class,
        custom_template_dir=custom_template_dir,
        extra_template_data=extra_template_data,
        target_python_version=target_python_version,
        text=input_text,
        dump_resolve_reference_action=dump_resolve_reference_action,
        validation=validation,
    )

    with datamodel_code_generator.chdir(output):
        result = parser.parse()

    if isinstance(result, str):
        modules = {output: result}
    else:
        if output is None:
            raise Error("Modular references require an output directory")
        if output.suffix:
            raise Error("Modular references require an output directory, not a file")
        modules = {
            output.joinpath(*name): body for name, body in sorted(result.items())
        }

    header = "# automatically generated file. DO NOT CHANGE MANUALLY"

    file: Optional[IO[Any]]
    for path, body in modules.items():
        if path is not None:
            if not path.parent.exists():
                path.parent.mkdir(parents=True)
            file = path.open("wt")
        else:
            file = None

        print(header, file=file)
        if body:
            print("", file=file)
            print(body.rstrip(), file=file)

        if file is not None:
            file.close()


def update_schema(schema: dict):
    """Adapt the kubernetes OpenAPI schema to our needs
    """
    definitions = schema["definitions"]
    for name, definition in definitions.items():
        version = None
        if "x-kubernetes-group-version-kind" in definition:
            k8s_versions = definition["x-kubernetes-group-version-kind"]
            if len(k8s_versions) != 1:
                print("warning, not correctly handling", name)

            k8s_version = k8s_versions[0]
            version = os.path.join(k8s_version["group"], k8s_version["version"])

        if "properties" in definition:
            # remove all fields named status
            # this might have some false positives, lets see what goes missing :)
            if "status" in definition["properties"]:
                definition["properties"].pop("status")

            for prop_name, prop in definition["properties"].items():
                # set the default of properties that are enums
                # with only one possible value to that value
                # This sets the `kind` property on all objects.
                if "enum" in prop and len(prop["enum"]) == 1:
                    prop.setdefault("default", prop["enum"][0])

                # set api version
                if prop_name == "apiVersion":
                    if version:
                        prop.setdefault("default", version)

                # inline IntOrString, avoids creation of IntOrString class
                # this allows assigning int or string directly, instead of this
                # ref_int_or_string = "#/definitions/io.k8s.apimachinery.pkg.util.intstr.IntOrString"
                # TODO using "oneOf" in properties is not supported by datamode-code-generator
                #      see https://github.com/koxudaxi/datamodel-code-generator/issues/139
                # if "$ref" in prop:
                #     ref = prop["$ref"]

                #     if ref == ref_int_or_string:
                #         prop.pop("$ref")

                #         prop.update(definitions[ref.split('/')[-1]])

                #         print(prop)
                # "$ref":
                #   "oneOf": [
                #     {
                #       "type": "string"
                #     },
                #     {
                #       "type": "integer"
                #     }
                #   ]


def download():
    tag = "v1.16.4"
    url = f"https://raw.githubusercontent.com/kubernetes/kubernetes/{tag}/api/openapi-spec/swagger.json"


def main():
    input_name = "k8s_1.16.4.json"
    schema = json.load(open(input_name))

    update_schema(schema)

    output = pathlib.Path(__file__).parent / pathlib.Path("gen")
    generate_models(output, json.dumps(schema))
    add_init_py(output)
    # run_mypy()


if __name__ == "__main__":
    main()
