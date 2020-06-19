# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import (
    Kind106,
    Kind107,
    Kind108,
    Kind109,
    Kind110,
    Kind111,
    Kind112,
    Kind113,
    Kind114,
    Kind115,
    Kind116,
    Kind117,
    Kind118,
    Kind119,
)
from ...apimachinery.pkg.apis.meta import v1
from ...apimachinery.pkg.util import intstr
from ..core import v1 as v1_1


class AllowedCSIDriver(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    name: str = Field(..., description="Name is the registered name of the CSI driver")


class AllowedFlexVolume(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    driver: str = Field(..., description="driver is the name of the Flexvolume driver.")


class AllowedHostPath(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    path_prefix: Optional[str] = Field(
        None,
        alias="pathPrefix",
        description="pathPrefix is the path prefix that the host volume must match. It does not support `*`. Trailing slashes are trimmed when validating the path prefix with a host path.\n\nExamples: `/foo` would allow `/foo`, `/foo/` and `/foo/bar` `/foo` would not allow `/food` or `/etc/foo`",
    )
    read_only: Optional[bool] = Field(
        None,
        alias="readOnly",
        description="when set to true, will allow host volumes matching the pathPrefix only if all volume mounts are readOnly.",
    )


class HostPortRange(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    max: int = Field(..., description="max is the end of the range, inclusive.")
    min: int = Field(..., description="min is the start of the range, inclusive.")


class IDRange(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    max: int = Field(..., description="max is the end of the range, inclusive.")
    min: int = Field(..., description="min is the start of the range, inclusive.")


class IPBlock(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    cidr: str = Field(
        ...,
        description='CIDR is a string representing the IP Block Valid examples are "192.168.1.1/24"',
    )
    except_: Optional[List[str]] = Field(
        None,
        alias="except",
        description='Except is a slice of CIDRs that should not be included within an IP Block Valid examples are "192.168.1.1/24" Except values will be rejected if they are outside the CIDR range',
    )


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


class RollbackConfig(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    revision: Optional[int] = Field(
        None,
        description="The revision to rollback to. If set to 0, rollback to the last revision.",
    )


class RunAsGroupStrategyOptions(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    ranges: Optional[List[IDRange]] = Field(
        None,
        description="ranges are the allowed ranges of gids that may be used. If you would like to force a single gid then supply a single range with the same start and end. Required for MustRunAs.",
    )
    rule: str = Field(
        ...,
        description="rule is the strategy that will dictate the allowable RunAsGroup values that may be set.",
    )


class RunAsUserStrategyOptions(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    ranges: Optional[List[IDRange]] = Field(
        None,
        description="ranges are the allowed ranges of uids that may be used. If you would like to force a single uid then supply a single range with the same start and end. Required for MustRunAs.",
    )
    rule: str = Field(
        ...,
        description="rule is the strategy that will dictate the allowable RunAsUser values that may be set.",
    )


class RuntimeClassStrategyOptions(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    allowed_runtime_class_names: List[str] = Field(
        ...,
        alias="allowedRuntimeClassNames",
        description='allowedRuntimeClassNames is a whitelist of RuntimeClass names that may be specified on a pod. A value of "*" means that any RuntimeClass name is allowed, and must be the only item in the list. An empty list requires the RuntimeClassName field to be unset.',
    )
    default_runtime_class_name: Optional[str] = Field(
        None,
        alias="defaultRuntimeClassName",
        description="defaultRuntimeClassName is the default RuntimeClassName to set on the pod. The default MUST be allowed by the allowedRuntimeClassNames list. A value of nil does not mutate the Pod.",
    )


class SELinuxStrategyOptions(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    rule: str = Field(
        ...,
        description="rule is the strategy that will dictate the allowable labels that may be set.",
    )
    se_linux_options: Optional[v1_1.SELinuxOptions] = Field(
        None,
        alias="seLinuxOptions",
        description="seLinuxOptions required to run as; required for MustRunAs More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/",
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


class SupplementalGroupsStrategyOptions(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    ranges: Optional[List[IDRange]] = Field(
        None,
        description="ranges are the allowed ranges of supplemental groups.  If you would like to force a single supplemental group then supply a single range with the same start and end. Required for MustRunAs.",
    )
    rule: Optional[str] = Field(
        None,
        description="rule is the strategy that will dictate what supplemental groups is used in the SecurityContext.",
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


class DeploymentRollback(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    api_version: Optional[str] = Field(
        "extensions/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind110] = Field(
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


class FSGroupStrategyOptions(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    ranges: Optional[List[IDRange]] = Field(
        None,
        description="ranges are the allowed ranges of fs groups.  If you would like to force a single fs group then supply a single range with the same start and end. Required for MustRunAs.",
    )
    rule: Optional[str] = Field(
        None,
        description="rule is the strategy that will dictate what FSGroup is used in the SecurityContext.",
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


class NetworkPolicyPort(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    port: Optional[Union[int, str]] = Field(
        None,
        description="If specified, the port on the given protocol.  This can either be a numerical or named port on a pod.  If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched.",
    )
    protocol: Optional[str] = Field(
        None,
        description="Optional.  The protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP.",
    )


class PodSecurityPolicySpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    allow_privilege_escalation: Optional[bool] = Field(
        None,
        alias="allowPrivilegeEscalation",
        description="allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true.",
    )
    allowed_csi_drivers: Optional[List[AllowedCSIDriver]] = Field(
        None,
        alias="allowedCSIDrivers",
        description="AllowedCSIDrivers is a whitelist of inline CSI drivers that must be explicitly set to be embedded within a pod spec. An empty value indicates that any CSI driver can be used for inline ephemeral volumes.",
    )
    allowed_capabilities: Optional[List[str]] = Field(
        None,
        alias="allowedCapabilities",
        description="allowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities.",
    )
    allowed_flex_volumes: Optional[List[AllowedFlexVolume]] = Field(
        None,
        alias="allowedFlexVolumes",
        description='allowedFlexVolumes is a whitelist of allowed Flexvolumes.  Empty or nil indicates that all Flexvolumes may be used.  This parameter is effective only when the usage of the Flexvolumes is allowed in the "volumes" field.',
    )
    allowed_host_paths: Optional[List[AllowedHostPath]] = Field(
        None,
        alias="allowedHostPaths",
        description="allowedHostPaths is a white list of allowed host paths. Empty indicates that all host paths may be used.",
    )
    allowed_proc_mount_types: Optional[List[str]] = Field(
        None,
        alias="allowedProcMountTypes",
        description="AllowedProcMountTypes is a whitelist of allowed ProcMountTypes. Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled.",
    )
    allowed_unsafe_sysctls: Optional[List[str]] = Field(
        None,
        alias="allowedUnsafeSysctls",
        description='allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to whitelist all allowed unsafe sysctls explicitly to avoid rejection.\n\nExamples: e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*" allows "foo.bar", "foo.baz", etc.',
    )
    default_add_capabilities: Optional[List[str]] = Field(
        None,
        alias="defaultAddCapabilities",
        description="defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list.",
    )
    default_allow_privilege_escalation: Optional[bool] = Field(
        None,
        alias="defaultAllowPrivilegeEscalation",
        description="defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process.",
    )
    forbidden_sysctls: Optional[List[str]] = Field(
        None,
        alias="forbiddenSysctls",
        description='forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden.\n\nExamples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc. e.g. "foo.*" forbids "foo.bar", "foo.baz", etc.',
    )
    fs_group: FSGroupStrategyOptions = Field(
        ...,
        alias="fsGroup",
        description="fsGroup is the strategy that will dictate what fs group is used by the SecurityContext.",
    )
    host_ipc: Optional[bool] = Field(
        None,
        alias="hostIPC",
        description="hostIPC determines if the policy allows the use of HostIPC in the pod spec.",
    )
    host_network: Optional[bool] = Field(
        None,
        alias="hostNetwork",
        description="hostNetwork determines if the policy allows the use of HostNetwork in the pod spec.",
    )
    host_pid: Optional[bool] = Field(
        None,
        alias="hostPID",
        description="hostPID determines if the policy allows the use of HostPID in the pod spec.",
    )
    host_ports: Optional[List[HostPortRange]] = Field(
        None,
        alias="hostPorts",
        description="hostPorts determines which host port ranges are allowed to be exposed.",
    )
    privileged: Optional[bool] = Field(
        None,
        description="privileged determines if a pod can request to be run as privileged.",
    )
    read_only_root_filesystem: Optional[bool] = Field(
        None,
        alias="readOnlyRootFilesystem",
        description="readOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.",
    )
    required_drop_capabilities: Optional[List[str]] = Field(
        None,
        alias="requiredDropCapabilities",
        description="requiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added.",
    )
    run_as_group: Optional[RunAsGroupStrategyOptions] = Field(
        None,
        alias="runAsGroup",
        description="RunAsGroup is the strategy that will dictate the allowable RunAsGroup values that may be set. If this field is omitted, the pod's RunAsGroup can take any value. This field requires the RunAsGroup feature gate to be enabled.",
    )
    run_as_user: RunAsUserStrategyOptions = Field(
        ...,
        alias="runAsUser",
        description="runAsUser is the strategy that will dictate the allowable RunAsUser values that may be set.",
    )
    runtime_class: Optional[RuntimeClassStrategyOptions] = Field(
        None,
        alias="runtimeClass",
        description="runtimeClass is the strategy that will dictate the allowable RuntimeClasses for a pod. If this field is omitted, the pod's runtimeClassName field is unrestricted. Enforcement of this field depends on the RuntimeClass feature gate being enabled.",
    )
    se_linux: SELinuxStrategyOptions = Field(
        ...,
        alias="seLinux",
        description="seLinux is the strategy that will dictate the allowable labels that may be set.",
    )
    supplemental_groups: SupplementalGroupsStrategyOptions = Field(
        ...,
        alias="supplementalGroups",
        description="supplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext.",
    )
    volumes: Optional[List[str]] = Field(
        None,
        description="volumes is a white list of allowed volume plugins. Empty indicates that no volumes may be used. To allow all volumes you may use '*'.",
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
        description="The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. By default, a value of 1 is used. Example: when this is set to 30%, the new RC can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new RC can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods.",
    )
    max_unavailable: Optional[Union[int, str]] = Field(
        None,
        alias="maxUnavailable",
        description="The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. By default, a fixed value of 1 is used. Example: when this is set to 30%, the old RC can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old RC can be scaled down further, followed by scaling up the new RC, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods.",
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
        description='Type of daemon set update. Can be "RollingUpdate" or "OnDelete". Default is OnDelete.',
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


class NetworkPolicyPeer(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    ip_block: Optional[IPBlock] = Field(
        None,
        alias="ipBlock",
        description="IPBlock defines policy on a particular IPBlock. If this field is set then neither of the other fields can be.",
    )
    namespace_selector: Optional[v1.LabelSelector] = Field(
        None,
        alias="namespaceSelector",
        description="Selects Namespaces using cluster-scoped labels. This field follows standard label selector semantics; if present but empty, it selects all namespaces.\n\nIf PodSelector is also set, then the NetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects all Pods in the Namespaces selected by NamespaceSelector.",
    )
    pod_selector: Optional[v1.LabelSelector] = Field(
        None,
        alias="podSelector",
        description="This is a label selector which selects Pods. This field follows standard label selector semantics; if present but empty, it selects all pods.\n\nIf NamespaceSelector is also set, then the NetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects the Pods matching PodSelector in the policy's own Namespace.",
    )


class PodSecurityPolicy(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "extensions/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind115] = Field(
        "PodSecurityPolicy",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[PodSecurityPolicySpec] = Field(
        None, description="spec defines the policy enforced."
    )


class PodSecurityPolicyList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "extensions/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[PodSecurityPolicy] = Field(
        ..., description="items is a list of schema objects."
    )
    kind: Optional[Kind116] = Field(
        "PodSecurityPolicyList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )


class Scale(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "extensions/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind119] = Field(
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


class Ingress(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "extensions/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind111] = Field(
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
        "extensions/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[Ingress] = Field(..., description="Items is the list of Ingress.")
    kind: Optional[Kind112] = Field(
        "IngressList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )


class NetworkPolicyEgressRule(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    ports: Optional[List[NetworkPolicyPort]] = Field(
        None,
        description="List of destination ports for outgoing traffic. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.",
    )
    to: Optional[List[NetworkPolicyPeer]] = Field(
        None,
        description="List of destinations for outgoing traffic of pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all destinations (traffic not restricted by destination). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the to list.",
    )


class NetworkPolicyIngressRule(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    from_: Optional[List[NetworkPolicyPeer]] = Field(
        None,
        alias="from",
        description="List of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the from list.",
    )
    ports: Optional[List[NetworkPolicyPort]] = Field(
        None,
        description="List of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.",
    )


class NetworkPolicySpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    egress: Optional[List[NetworkPolicyEgressRule]] = Field(
        None,
        description="List of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic matches at least one egress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it selects are isolated by default). This field is beta-level in 1.8",
    )
    ingress: Optional[List[NetworkPolicyIngressRule]] = Field(
        None,
        description="List of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod OR if the traffic source is the pod's local node, OR if the traffic matches at least one ingress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default).",
    )
    pod_selector: v1.LabelSelector = Field(
        ...,
        alias="podSelector",
        description="Selects the pods to which this NetworkPolicy object applies.  The array of ingress rules is applied to any pods selected by this field. Multiple network policies can select the same set of pods.  In this case, the ingress rules for each are combined additively. This field is NOT optional and follows standard label selector semantics. An empty podSelector matches all pods in this namespace.",
    )
    policy_types: Optional[List[str]] = Field(
        None,
        alias="policyTypes",
        description='List of rule types that the NetworkPolicy relates to. Valid options are "Ingress", "Egress", or "Ingress,Egress". If this field is not specified, it will default based on the existence of Ingress or Egress rules; policies that contain an Egress section are assumed to affect Egress, and all policies (whether or not they contain an Ingress section) are assumed to affect Ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ "Egress" ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include "Egress" (since such a policy would not include an Egress section and would otherwise default to just [ "Ingress" ]). This field is beta-level in 1.8',
    )


class NetworkPolicy(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "extensions/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind113] = Field(
        "NetworkPolicy",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[NetworkPolicySpec] = Field(
        None,
        description="Specification of the desired behavior for this NetworkPolicy.",
    )


class NetworkPolicyList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "extensions/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[NetworkPolicy] = Field(
        ..., description="Items is a list of schema objects."
    )
    kind: Optional[Kind114] = Field(
        "NetworkPolicyList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
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
    selector: Optional[v1.LabelSelector] = Field(
        None,
        description="A label query over pods that are managed by the daemon set. Must match in order to be controlled. If empty, defaulted to labels on Pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors",
    )
    template: v1_1.PodTemplateSpec = Field(
        ...,
        description="An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template",
    )
    template_generation: Optional[int] = Field(
        None,
        alias="templateGeneration",
        description="DEPRECATED. A sequence number representing a specific generation of the template. Populated by the system. It can be set only during the creation.",
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
        None,
        description="Indicates that the deployment is paused and will not be processed by the deployment controller.",
    )
    progress_deadline_seconds: Optional[int] = Field(
        None,
        alias="progressDeadlineSeconds",
        description='The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. This is set to the max value of int32 (i.e. 2147483647) by default, which means "no deadline".',
    )
    replicas: Optional[int] = Field(
        None,
        description="Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.",
    )
    revision_history_limit: Optional[int] = Field(
        None,
        alias="revisionHistoryLimit",
        description='The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. This is set to the max value of int32 (i.e. 2147483647) by default, which means "retaining all old RelicaSets".',
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
    selector: Optional[v1.LabelSelector] = Field(
        None,
        description="Selector is a label query over pods that should match the replica count. If the selector is empty, it is defaulted to the labels present on the pod template. Label keys and values that must match in order to be controlled by this replica set. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors",
    )
    template: Optional[v1_1.PodTemplateSpec] = Field(
        None,
        description="Template is the object that describes the pod that will be created if insufficient replicas are detected. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template",
    )


class DaemonSet(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "extensions/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind106] = Field(
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
        "extensions/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[DaemonSet] = Field(..., description="A list of daemon sets.")
    kind: Optional[Kind107] = Field(
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
        "extensions/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind108] = Field(
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
        "extensions/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[Deployment] = Field(
        ..., description="Items is the list of Deployments."
    )
    kind: Optional[Kind109] = Field(
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
        "extensions/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind117] = Field(
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
        "extensions/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[ReplicaSet] = Field(
        ...,
        description="List of ReplicaSets. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller",
    )
    kind: Optional[Kind118] = Field(
        "ReplicaSetList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
