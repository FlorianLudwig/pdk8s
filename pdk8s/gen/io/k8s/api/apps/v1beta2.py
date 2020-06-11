# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import (
    Kind26,
    Kind27,
    Kind28,
    Kind29,
    Kind30,
    Kind31,
    Kind32,
    Kind33,
    Kind34,
    Kind35,
    Kind36,
)
from ...apimachinery.pkg import runtime
from ...apimachinery.pkg.apis.meta import v1
from ...apimachinery.pkg.util import intstr
from ..core import v1 as v1_1


class RollingUpdateStatefulSetStrategy(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    partition: Optional[int] = Field(
        None,
        description="Partition indicates the ordinal at which the StatefulSet should be partitioned. Default value is 0.",
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
        None,
        description="Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate.",
    )


class DaemonSetCondition(BaseModel):
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
    type: str = Field(..., description="Type of DaemonSet condition.")


class DaemonSetStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    collision_count: Optional[int] = Field(
        None,
        alias="collisionCount",
        description="Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.",
    )
    conditions: Optional[List[DaemonSetCondition]] = Field(
        None,
        description="Represents the latest available observations of a DaemonSet's current state.",
    )
    current_number_scheduled: int = Field(
        ...,
        alias="currentNumberScheduled",
        description="The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/",
    )
    desired_number_scheduled: int = Field(
        ...,
        alias="desiredNumberScheduled",
        description="The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/",
    )
    number_available: Optional[int] = Field(
        None,
        alias="numberAvailable",
        description="The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds)",
    )
    number_misscheduled: int = Field(
        ...,
        alias="numberMisscheduled",
        description="The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/",
    )
    number_ready: int = Field(
        ...,
        alias="numberReady",
        description="The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and ready.",
    )
    number_unavailable: Optional[int] = Field(
        None,
        alias="numberUnavailable",
        description="The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds)",
    )
    observed_generation: Optional[int] = Field(
        None,
        alias="observedGeneration",
        description="The most recent generation observed by the daemon set controller.",
    )
    updated_number_scheduled: Optional[int] = Field(
        None,
        alias="updatedNumberScheduled",
        description="The total number of nodes that are running updated daemon pod",
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


class ReplicaSetCondition(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    last_transition_time: Optional[v1.Time] = Field(
        None,
        alias="lastTransitionTime",
        description="The last time the condition transitioned from one status to another.",
    )
    message: Optional[str] = Field(
        None,
        description="A human readable message indicating details about the transition.",
    )
    reason: Optional[str] = Field(
        None, description="The reason for the condition's last transition."
    )
    type: str = Field(..., description="Type of replica set condition.")


class ReplicaSetStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    available_replicas: Optional[int] = Field(
        None,
        alias="availableReplicas",
        description="The number of available replicas (ready for at least minReadySeconds) for this replica set.",
    )
    conditions: Optional[List[ReplicaSetCondition]] = Field(
        None,
        description="Represents the latest available observations of a replica set's current state.",
    )
    fully_labeled_replicas: Optional[int] = Field(
        None,
        alias="fullyLabeledReplicas",
        description="The number of pods that have labels matching the labels of the pod template of the replicaset.",
    )
    observed_generation: Optional[int] = Field(
        None,
        alias="observedGeneration",
        description="ObservedGeneration reflects the generation of the most recently observed ReplicaSet.",
    )
    ready_replicas: Optional[int] = Field(
        None,
        alias="readyReplicas",
        description="The number of ready replicas for this replica set.",
    )
    replicas: int = Field(
        ...,
        description="Replicas is the most recently oberved number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller",
    )


class RollingUpdateDaemonSet(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    max_unavailable: Optional[Union[int, str]] = Field(
        None,
        alias="maxUnavailable",
        description="The maximum number of DaemonSet pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of total number of DaemonSet pods at the start of the update (ex: 10%). Absolute number is calculated from percentage by rounding up. This cannot be 0. Default value is 1. Example: when this is set to 30%, at most 30% of the total number of nodes that should be running the daemon pod (i.e. status.desiredNumberScheduled) can have their pods stopped for an update at any given time. The update starts by stopping at most 30% of those DaemonSet pods and then brings up new DaemonSet pods in their place. Once the new pods are available, it then proceeds onto other DaemonSet pods, thus ensuring that at least 70% of original number of DaemonSet pods are available at all times during the update.",
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
        "apps/v1beta2",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    data: Optional[runtime.RawExtension] = Field(
        None, description="Data is the serialized representation of the state."
    )
    kind: Optional[Kind26] = Field(
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
        "apps/v1beta2",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[ControllerRevision] = Field(
        ..., description="Items is the list of ControllerRevisions"
    )
    kind: Optional[Kind27] = Field(
        "ControllerRevisionList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )


class DaemonSetUpdateStrategy(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    rolling_update: Optional[RollingUpdateDaemonSet] = Field(
        None,
        alias="rollingUpdate",
        description='Rolling update config params. Present only if type = "RollingUpdate".',
    )
    type: Optional[str] = Field(
        None,
        description='Type of daemon set update. Can be "RollingUpdate" or "OnDelete". Default is RollingUpdate.',
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
        "apps/v1beta2",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind34] = Field(
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


class DaemonSetSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    min_ready_seconds: Optional[int] = Field(
        None,
        alias="minReadySeconds",
        description="The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready).",
    )
    revision_history_limit: Optional[int] = Field(
        None,
        alias="revisionHistoryLimit",
        description="The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.",
    )
    selector: v1.LabelSelector = Field(
        ...,
        description="A label query over pods that are managed by the daemon set. Must match in order to be controlled. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors",
    )
    template: v1_1.PodTemplateSpec = Field(
        ...,
        description="An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template",
    )
    update_strategy: Optional[DaemonSetUpdateStrategy] = Field(
        None,
        alias="updateStrategy",
        description="An update strategy to replace existing DaemonSet pods with new pods.",
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
        description="The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.",
    )
    selector: v1.LabelSelector = Field(
        ...,
        description="Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template's labels.",
    )
    strategy: Optional[DeploymentStrategy] = Field(
        None,
        description="The deployment strategy to use to replace existing pods with new ones.",
    )
    template: v1_1.PodTemplateSpec = Field(
        ..., description="Template describes the pods that will be created."
    )


class ReplicaSetSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    min_ready_seconds: Optional[int] = Field(
        None,
        alias="minReadySeconds",
        description="Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)",
    )
    replicas: Optional[int] = Field(
        None,
        description="Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller",
    )
    selector: v1.LabelSelector = Field(
        ...,
        description="Selector is a label query over pods that should match the replica count. Label keys and values that must match in order to be controlled by this replica set. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors",
    )
    template: Optional[v1_1.PodTemplateSpec] = Field(
        None,
        description="Template is the object that describes the pod that will be created if insufficient replicas are detected. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template",
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
    selector: v1.LabelSelector = Field(
        ...,
        description="selector is a label query over pods that should match the replica count. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors",
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


class DaemonSet(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "apps/v1beta2",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind28] = Field(
        "DaemonSet",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[DaemonSetSpec] = Field(
        None,
        description="The desired behavior of this daemon set. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class DaemonSetList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "apps/v1beta2",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[DaemonSet] = Field(..., description="A list of daemon sets.")
    kind: Optional[Kind29] = Field(
        "DaemonSetList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )


class Deployment(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "apps/v1beta2",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind30] = Field(
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
        "apps/v1beta2",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[Deployment] = Field(
        ..., description="Items is the list of Deployments."
    )
    kind: Optional[Kind31] = Field(
        "DeploymentList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(None, description="Standard list metadata.")


class ReplicaSet(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "apps/v1beta2",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind32] = Field(
        "ReplicaSet",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="If the Labels of a ReplicaSet are empty, they are defaulted to be the same as the Pod(s) that the ReplicaSet manages. Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[ReplicaSetSpec] = Field(
        None,
        description="Spec defines the specification of the desired behavior of the ReplicaSet. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class ReplicaSetList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "apps/v1beta2",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[ReplicaSet] = Field(
        ...,
        description="List of ReplicaSets. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller",
    )
    kind: Optional[Kind33] = Field(
        "ReplicaSetList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )


class StatefulSet(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "apps/v1beta2",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind35] = Field(
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
        "apps/v1beta2",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[StatefulSet]
    kind: Optional[Kind36] = Field(
        "StatefulSetList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = None
