# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Kind159, Kind160
from ...apimachinery.pkg.apis.meta import v1


class PriorityClass(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "scheduling.k8s.io/v1alpha1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    description: Optional[str] = Field(
        None,
        description="description is an arbitrary string that usually provides guidelines on when this priority class should be used.",
    )
    global_default: Optional[bool] = Field(
        None,
        alias="globalDefault",
        description="globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority.",
    )
    kind: Optional[Kind159] = Field(
        "PriorityClass",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    preemption_policy: Optional[str] = Field(
        None,
        alias="preemptionPolicy",
        description="PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. This field is alpha-level and is only honored by servers that enable the NonPreemptingPriority feature.",
    )
    value: int = Field(
        ...,
        description="The value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec.",
    )


class PriorityClassList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "scheduling.k8s.io/v1alpha1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[PriorityClass] = Field(
        ..., description="items is the list of PriorityClasses"
    )
    kind: Optional[Kind160] = Field(
        "PriorityClassList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
