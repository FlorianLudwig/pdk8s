# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Kind122, Kind123
from ...apimachinery.pkg.apis.meta import v1
from ...apimachinery.pkg.util import intstr
from ..core import v1


class IngressStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    load_balancer: Optional[v1_1.LoadBalancerStatus] = Field(
        None,
        alias="loadBalancer",
        description="LoadBalancer contains the current status of the load-balancer.",
    )


class IngressTLS(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    hosts: Optional[List[str]] = Field(
        None,
        description="Hosts are a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified.",
    )
    secret_name: Optional[str] = Field(
        None,
        alias="secretName",
        description='SecretName is the name of the secret used to terminate SSL traffic on 443. Field is left optional to allow SSL routing based on SNI hostname alone. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing.',
    )


class IngressBackend(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    service_name: str = Field(
        ...,
        alias="serviceName",
        description="Specifies the name of the referenced service.",
    )
    service_port: Union[int, str] = Field(
        ...,
        alias="servicePort",
        description="Specifies the port of the referenced service.",
    )


class HTTPIngressPath(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    backend: IngressBackend = Field(
        ...,
        description="Backend defines the referenced service endpoint to which the traffic will be forwarded to.",
    )
    path: Optional[str] = Field(
        None,
        description="Path is an extended POSIX regex as defined by IEEE Std 1003.1, (i.e this follows the egrep/unix syntax, not the perl syntax) matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional \"path\" part of a URL as defined by RFC 3986. Paths must begin with a '/'. If unspecified, the path defaults to a catch all sending traffic to the backend.",
    )


class HTTPIngressRuleValue(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    paths: List[HTTPIngressPath] = Field(
        ..., description="A collection of paths that map requests to backends."
    )


class IngressRule(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    host: Optional[str] = Field(
        None,
        description='Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the "host" part of the URI as defined in the RFC: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to the\n\t  IP in the Spec of the parent Ingress.\n2. The `:` delimiter is not respected because ports are not allowed.\n\t  Currently the port of an Ingress is implicitly :80 for http and\n\t  :443 for https.\nBoth these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.',
    )
    http: Optional[HTTPIngressRuleValue] = None


class IngressSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    backend: Optional[IngressBackend] = Field(
        None,
        description="A default backend capable of servicing requests that don't match any rule. At least one of 'backend' or 'rules' must be specified. This field is optional to allow the loadbalancer controller or defaulting logic to specify a global default.",
    )
    rules: Optional[List[IngressRule]] = Field(
        None,
        description="A list of host rules used to configure the Ingress. If unspecified, or no rule matches, all traffic is sent to the default backend.",
    )
    tls: Optional[List[IngressTLS]] = Field(
        None,
        description="TLS configuration. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI.",
    )


class Ingress(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "networking.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind122] = Field(
        "Ingress",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[IngressSpec] = Field(
        None,
        description="Spec is the desired state of the Ingress. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class IngressList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "networking.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[Ingress] = Field(..., description="Items is the list of Ingress.")
    kind: Optional[Kind123] = Field(
        "IngressList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
