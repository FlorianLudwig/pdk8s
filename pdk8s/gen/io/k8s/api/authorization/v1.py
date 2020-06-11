# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Kind42, Kind43, Kind44, Kind45
from ...apimachinery.pkg.apis.meta import v1


class NonResourceAttributes(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    path: Optional[str] = Field(None, description="Path is the URL path of the request")
    verb: Optional[str] = Field(None, description="Verb is the standard HTTP verb")


class NonResourceRule(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    non_resource_ur_ls: Optional[List[str]] = Field(
        None,
        alias="nonResourceURLs",
        description='NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path.  "*" means all.',
    )
    verbs: List[str] = Field(
        ...,
        description='Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options.  "*" means all.',
    )


class ResourceAttributes(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    group: Optional[str] = Field(
        None, description='Group is the API Group of the Resource.  "*" means all.'
    )
    name: Optional[str] = Field(
        None,
        description='Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all.',
    )
    namespace: Optional[str] = Field(
        None,
        description='Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview',
    )
    resource: Optional[str] = Field(
        None,
        description='Resource is one of the existing resource types.  "*" means all.',
    )
    subresource: Optional[str] = Field(
        None,
        description='Subresource is one of the existing resource types.  "" means none.',
    )
    verb: Optional[str] = Field(
        None,
        description='Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  "*" means all.',
    )
    version: Optional[str] = Field(
        None, description='Version is the API Version of the Resource.  "*" means all.'
    )


class ResourceRule(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    api_groups: Optional[List[str]] = Field(
        None,
        alias="apiGroups",
        description='APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.  "*" means all.',
    )
    resource_names: Optional[List[str]] = Field(
        None,
        alias="resourceNames",
        description='ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.  "*" means all.',
    )
    resources: Optional[List[str]] = Field(
        None,
        description='Resources is a list of resources this rule applies to.  "*" means all in the specified apiGroups.\n "*/foo" represents the subresource \'foo\' for all resources in the specified apiGroups.',
    )
    verbs: List[str] = Field(
        ...,
        description='Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy.  "*" means all.',
    )


class SelfSubjectAccessReviewSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    non_resource_attributes: Optional[NonResourceAttributes] = Field(
        None,
        alias="nonResourceAttributes",
        description="NonResourceAttributes describes information for a non-resource access request",
    )
    resource_attributes: Optional[ResourceAttributes] = Field(
        None,
        alias="resourceAttributes",
        description="ResourceAuthorizationAttributes describes information for a resource access request",
    )


class SelfSubjectRulesReviewSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    namespace: Optional[str] = Field(
        None, description="Namespace to evaluate rules for. Required."
    )


class SubjectAccessReviewSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    extra: Optional[Dict[str, Any]] = Field(
        None,
        description="Extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is input to the authorizer it needs a reflection here.",
    )
    groups: Optional[List[str]] = Field(
        None, description="Groups is the groups you're testing for."
    )
    non_resource_attributes: Optional[NonResourceAttributes] = Field(
        None,
        alias="nonResourceAttributes",
        description="NonResourceAttributes describes information for a non-resource access request",
    )
    resource_attributes: Optional[ResourceAttributes] = Field(
        None,
        alias="resourceAttributes",
        description="ResourceAuthorizationAttributes describes information for a resource access request",
    )
    uid: Optional[str] = Field(
        None, description="UID information about the requesting user."
    )
    user: Optional[str] = Field(
        None,
        description='User is the user you\'re testing for. If you specify "User" but not "Groups", then is it interpreted as "What if User were not a member of any groups',
    )


class SubjectAccessReviewStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    allowed: bool = Field(
        ...,
        description="Allowed is required. True if the action would be allowed, false otherwise.",
    )
    denied: Optional[bool] = Field(
        None,
        description="Denied is optional. True if the action would be denied, otherwise false. If both allowed is false and denied is false, then the authorizer has no opinion on whether to authorize the action. Denied may not be true if Allowed is true.",
    )
    evaluation_error: Optional[str] = Field(
        None,
        alias="evaluationError",
        description="EvaluationError is an indication that some error occurred during the authorization check. It is entirely possible to get an error and be able to continue determine authorization status in spite of it. For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request.",
    )
    reason: Optional[str] = Field(
        None,
        description="Reason is optional.  It indicates why a request was allowed or denied.",
    )


class SubjectRulesReviewStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    evaluation_error: Optional[str] = Field(
        None,
        alias="evaluationError",
        description="EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn't support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete.",
    )
    incomplete: bool = Field(
        ...,
        description="Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn't support rules evaluation.",
    )
    non_resource_rules: List[NonResourceRule] = Field(
        ...,
        alias="nonResourceRules",
        description="NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.",
    )
    resource_rules: List[ResourceRule] = Field(
        ...,
        alias="resourceRules",
        description="ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.",
    )


class LocalSubjectAccessReview(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "authorization.k8s.io/v1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind42] = Field(
        "LocalSubjectAccessReview",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: SubjectAccessReviewSpec = Field(
        ...,
        description="Spec holds information about the request being evaluated.  spec.namespace must be equal to the namespace you made the request against.  If empty, it is defaulted.",
    )


class SelfSubjectAccessReview(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "authorization.k8s.io/v1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind43] = Field(
        "SelfSubjectAccessReview",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: SelfSubjectAccessReviewSpec = Field(
        ...,
        description="Spec holds information about the request being evaluated.  user and groups must be empty",
    )


class SelfSubjectRulesReview(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "authorization.k8s.io/v1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind44] = Field(
        "SelfSubjectRulesReview",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: SelfSubjectRulesReviewSpec = Field(
        ..., description="Spec holds information about the request being evaluated."
    )


class SubjectAccessReview(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "authorization.k8s.io/v1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind45] = Field(
        "SubjectAccessReview",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: SubjectAccessReviewSpec = Field(
        ..., description="Spec holds information about the request being evaluated"
    )
