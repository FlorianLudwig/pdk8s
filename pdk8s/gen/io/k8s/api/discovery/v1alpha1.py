# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Kind102, Kind103
from ...apimachinery.pkg.apis.meta import v1
from ..core import v1


class EndpointConditions(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    ready: Optional[bool] = Field(
        None,
        description="ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready.",
    )


class EndpointPort(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    name: Optional[str] = Field(
        None,
        description="The name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is dervied from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass IANA_SVC_NAME validation: * must be no more than 15 characters long * may contain only [-a-z0-9] * must contain at least one letter [a-z] * it must not start or end with a hyphen, nor contain adjacent hyphens Default is empty string.",
    )
    port: Optional[int] = Field(
        None,
        description="The port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer.",
    )
    protocol: Optional[str] = Field(
        None,
        description="The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.",
    )


class Endpoint(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    addresses: List[str] = Field(
        ...,
        description="addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. This allows for cases like dual-stack (IPv4 and IPv6) networking. Consumers (e.g. kube-proxy) must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100.",
    )
    conditions: Optional[EndpointConditions] = Field(
        None,
        description="conditions contains information about the current status of the endpoint.",
    )
    hostname: Optional[str] = Field(
        None,
        description="hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must pass DNS Label (RFC 1123) validation.",
    )
    target_ref: Optional[v1.ObjectReference] = Field(
        None,
        alias="targetRef",
        description="targetRef is a reference to a Kubernetes object that represents this endpoint.",
    )
    topology: Optional[Dict[str, Any]] = Field(
        None,
        description="topology contains arbitrary topology information associated with the endpoint. These key/value pairs must conform with the label format. https://kubernetes.io/docs/concepts/overview/working-with-objects/labels Topology may include a maximum of 16 key/value pairs. This includes, but is not limited to the following well known keys: * kubernetes.io/hostname: the value indicates the hostname of the node\n  where the endpoint is located. This should match the corresponding\n  node label.\n* topology.kubernetes.io/zone: the value indicates the zone where the\n  endpoint is located. This should match the corresponding node label.\n* topology.kubernetes.io/region: the value indicates the region where the\n  endpoint is located. This should match the corresponding node label.",
    )


class EndpointSlice(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    address_type: Optional[str] = Field(
        None,
        alias="addressType",
        description="addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. Default is IP",
    )
    api_version: Optional[str] = Field(
        "discovery.k8s.io/v1alpha1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    endpoints: List[Endpoint] = Field(
        ...,
        description="endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints.",
    )
    kind: Optional[Kind102] = Field(
        "EndpointSlice",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None, description="Standard object's metadata."
    )
    ports: Optional[List[EndpointPort]] = Field(
        None,
        description='ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates "all ports". Each slice may include a maximum of 100 ports.',
    )


class EndpointSliceList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "discovery.k8s.io/v1alpha1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[EndpointSlice] = Field(..., description="List of endpoint slices")
    kind: Optional[Kind103] = Field(
        "EndpointSliceList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(None, description="Standard list metadata.")
