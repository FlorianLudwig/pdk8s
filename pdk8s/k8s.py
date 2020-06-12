import yaml
import pydantic

# TODO: generate imports
from .gen.io.k8s.api.extensions.v1beta1 import *  # pylint: disable=unused-wildcard-import
from .gen.io.k8s.api.apps.v1 import *  # pylint: disable=unused-wildcard-import
from .gen.io.k8s.api.core.v1 import *  # pylint: disable=unused-wildcard-import
from .gen.io.k8s.apimachinery.pkg.apis.meta.v1 import *  # pylint: disable=unused-wildcard-import

API_VERSION = "1.16.4"


class Chart(list):
    pass


def _parse_object(obj):
    kind = obj["kind"]
    del obj["kind"]  # TODO

    cls = globals()[kind]

    if not issubclass(cls, pydantic.BaseModel):
        raise AttributeError(f"unknown kind {kind}")

    return cls(**obj)


def parse(name):
    docs = yaml.safe_load_all(open(name))
    return [_parse_object(doc) for doc in docs]
