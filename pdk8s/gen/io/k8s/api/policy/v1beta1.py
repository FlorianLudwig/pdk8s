# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Kind128, Kind129, Kind130, Kind131, Kind132
from ...apimachinery.pkg.apis.meta import v1
from ...apimachinery.pkg.util import intstr
from ..core import v1


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


class PodDisruptionBudgetStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    current_healthy: int = Field(
        ..., alias="currentHealthy", description="current number of healthy pods"
    )
    desired_healthy: int = Field(
        ...,
        alias="desiredHealthy",
        description="minimum desired number of healthy pods",
    )
    disrupted_pods: Optional[Dict[str, Any]] = Field(
        None,
        alias="disruptedPods",
        description="DisruptedPods contains information about pods whose eviction was processed by the API server eviction subresource handler but has not yet been observed by the PodDisruptionBudget controller. A pod will be in this map from the time when the API server processed the eviction request to the time when the pod is seen by PDB controller as having been marked for deletion (or after a timeout). The key in the map is the name of the pod and the value is the time when the API server processed the eviction request. If the deletion didn't occur and a pod is still there it will be removed from the list automatically by PodDisruptionBudget controller after some time. If everything goes smooth this map should be empty for the most of the time. Large number of entries in the map may indicate problems with pod deletions.",
    )
    disruptions_allowed: int = Field(
        ...,
        alias="disruptionsAllowed",
        description="Number of pod disruptions that are currently allowed.",
    )
    expected_pods: int = Field(
        ...,
        alias="expectedPods",
        description="total number of pods counted by this disruption budget",
    )
    observed_generation: Optional[int] = Field(
        None,
        alias="observedGeneration",
        description="Most recent generation observed when updating this PDB status. PodDisruptionsAllowed and other status informatio is valid only if observedGeneration equals to PDB's object generation.",
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
        description="AllowedCSIDrivers is a whitelist of inline CSI drivers that must be explicitly set to be embedded within a pod spec. An empty value indicates that any CSI driver can be used for inline ephemeral volumes. This is an alpha field, and is only honored if the API server enables the CSIInlineVolume feature gate.",
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


class Eviction(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "policy/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    delete_options: Optional[v1.DeleteOptions] = Field(
        None, alias="deleteOptions", description="DeleteOptions may be provided"
    )
    kind: Optional[Kind128] = Field(
        "Eviction",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None, description="ObjectMeta describes the pod that is being evicted."
    )


class PodDisruptionBudgetSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    max_unavailable: Optional[Union[int, str]] = Field(
        None,
        alias="maxUnavailable",
        description='An eviction is allowed if at most "maxUnavailable" pods selected by "selector" are unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting with "minAvailable".',
    )
    min_available: Optional[Union[int, str]] = Field(
        None,
        alias="minAvailable",
        description='An eviction is allowed if at least "minAvailable" pods selected by "selector" will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying "100%".',
    )
    selector: Optional[v1.LabelSelector] = Field(
        None,
        description="Label query over pods whose evictions are managed by the disruption budget.",
    )


class PodSecurityPolicy(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "policy/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind131] = Field(
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
        "policy/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[PodSecurityPolicy] = Field(
        ..., description="items is a list of schema objects."
    )
    kind: Optional[Kind132] = Field(
        "PodSecurityPolicyList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )


class PodDisruptionBudget(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "policy/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind129] = Field(
        "PodDisruptionBudget",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: Optional[PodDisruptionBudgetSpec] = Field(
        None,
        description="Specification of the desired behavior of the PodDisruptionBudget.",
    )


class PodDisruptionBudgetList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "policy/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[PodDisruptionBudget]
    kind: Optional[Kind130] = Field(
        "PodDisruptionBudgetList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = None
