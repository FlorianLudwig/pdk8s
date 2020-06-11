# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Kind41
from ...apimachinery.pkg.apis.meta import v1


class TokenReviewSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    audiences: Optional[List[str]] = Field(
        None,
        description="Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver.",
    )
    token: Optional[str] = Field(None, description="Token is the opaque bearer token.")


class UserInfo(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    extra: Optional[Dict[str, Any]] = Field(
        None, description="Any additional information provided by the authenticator."
    )
    groups: Optional[List[str]] = Field(
        None, description="The names of groups this user is a part of."
    )
    uid: Optional[str] = Field(
        None,
        description="A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs.",
    )
    username: Optional[str] = Field(
        None,
        description="The name that uniquely identifies this user among all active users.",
    )


class TokenReviewStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    audiences: Optional[List[str]] = Field(
        None,
        description='Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token\'s audiences. A client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is "true", the token is valid against the audience of the Kubernetes API server.',
    )
    authenticated: Optional[bool] = Field(
        None,
        description="Authenticated indicates that the token was associated with a known user.",
    )
    error: Optional[str] = Field(
        None, description="Error indicates that the token couldn't be checked"
    )
    user: Optional[UserInfo] = Field(
        None, description="User is the UserInfo associated with the provided token."
    )


class TokenReview(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "authentication.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind41] = Field(
        "TokenReview",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: TokenReviewSpec = Field(
        ..., description="Spec holds information about the request being evaluated"
    )
