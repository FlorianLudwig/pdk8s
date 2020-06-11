# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Kind67, Kind68
from ...apimachinery.pkg.apis.meta import v1


class LeaseSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    acquire_time: Optional[v1.MicroTime] = Field(
        None,
        alias="acquireTime",
        description="acquireTime is a time when the current lease was acquired.",
    )
    holder_identity: Optional[str] = Field(
        None,
        alias="holderIdentity",
        description="holderIdentity contains the identity of the holder of a current lease.",
    )
    lease_duration_seconds: Optional[int] = Field(
        None,
        alias="leaseDurationSeconds",
        description="leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measure against time of last observed RenewTime.",
    )
    lease_transitions: Optional[int] = Field(
        None,
        alias="leaseTransitions",
        description="leaseTransitions is the number of transitions of a lease between holders.",
    )
    renew_time: Optional[v1.MicroTime] = Field(
        None,
        alias="renewTime",
        description="renewTime is a time when the current holder of a lease has last updated the lease.",
    )


class Lease(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "coordination.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind67] = Field(
        "Lease",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[LeaseSpec] = Field(
        None,
        description="Specification of the Lease. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class LeaseList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "coordination.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[Lease] = Field(..., description="Items is a list of schema objects.")
    kind: Optional[Kind68] = Field(
        "LeaseList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
