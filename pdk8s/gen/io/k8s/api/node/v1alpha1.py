# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Kind124, Kind125
from ...apimachinery.pkg.apis.meta import v1
from ..core import v1


class Overhead(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    pod_fixed: Optional[Dict[str, Any]] = Field(
        None,
        alias="podFixed",
        description="PodFixed represents the fixed resource overhead associated with running a pod.",
    )


class Scheduling(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    node_selector: Optional[Dict[str, Any]] = Field(
        None,
        alias="nodeSelector",
        description="nodeSelector lists labels that must be present on nodes that support this RuntimeClass. Pods using this RuntimeClass can only be scheduled to a node matched by this selector. The RuntimeClass nodeSelector is merged with a pod's existing nodeSelector. Any conflicts will cause the pod to be rejected in admission.",
    )
    tolerations: Optional[List[v1.Toleration]] = Field(
        None,
        description="tolerations are appended (excluding duplicates) to pods running with this RuntimeClass during admission, effectively unioning the set of nodes tolerated by the pod and the RuntimeClass.",
    )


class RuntimeClassSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    overhead: Optional[Overhead] = Field(
        None,
        description="Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. For more details, see https://git.k8s.io/enhancements/keps/sig-node/20190226-pod-overhead.md This field is alpha-level as of Kubernetes v1.15, and is only honored by servers that enable the PodOverhead feature.",
    )
    runtime_handler: str = Field(
        ...,
        alias="runtimeHandler",
        description='RuntimeHandler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called "runc" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The RuntimeHandler must conform to the DNS Label (RFC 1123) requirements and is immutable.',
    )
    scheduling: Optional[Scheduling] = Field(
        None,
        description="Scheduling holds the scheduling constraints to ensure that pods running with this RuntimeClass are scheduled to nodes that support it. If scheduling is nil, this RuntimeClass is assumed to be supported by all nodes.",
    )


class RuntimeClass(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "node.k8s.io/v1alpha1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind124] = Field(
        "RuntimeClass",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: RuntimeClassSpec = Field(
        ...,
        description="Specification of the RuntimeClass More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class RuntimeClassList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "node.k8s.io/v1alpha1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[RuntimeClass] = Field(
        ..., description="Items is a list of schema objects."
    )
    kind: Optional[Kind125] = Field(
        "RuntimeClassList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
