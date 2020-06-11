# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Kind18, Kind19, Kind20, Kind21, Kind22, Kind23, Kind24, Kind25
from ...apimachinery.pkg import runtime
from ...apimachinery.pkg.apis.meta import v1
from ...apimachinery.pkg.util import intstr
from ..core import v1 as v1_1


class RollbackConfig(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    revision: Optional[int] = Field(
        None,
        description="The revision to rollback to. If set to 0, rollback to the last revision.",
    )


class RollingUpdateStatefulSetStrategy(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    partition: Optional[int] = Field(
        None,
        description="Partition indicates the ordinal at which the StatefulSet should be partitioned.",
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
    selector: Optional[Dict[str, Any]] = Field(
        None,
        description="label query over pods that should match the replicas count. More info: http://kubernetes.io/docs/user-guide/labels#label-selectors",
    )
    target_selector: Optional[str] = Field(
        None,
        alias="targetSelector",
        description="label selector for pods that should match the replicas count. This is a serializated version of both map-based and more expressive set-based selectors. This is done to avoid introspection in the clients. The string will be in the same format as the query-param syntax. If the target type only supports map-based selectors, both this field and map-based selector field are populated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors",
    )


class StatefulSetUpdateStrategy(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    rolling_update: Optional[RollingUpdateStatefulSetStrategy] = Field(
        None,
        alias="rollingUpdate",
        description="RollingUpdate is used to communicate parameters when Type is RollingUpdateStatefulSetStrategyType.",
    )
    type: Optional[str] = Field(
        None, description="Type indicates the type of the StatefulSetUpdateStrategy."
    )


class DeploymentCondition(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    last_transition_time: Optional[v1.Time] = Field(
        None,
        alias="lastTransitionTime",
        description="Last time the condition transitioned from one status to another.",
    )
    last_update_time: Optional[v1.Time] = Field(
        None,
        alias="lastUpdateTime",
        description="The last time this condition was updated.",
    )
    message: Optional[str] = Field(
        None,
        description="A human readable message indicating details about the transition.",
    )
    reason: Optional[str] = Field(
        None, description="The reason for the condition's last transition."
    )
    type: str = Field(..., description="Type of deployment condition.")


class DeploymentRollback(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    api_version: Optional[str] = Field(
        "apps/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind22] = Field(
        "DeploymentRollback",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    name: str = Field(
        ..., description="Required: This must match the Name of a deployment."
    )
    rollback_to: RollbackConfig = Field(
        ..., alias="rollbackTo", description="The config of this deployment rollback."
    )
    updated_annotations: Optional[Dict[str, Any]] = Field(
        None,
        alias="updatedAnnotations",
        description="The annotations to be updated to a deployment",
    )


class DeploymentStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    available_replicas: Optional[int] = Field(
        None,
        alias="availableReplicas",
        description="Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.",
    )
    collision_count: Optional[int] = Field(
        None,
        alias="collisionCount",
        description="Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.",
    )
    conditions: Optional[List[DeploymentCondition]] = Field(
        None,
        description="Represents the latest available observations of a deployment's current state.",
    )
    observed_generation: Optional[int] = Field(
        None,
        alias="observedGeneration",
        description="The generation observed by the deployment controller.",
    )
    ready_replicas: Optional[int] = Field(
        None,
        alias="readyReplicas",
        description="Total number of ready pods targeted by this deployment.",
    )
    replicas: Optional[int] = Field(
        None,
        description="Total number of non-terminated pods targeted by this deployment (their labels match the selector).",
    )
    unavailable_replicas: Optional[int] = Field(
        None,
        alias="unavailableReplicas",
        description="Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.",
    )
    updated_replicas: Optional[int] = Field(
        None,
        alias="updatedReplicas",
        description="Total number of non-terminated pods targeted by this deployment that have the desired template spec.",
    )


class RollingUpdateDeployment(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    max_surge: Optional[Union[int, str]] = Field(
        None,
        alias="maxSurge",
        description="The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods.",
    )
    max_unavailable: Optional[Union[int, str]] = Field(
        None,
        alias="maxUnavailable",
        description="The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods.",
    )


class StatefulSetCondition(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    last_transition_time: Optional[v1.Time] = Field(
        None,
        alias="lastTransitionTime",
        description="Last time the condition transitioned from one status to another.",
    )
    message: Optional[str] = Field(
        None,
        description="A human readable message indicating details about the transition.",
    )
    reason: Optional[str] = Field(
        None, description="The reason for the condition's last transition."
    )
    type: str = Field(..., description="Type of statefulset condition.")


class StatefulSetStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    collision_count: Optional[int] = Field(
        None,
        alias="collisionCount",
        description="collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.",
    )
    conditions: Optional[List[StatefulSetCondition]] = Field(
        None,
        description="Represents the latest available observations of a statefulset's current state.",
    )
    current_replicas: Optional[int] = Field(
        None,
        alias="currentReplicas",
        description="currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision.",
    )
    current_revision: Optional[str] = Field(
        None,
        alias="currentRevision",
        description="currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas).",
    )
    observed_generation: Optional[int] = Field(
        None,
        alias="observedGeneration",
        description="observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet's generation, which is updated on mutation by the API Server.",
    )
    ready_replicas: Optional[int] = Field(
        None,
        alias="readyReplicas",
        description="readyReplicas is the number of Pods created by the StatefulSet controller that have a Ready Condition.",
    )
    replicas: int = Field(
        ...,
        description="replicas is the number of Pods created by the StatefulSet controller.",
    )
    update_revision: Optional[str] = Field(
        None,
        alias="updateRevision",
        description="updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas)",
    )
    updated_replicas: Optional[int] = Field(
        None,
        alias="updatedReplicas",
        description="updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision.",
    )


class ControllerRevision(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "apps/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    data: Optional[runtime.RawExtension] = Field(
        None, description="Data is the serialized representation of the state."
    )
    kind: Optional[Kind18] = Field(
        "ControllerRevision",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    revision: int = Field(
        ...,
        description="Revision indicates the revision of the state represented by Data.",
    )


class ControllerRevisionList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "apps/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[ControllerRevision] = Field(
        ..., description="Items is the list of ControllerRevisions"
    )
    kind: Optional[Kind19] = Field(
        "ControllerRevisionList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )


class DeploymentStrategy(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    rolling_update: Optional[RollingUpdateDeployment] = Field(
        None,
        alias="rollingUpdate",
        description="Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.",
    )
    type: Optional[str] = Field(
        None,
        description='Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate.',
    )


class Scale(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "apps/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind23] = Field(
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


class DeploymentSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    min_ready_seconds: Optional[int] = Field(
        None,
        alias="minReadySeconds",
        description="Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)",
    )
    paused: Optional[bool] = Field(
        None, description="Indicates that the deployment is paused."
    )
    progress_deadline_seconds: Optional[int] = Field(
        None,
        alias="progressDeadlineSeconds",
        description="The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s.",
    )
    replicas: Optional[int] = Field(
        None,
        description="Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.",
    )
    revision_history_limit: Optional[int] = Field(
        None,
        alias="revisionHistoryLimit",
        description="The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 2.",
    )
    rollback_to: Optional[RollbackConfig] = Field(
        None,
        alias="rollbackTo",
        description="DEPRECATED. The config this deployment is rolling back to. Will be cleared after rollback is done.",
    )
    selector: Optional[v1.LabelSelector] = Field(
        None,
        description="Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment.",
    )
    strategy: Optional[DeploymentStrategy] = Field(
        None,
        description="The deployment strategy to use to replace existing pods with new ones.",
    )
    template: v1_1.PodTemplateSpec = Field(
        ..., description="Template describes the pods that will be created."
    )


class StatefulSetSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    pod_management_policy: Optional[str] = Field(
        None,
        alias="podManagementPolicy",
        description="podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once.",
    )
    replicas: Optional[int] = Field(
        None,
        description="replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1.",
    )
    revision_history_limit: Optional[int] = Field(
        None,
        alias="revisionHistoryLimit",
        description="revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet's revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10.",
    )
    selector: Optional[v1.LabelSelector] = Field(
        None,
        description="selector is a label query over pods that should match the replica count. If empty, defaulted to labels on the pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors",
    )
    service_name: str = Field(
        ...,
        alias="serviceName",
        description='serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where "pod-specific-string" is managed by the StatefulSet controller.',
    )
    template: v1_1.PodTemplateSpec = Field(
        ...,
        description="template is the object that describes the pod that will be created if insufficient replicas are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have a unique identity from the rest of the StatefulSet.",
    )
    update_strategy: Optional[StatefulSetUpdateStrategy] = Field(
        None,
        alias="updateStrategy",
        description="updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template.",
    )
    volume_claim_templates: Optional[List[v1_1.PersistentVolumeClaim]] = Field(
        None,
        alias="volumeClaimTemplates",
        description="volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name.",
    )


class Deployment(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "apps/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind20] = Field(
        "Deployment",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None, description="Standard object metadata."
    )
    spec: Optional[DeploymentSpec] = Field(
        None, description="Specification of the desired behavior of the Deployment."
    )


class DeploymentList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "apps/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[Deployment] = Field(
        ..., description="Items is the list of Deployments."
    )
    kind: Optional[Kind21] = Field(
        "DeploymentList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(None, description="Standard list metadata.")


class StatefulSet(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "apps/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind24] = Field(
        "StatefulSet",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: Optional[StatefulSetSpec] = Field(
        None, description="Spec defines the desired identities of pods in this set."
    )


class StatefulSetList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "apps/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[StatefulSet]
    kind: Optional[Kind25] = Field(
        "StatefulSetList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = None
