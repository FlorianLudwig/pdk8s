# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Extra, Kind39, Kind40
from ...apimachinery.pkg.apis.meta import v1


class BoundObjectReference(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    api_version: Optional[str] = Field(
        None, alias="apiVersion", description="API version of the referent."
    )
    kind: Optional[str] = Field(
        None, description="Kind of the referent. Valid kinds are 'Pod' and 'Secret'."
    )
    name: Optional[str] = Field(None, description="Name of the referent.")
    uid: Optional[str] = Field(None, description="UID of the referent.")


class TokenRequestSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    audiences: List[str] = Field(
        ...,
        description="Audiences are the intendend audiences of the token. A recipient of a token must identitfy themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences.",
    )
    bound_object_ref: Optional[BoundObjectReference] = Field(
        None,
        alias="boundObjectRef",
        description="BoundObjectRef is a reference to an object that the token will be bound to. The token will only be valid for as long as the bound object exists. NOTE: The API server's TokenReview endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds small if you want prompt revocation.",
    )
    expiration_seconds: Optional[int] = Field(
        None,
        alias="expirationSeconds",
        description="ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response.",
    )


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

    extra: Optional[Dict[str, Extra]] = Field(
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


class TokenRequestStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    expiration_timestamp: v1.Time = Field(
        ...,
        alias="expirationTimestamp",
        description="ExpirationTimestamp is the time of expiration of the returned token.",
    )
    token: str = Field(..., description="Token is the opaque bearer token.")


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


class TokenRequest(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "authentication.k8s.io/v1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind39] = Field(
        "TokenRequest",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: TokenRequestSpec


class TokenReview(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "authentication.k8s.io/v1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind40] = Field(
        "TokenReview",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: TokenReviewSpec = Field(
        ..., description="Spec holds information about the request being evaluated"
    )
