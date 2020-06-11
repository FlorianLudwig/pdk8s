# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Kind163, Kind164
from ...apimachinery.pkg.apis.meta import v1 as v1_1
from ..core import v1


class PodPresetSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    env: Optional[List[v1.EnvVar]] = Field(
        None,
        description="Env defines the collection of EnvVar to inject into containers.",
    )
    env_from: Optional[List[v1.EnvFromSource]] = Field(
        None,
        alias="envFrom",
        description="EnvFrom defines the collection of EnvFromSource to inject into containers.",
    )
    selector: Optional[v1_1.LabelSelector] = Field(
        None,
        description="Selector is a label query over a set of resources, in this case pods. Required.",
    )
    volume_mounts: Optional[List[v1.VolumeMount]] = Field(
        None,
        alias="volumeMounts",
        description="VolumeMounts defines the collection of VolumeMount to inject into containers.",
    )
    volumes: Optional[List[v1.Volume]] = Field(
        None,
        description="Volumes defines the collection of Volume to inject into the pod.",
    )


class PodPreset(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "settings.k8s.io/v1alpha1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind163] = Field(
        "PodPreset",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: Optional[PodPresetSpec] = None


class PodPresetList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "settings.k8s.io/v1alpha1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[PodPreset] = Field(
        ..., description="Items is a list of schema objects."
    )
    kind: Optional[Kind164] = Field(
        "PodPresetList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
