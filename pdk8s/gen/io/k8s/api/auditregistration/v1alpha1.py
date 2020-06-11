# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Kind37, Kind38
from ...apimachinery.pkg.apis.meta import v1


class Policy(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    level: str = Field(
        ...,
        description="The Level that all requests are recorded at. available options: None, Metadata, Request, RequestResponse required",
    )
    stages: Optional[List[str]] = Field(
        None, description="Stages is a list of stages for which events are created."
    )


class ServiceReference(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    name: str = Field(..., description="`name` is the name of the service. Required")
    namespace: str = Field(
        ..., description="`namespace` is the namespace of the service. Required"
    )
    path: Optional[str] = Field(
        None,
        description="`path` is an optional URL path which will be sent in any request to this service.",
    )
    port: Optional[int] = Field(
        None,
        description="If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. `port` should be a valid port number (1-65535, inclusive).",
    )


class WebhookClientConfig(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    ca_bundle: Optional[str] = Field(
        None,
        alias="caBundle",
        description="`caBundle` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. If unspecified, system trust roots on the apiserver are used.",
    )
    service: Optional[ServiceReference] = Field(
        None,
        description="`service` is a reference to the service for this webhook. Either `service` or `url` must be specified.\n\nIf the webhook is running within the cluster, then you should use `service`.",
    )
    url: Optional[str] = Field(
        None,
        description='`url` gives the location of the webhook, in standard URL form (`scheme://host:port/path`). Exactly one of `url` or `service` must be specified.\n\nThe `host` should not refer to a service running in the cluster; use the `service` field instead. The host might be resolved via external DNS in some apiservers (e.g., `kube-apiserver` cannot resolve in-cluster DNS as that would be a layering violation). `host` may also be an IP address.\n\nPlease note that using `localhost` or `127.0.0.1` as a `host` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.\n\nThe scheme must be "https"; the URL must begin with "https://".\n\nA path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.\n\nAttempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#...") and query parameters ("?...") are not allowed, either.',
    )


class WebhookThrottleConfig(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    burst: Optional[int] = Field(
        None,
        description="ThrottleBurst is the maximum number of events sent at the same moment default 15 QPS",
    )
    qps: Optional[int] = Field(
        None,
        description="ThrottleQPS maximum number of batches per second default 10 QPS",
    )


class Webhook(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    client_config: WebhookClientConfig = Field(
        ...,
        alias="clientConfig",
        description="ClientConfig holds the connection parameters for the webhook required",
    )
    throttle: Optional[WebhookThrottleConfig] = Field(
        None, description="Throttle holds the options for throttling the webhook"
    )


class AuditSinkSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    policy: Policy = Field(
        ...,
        description="Policy defines the policy for selecting which events should be sent to the webhook required",
    )
    webhook: Webhook = Field(..., description="Webhook to send events required")


class AuditSink(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "auditregistration.k8s.io/v1alpha1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind37] = Field(
        "AuditSink",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: Optional[AuditSinkSpec] = Field(
        None, description="Spec defines the audit configuration spec"
    )


class AuditSinkList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "auditregistration.k8s.io/v1alpha1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[AuditSink] = Field(..., description="List of audit configurations.")
    kind: Optional[Kind38] = Field(
        "AuditSinkList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = None
