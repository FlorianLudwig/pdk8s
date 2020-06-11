# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

import pdk8s.model

from ....... import Kind181, Kind182
from .....apimachinery.pkg.apis.meta import v1


class CustomResourceColumnDefinition(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    json_path: str = Field(
        ...,
        alias="JSONPath",
        description="JSONPath is a simple JSON path (i.e. with array notation) which is evaluated against each custom resource to produce the value for this column.",
    )
    description: Optional[str] = Field(
        None, description="description is a human readable description of this column."
    )
    format: Optional[str] = Field(
        None,
        description="format is an optional OpenAPI type definition for this column. The 'name' format is applied to the primary identifier column to assist in clients identifying column is the resource name. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details.",
    )
    name: str = Field(..., description="name is a human readable name for the column.")
    priority: Optional[int] = Field(
        None,
        description="priority is an integer defining the relative importance of this column compared to others. Lower numbers are considered higher priority. Columns that may be omitted in limited space scenarios should be given a priority greater than 0.",
    )
    type: str = Field(
        ...,
        description="type is an OpenAPI type definition for this column. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details.",
    )


class CustomResourceDefinitionNames(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    categories: Optional[List[str]] = Field(
        None,
        description="categories is a list of grouped resources this custom resource belongs to (e.g. 'all'). This is published in API discovery documents, and used by clients to support invocations like `kubectl get all`.",
    )
    kind: str = Field(
        ...,
        description="kind is the serialized kind of the resource. It is normally CamelCase and singular. Custom resource instances will use this value as the `kind` attribute in API calls.",
    )
    list_kind: Optional[str] = Field(
        None,
        alias="listKind",
        description='listKind is the serialized kind of the list for this resource. Defaults to "`kind`List".',
    )
    plural: str = Field(
        ...,
        description="plural is the plural name of the resource to serve. The custom resources are served under `/apis/<group>/<version>/.../<plural>`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`). Must be all lowercase.",
    )
    short_names: Optional[List[str]] = Field(
        None,
        alias="shortNames",
        description="shortNames are short names for the resource, exposed in API discovery documents, and used by clients to support invocations like `kubectl get <shortname>`. It must be all lowercase.",
    )
    singular: Optional[str] = Field(
        None,
        description="singular is the singular name of the resource. It must be all lowercase. Defaults to lowercased `kind`.",
    )


class CustomResourceSubresourceScale(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    label_selector_path: Optional[str] = Field(
        None,
        alias="labelSelectorPath",
        description="labelSelectorPath defines the JSON path inside of a custom resource that corresponds to Scale `status.selector`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.status` or `.spec`. Must be set to work with HorizontalPodAutoscaler. The field pointed by this JSON path must be a string field (not a complex selector struct) which contains a serialized label selector in string form. More info: https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions#scale-subresource If there is no value under the given path in the custom resource, the `status.selector` value in the `/scale` subresource will default to the empty string.",
    )
    spec_replicas_path: str = Field(
        ...,
        alias="specReplicasPath",
        description="specReplicasPath defines the JSON path inside of a custom resource that corresponds to Scale `spec.replicas`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.spec`. If there is no value under the given path in the custom resource, the `/scale` subresource will return an error on GET.",
    )
    status_replicas_path: str = Field(
        ...,
        alias="statusReplicasPath",
        description="statusReplicasPath defines the JSON path inside of a custom resource that corresponds to Scale `status.replicas`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.status`. If there is no value under the given path in the custom resource, the `status.replicas` value in the `/scale` subresource will default to 0.",
    )


class CustomResourceSubresourceStatus(BaseModel):
    pass

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"


class CustomResourceSubresources(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    scale: Optional[CustomResourceSubresourceScale] = Field(
        None,
        description="scale indicates the custom resource should serve a `/scale` subresource that returns an `autoscaling/v1` Scale object.",
    )


class ExternalDocumentation(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    description: Optional[str] = None
    url: Optional[str] = None


class JSON(BaseModel):
    __root__: Any


class JSONSchemaPropsOrArray(BaseModel):
    __root__: Any


class JSONSchemaPropsOrBool(BaseModel):
    __root__: Any


class JSONSchemaPropsOrStringArray(BaseModel):
    __root__: Any


class ServiceReference(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    name: str = Field(..., description="name is the name of the service. Required")
    namespace: str = Field(
        ..., description="namespace is the namespace of the service. Required"
    )
    path: Optional[str] = Field(
        None,
        description="path is an optional URL path at which the webhook will be contacted.",
    )
    port: Optional[int] = Field(
        None,
        description="port is an optional service port at which the webhook will be contacted. `port` should be a valid port number (1-65535, inclusive). Defaults to 443 for backward compatibility.",
    )


class WebhookClientConfig(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    ca_bundle: Optional[str] = Field(
        None,
        alias="caBundle",
        description="caBundle is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. If unspecified, system trust roots on the apiserver are used.",
    )
    service: Optional[ServiceReference] = Field(
        None,
        description="service is a reference to the service for this webhook. Either service or url must be specified.\n\nIf the webhook is running within the cluster, then you should use `service`.",
    )
    url: Optional[str] = Field(
        None,
        description='url gives the location of the webhook, in standard URL form (`scheme://host:port/path`). Exactly one of `url` or `service` must be specified.\n\nThe `host` should not refer to a service running in the cluster; use the `service` field instead. The host might be resolved via external DNS in some apiservers (e.g., `kube-apiserver` cannot resolve in-cluster DNS as that would be a layering violation). `host` may also be an IP address.\n\nPlease note that using `localhost` or `127.0.0.1` as a `host` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.\n\nThe scheme must be "https"; the URL must begin with "https://".\n\nA path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.\n\nAttempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#...") and query parameters ("?...") are not allowed, either.',
    )


class CustomResourceConversion(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    conversion_review_versions: Optional[List[str]] = Field(
        None,
        alias="conversionReviewVersions",
        description='conversionReviewVersions is an ordered list of preferred `ConversionReview` versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail. Defaults to `["v1beta1"]`.',
    )
    strategy: str = Field(
        ...,
        description="strategy specifies how custom resources are converted between versions. Allowed values are: - `None`: The converter only change the apiVersion and would not touch any other field in the custom resource. - `Webhook`: API Server will call to an external webhook to do the conversion. Additional information\n  is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhookClientConfig to be set.",
    )
    webhook_client_config: Optional[WebhookClientConfig] = Field(
        None,
        alias="webhookClientConfig",
        description="webhookClientConfig is the instructions for how to call the webhook if strategy is `Webhook`. Required when `strategy` is set to `Webhook`.",
    )


class CustomResourceDefinitionCondition(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    last_transition_time: Optional[v1.Time] = Field(
        None,
        alias="lastTransitionTime",
        description="lastTransitionTime last time the condition transitioned from one status to another.",
    )
    message: Optional[str] = Field(
        None,
        description="message is a human-readable message indicating details about last transition.",
    )
    reason: Optional[str] = Field(
        None,
        description="reason is a unique, one-word, CamelCase reason for the condition's last transition.",
    )
    type: str = Field(
        ...,
        description="type is the type of the condition. Types include Established, NamesAccepted and Terminating.",
    )


class CustomResourceDefinitionStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    accepted_names: CustomResourceDefinitionNames = Field(
        ...,
        alias="acceptedNames",
        description="acceptedNames are the names that are actually being used to serve discovery. They may be different than the names in spec.",
    )
    conditions: Optional[List[CustomResourceDefinitionCondition]] = Field(
        None,
        description="conditions indicate state for particular aspects of a CustomResourceDefinition",
    )
    stored_versions: List[str] = Field(
        ...,
        alias="storedVersions",
        description="storedVersions lists all versions of CustomResources that were ever persisted. Tracking these versions allows a migration path for stored versions in etcd. The field is mutable so a migration controller can finish a migration to another version (ensuring no old objects are left in storage), and then remove the rest of the versions from this list. Versions may not be removed from `spec.versions` while they exist in this list.",
    )


class JSONSchemaProps(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    _ref: Optional[str] = Field(None, alias="$ref")
    _schema: Optional[str] = Field(None, alias="$schema")
    additional_items: Optional[JSONSchemaPropsOrBool] = Field(
        None, alias="additionalItems"
    )
    additional_properties: Optional[JSONSchemaPropsOrBool] = Field(
        None, alias="additionalProperties"
    )
    all_of: Optional[List[JSONSchemaProps]] = Field(None, alias="allOf")
    any_of: Optional[List[JSONSchemaProps]] = Field(None, alias="anyOf")
    default: Optional[JSON] = Field(
        None,
        description="default is a default value for undefined object fields. Defaulting is a beta feature under the CustomResourceDefaulting feature gate. CustomResourceDefinitions with defaults must be created using the v1 (or newer) CustomResourceDefinition API.",
    )
    definitions: Optional[Dict[str, Any]] = None
    dependencies: Optional[Dict[str, Any]] = None
    description: Optional[str] = None
    enum: Optional[List[JSON]] = None
    example: Optional[JSON] = None
    exclusive_maximum: Optional[bool] = Field(None, alias="exclusiveMaximum")
    exclusive_minimum: Optional[bool] = Field(None, alias="exclusiveMinimum")
    external_docs: Optional[ExternalDocumentation] = Field(None, alias="externalDocs")
    format: Optional[str] = None
    id: Optional[str] = None
    items: Optional[JSONSchemaPropsOrArray] = None
    max_items: Optional[int] = Field(None, alias="maxItems")
    max_length: Optional[int] = Field(None, alias="maxLength")
    max_properties: Optional[int] = Field(None, alias="maxProperties")
    maximum: Optional[float] = None
    min_items: Optional[int] = Field(None, alias="minItems")
    min_length: Optional[int] = Field(None, alias="minLength")
    min_properties: Optional[int] = Field(None, alias="minProperties")
    minimum: Optional[float] = None
    multiple_of: Optional[float] = Field(None, alias="multipleOf")
    not_: Optional[JSONSchemaProps] = Field(None, alias="not")
    nullable: Optional[bool] = None
    one_of: Optional[List[JSONSchemaProps]] = Field(None, alias="oneOf")
    pattern: Optional[str] = None
    pattern_properties: Optional[Dict[str, Any]] = Field(
        None, alias="patternProperties"
    )
    properties: Optional[Dict[str, Any]] = None
    required: Optional[List[str]] = None
    title: Optional[str] = None
    type: Optional[str] = None
    unique_items: Optional[bool] = Field(None, alias="uniqueItems")
    x_kubernetes_embedded_resource: Optional[bool] = Field(
        None,
        alias="x-kubernetes-embedded-resource",
        description="x-kubernetes-embedded-resource defines that the value is an embedded Kubernetes runtime.Object, with TypeMeta and ObjectMeta. The type must be object. It is allowed to further restrict the embedded object. kind, apiVersion and metadata are validated automatically. x-kubernetes-preserve-unknown-fields is allowed to be true, but does not have to be if the object is fully specified (up to kind, apiVersion, metadata).",
    )
    x_kubernetes_int_or_string: Optional[bool] = Field(
        None,
        alias="x-kubernetes-int-or-string",
        description="x-kubernetes-int-or-string specifies that this value is either an integer or a string. If this is true, an empty type is allowed and type as child of anyOf is permitted if following one of the following patterns:\n\n1) anyOf:\n   - type: integer\n   - type: string\n2) allOf:\n   - anyOf:\n     - type: integer\n     - type: string\n   - ... zero or more",
    )
    x_kubernetes_list_map_keys: Optional[List[str]] = Field(
        None,
        alias="x-kubernetes-list-map-keys",
        description='x-kubernetes-list-map-keys annotates an array with the x-kubernetes-list-type `map` by specifying the keys used as the index of the map.\n\nThis tag MUST only be used on lists that have the "x-kubernetes-list-type" extension set to "map". Also, the values specified for this attribute must be a scalar typed field of the child structure (no nesting is supported).',
    )
    x_kubernetes_list_type: Optional[str] = Field(
        None,
        alias="x-kubernetes-list-type",
        description="x-kubernetes-list-type annotates an array to further describe its topology. This extension must only be used on lists and may have 3 possible values:\n\n1) `atomic`: the list is treated as a single entity, like a scalar.\n     Atomic lists will be entirely replaced when updated. This extension\n     may be used on any type of list (struct, scalar, ...).\n2) `set`:\n     Sets are lists that must not have multiple items with the same value. Each\n     value must be a scalar, an object with x-kubernetes-map-type `atomic` or an\n     array with x-kubernetes-list-type `atomic`.\n3) `map`:\n     These lists are like maps in that their elements have a non-index key\n     used to identify them. Order is preserved upon merge. The map tag\n     must only be used on a list with elements of type object.\nDefaults to atomic for arrays.",
    )
    x_kubernetes_preserve_unknown_fields: Optional[bool] = Field(
        None,
        alias="x-kubernetes-preserve-unknown-fields",
        description="x-kubernetes-preserve-unknown-fields stops the API server decoding step from pruning fields which are not specified in the validation schema. This affects fields recursively, but switches back to normal pruning behaviour if nested properties or additionalProperties are specified in the schema. This can either be true or undefined. False is forbidden.",
    )


class CustomResourceValidation(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    open_apiv3_schema: Optional[JSONSchemaProps] = Field(
        None,
        alias="openAPIV3Schema",
        description="openAPIV3Schema is the OpenAPI v3 schema to use for validation and pruning.",
    )


class CustomResourceDefinitionVersion(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    additional_printer_columns: Optional[List[CustomResourceColumnDefinition]] = Field(
        None,
        alias="additionalPrinterColumns",
        description="additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. Top-level and per-version columns are mutually exclusive. Per-version columns must not all be set to identical values (top-level columns should be used instead). If no top-level or per-version columns are specified, a single column displaying the age of the custom resource is used.",
    )
    name: str = Field(
        ...,
        description="name is the version name, e.g. “v1”, “v2beta1”, etc. The custom resources are served under this version at `/apis/<group>/<version>/...` if `served` is true.",
    )
    schema: Optional[CustomResourceValidation] = Field(
        None,
        description="schema describes the schema used for validation and pruning of this version of the custom resource. Top-level and per-version schemas are mutually exclusive. Per-version schemas must not all be set to identical values (top-level validation schema should be used instead).",
    )
    served: bool = Field(
        ...,
        description="served is a flag enabling/disabling this version from being served via REST APIs",
    )
    storage: bool = Field(
        ...,
        description="storage indicates this version should be used when persisting custom resources to storage. There must be exactly one version with storage=true.",
    )
    subresources: Optional[CustomResourceSubresources] = Field(
        None,
        description="subresources specify what subresources this version of the defined custom resource have. Top-level and per-version subresources are mutually exclusive. Per-version subresources must not all be set to identical values (top-level subresources should be used instead).",
    )


class CustomResourceDefinitionSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    additional_printer_columns: Optional[List[CustomResourceColumnDefinition]] = Field(
        None,
        alias="additionalPrinterColumns",
        description="additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. If present, this field configures columns for all versions. Top-level and per-version columns are mutually exclusive. If no top-level or per-version columns are specified, a single column displaying the age of the custom resource is used.",
    )
    conversion: Optional[CustomResourceConversion] = Field(
        None, description="conversion defines conversion settings for the CRD."
    )
    group: str = Field(
        ...,
        description="group is the API group of the defined custom resource. The custom resources are served under `/apis/<group>/...`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`).",
    )
    names: CustomResourceDefinitionNames = Field(
        ...,
        description="names specify the resource and kind names for the custom resource.",
    )
    preserve_unknown_fields: Optional[bool] = Field(
        None,
        alias="preserveUnknownFields",
        description="preserveUnknownFields indicates that object fields which are not specified in the OpenAPI schema should be preserved when persisting to storage. apiVersion, kind, metadata and known fields inside metadata are always preserved. If false, schemas must be defined for all versions. Defaults to true in v1beta for backwards compatibility. Deprecated: will be required to be false in v1. Preservation of unknown fields can be specified in the validation schema using the `x-kubernetes-preserve-unknown-fields: true` extension. See https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/#pruning-versus-preserving-unknown-fields for details.",
    )
    scope: str = Field(
        ...,
        description="scope indicates whether the defined custom resource is cluster- or namespace-scoped. Allowed values are `Cluster` and `Namespaced`. Default is `Namespaced`.",
    )
    subresources: Optional[CustomResourceSubresources] = Field(
        None,
        description="subresources specify what subresources the defined custom resource has. If present, this field configures subresources for all versions. Top-level and per-version subresources are mutually exclusive.",
    )
    validation: Optional[CustomResourceValidation] = Field(
        None,
        description="validation describes the schema used for validation and pruning of the custom resource. If present, this validation schema is used to validate all versions. Top-level and per-version schemas are mutually exclusive.",
    )
    version: Optional[str] = Field(
        None,
        description="version is the API version of the defined custom resource. The custom resources are served under `/apis/<group>/<version>/...`. Must match the name of the first item in the `versions` list if `version` and `versions` are both specified. Optional if `versions` is specified. Deprecated: use `versions` instead.",
    )
    versions: Optional[List[CustomResourceDefinitionVersion]] = Field(
        None,
        description='versions is the list of all API versions of the defined custom resource. Optional if `version` is specified. The name of the first item in the `versions` list must match the `version` field if `version` and `versions` are both specified. Version names are used to compute the order in which served versions are listed in API discovery. If the version string is "kube-like", it will sort above non "kube-like" version strings, which are ordered lexicographically. "Kube-like" versions start with a "v", then are followed by a number (the major version), then optionally the string "alpha" or "beta" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.',
    )


class CustomResourceDefinition(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "apiextensions.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind181] = Field(
        "CustomResourceDefinition",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: CustomResourceDefinitionSpec = Field(
        ..., description="spec describes how the user wants the resources to appear"
    )


class CustomResourceDefinitionList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "apiextensions.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[CustomResourceDefinition] = Field(
        ..., description="items list individual CustomResourceDefinition objects"
    )
    kind: Optional[Kind182] = Field(
        "CustomResourceDefinitionList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = None


io.k8s.apiextensions_apiserver.pkg.apis.apiextensions.v1beta1.JSONSchemaProps.update_forward_refs()
