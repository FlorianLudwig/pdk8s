# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Kind50, Kind51, Kind52
from ...apimachinery.pkg.apis.meta import v1


class CrossVersionObjectReference(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    api_version: Optional[str] = Field(
        None, alias="apiVersion", description="API version of the referent"
    )
    kind: str = Field(
        ...,
        description='Kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"',
    )
    name: str = Field(
        ...,
        description="Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names",
    )


class HorizontalPodAutoscalerSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    max_replicas: int = Field(
        ...,
        alias="maxReplicas",
        description="upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.",
    )
    min_replicas: Optional[int] = Field(
        None,
        alias="minReplicas",
        description="minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available.",
    )
    scale_target_ref: CrossVersionObjectReference = Field(
        ...,
        alias="scaleTargetRef",
        description="reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource.",
    )
    target_cpu_utilization_percentage: Optional[int] = Field(
        None,
        alias="targetCPUUtilizationPercentage",
        description="target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used.",
    )


class ScaleSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    replicas: Optional[int] = Field(
        None, description="desired number of instances for the scaled object."
    )


class ScaleStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    replicas: int = Field(
        ..., description="actual number of observed instances of the scaled object."
    )
    selector: Optional[str] = Field(
        None,
        description="label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by clients. The string will be in the same format as the query-param syntax. More info about label selectors: http://kubernetes.io/docs/user-guide/labels#label-selectors",
    )


class HorizontalPodAutoscalerStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    current_cpu_utilization_percentage: Optional[int] = Field(
        None,
        alias="currentCPUUtilizationPercentage",
        description="current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU.",
    )
    current_replicas: int = Field(
        ...,
        alias="currentReplicas",
        description="current number of replicas of pods managed by this autoscaler.",
    )
    desired_replicas: int = Field(
        ...,
        alias="desiredReplicas",
        description="desired number of replicas of pods managed by this autoscaler.",
    )
    last_scale_time: Optional[v1.Time] = Field(
        None,
        alias="lastScaleTime",
        description="last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed.",
    )
    observed_generation: Optional[int] = Field(
        None,
        alias="observedGeneration",
        description="most recent generation observed by this autoscaler.",
    )


class HorizontalPodAutoscaler(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "autoscaling/v1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind50] = Field(
        "HorizontalPodAutoscaler",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[HorizontalPodAutoscalerSpec] = Field(
        None,
        description="behaviour of autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.",
    )


class HorizontalPodAutoscalerList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "autoscaling/v1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[HorizontalPodAutoscaler] = Field(
        ..., description="list of horizontal pod autoscaler objects."
    )
    kind: Optional[Kind51] = Field(
        "HorizontalPodAutoscalerList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(None, description="Standard list metadata.")


class Scale(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "autoscaling/v1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind52] = Field(
        "Scale",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.",
    )
    spec: Optional[ScaleSpec] = Field(
        None,
        description="defines the behavior of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.",
    )
