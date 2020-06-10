# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from ..... import Kind128, Kind129, Kind130, Kind131, Kind132
from ...apimachinery.pkg.apis.meta import v1
from ...apimachinery.pkg.util import intstr
from ..core import v1


class AllowedCSIDriver(BaseModel):
    name: str = Field(..., description='Name is the registered name of the CSI driver')


class AllowedFlexVolume(BaseModel):
    driver: str = Field(..., description='driver is the name of the Flexvolume driver.')


class AllowedHostPath(BaseModel):
    pathPrefix: Optional[str] = Field(
        None,
        description='pathPrefix is the path prefix that the host volume must match. It does not support `*`. Trailing slashes are trimmed when validating the path prefix with a host path.\n\nExamples: `/foo` would allow `/foo`, `/foo/` and `/foo/bar` `/foo` would not allow `/food` or `/etc/foo`',
    )
    readOnly: Optional[bool] = Field(
        None,
        description='when set to true, will allow host volumes matching the pathPrefix only if all volume mounts are readOnly.',
    )


class HostPortRange(BaseModel):
    max: int = Field(..., description='max is the end of the range, inclusive.')
    min: int = Field(..., description='min is the start of the range, inclusive.')


class IDRange(BaseModel):
    max: int = Field(..., description='max is the end of the range, inclusive.')
    min: int = Field(..., description='min is the start of the range, inclusive.')


class PodDisruptionBudgetStatus(BaseModel):
    currentHealthy: int = Field(..., description='current number of healthy pods')
    desiredHealthy: int = Field(
        ..., description='minimum desired number of healthy pods'
    )
    disruptedPods: Optional[Dict[str, Any]] = Field(
        None,
        description="DisruptedPods contains information about pods whose eviction was processed by the API server eviction subresource handler but has not yet been observed by the PodDisruptionBudget controller. A pod will be in this map from the time when the API server processed the eviction request to the time when the pod is seen by PDB controller as having been marked for deletion (or after a timeout). The key in the map is the name of the pod and the value is the time when the API server processed the eviction request. If the deletion didn't occur and a pod is still there it will be removed from the list automatically by PodDisruptionBudget controller after some time. If everything goes smooth this map should be empty for the most of the time. Large number of entries in the map may indicate problems with pod deletions.",
    )
    disruptionsAllowed: int = Field(
        ..., description='Number of pod disruptions that are currently allowed.'
    )
    expectedPods: int = Field(
        ..., description='total number of pods counted by this disruption budget'
    )
    observedGeneration: Optional[int] = Field(
        None,
        description="Most recent generation observed when updating this PDB status. PodDisruptionsAllowed and other status informatio is valid only if observedGeneration equals to PDB's object generation.",
    )


class RunAsGroupStrategyOptions(BaseModel):
    ranges: Optional[List[IDRange]] = Field(
        None,
        description='ranges are the allowed ranges of gids that may be used. If you would like to force a single gid then supply a single range with the same start and end. Required for MustRunAs.',
    )
    rule: str = Field(
        ...,
        description='rule is the strategy that will dictate the allowable RunAsGroup values that may be set.',
    )


class RunAsUserStrategyOptions(BaseModel):
    ranges: Optional[List[IDRange]] = Field(
        None,
        description='ranges are the allowed ranges of uids that may be used. If you would like to force a single uid then supply a single range with the same start and end. Required for MustRunAs.',
    )
    rule: str = Field(
        ...,
        description='rule is the strategy that will dictate the allowable RunAsUser values that may be set.',
    )


class RuntimeClassStrategyOptions(BaseModel):
    allowedRuntimeClassNames: List[str] = Field(
        ...,
        description='allowedRuntimeClassNames is a whitelist of RuntimeClass names that may be specified on a pod. A value of "*" means that any RuntimeClass name is allowed, and must be the only item in the list. An empty list requires the RuntimeClassName field to be unset.',
    )
    defaultRuntimeClassName: Optional[str] = Field(
        None,
        description='defaultRuntimeClassName is the default RuntimeClassName to set on the pod. The default MUST be allowed by the allowedRuntimeClassNames list. A value of nil does not mutate the Pod.',
    )


class SELinuxStrategyOptions(BaseModel):
    rule: str = Field(
        ...,
        description='rule is the strategy that will dictate the allowable labels that may be set.',
    )
    seLinuxOptions: Optional[v1.SELinuxOptions] = Field(
        None,
        description='seLinuxOptions required to run as; required for MustRunAs More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/',
    )


class SupplementalGroupsStrategyOptions(BaseModel):
    ranges: Optional[List[IDRange]] = Field(
        None,
        description='ranges are the allowed ranges of supplemental groups.  If you would like to force a single supplemental group then supply a single range with the same start and end. Required for MustRunAs.',
    )
    rule: Optional[str] = Field(
        None,
        description='rule is the strategy that will dictate what supplemental groups is used in the SecurityContext.',
    )


class FSGroupStrategyOptions(BaseModel):
    ranges: Optional[List[IDRange]] = Field(
        None,
        description='ranges are the allowed ranges of fs groups.  If you would like to force a single fs group then supply a single range with the same start and end. Required for MustRunAs.',
    )
    rule: Optional[str] = Field(
        None,
        description='rule is the strategy that will dictate what FSGroup is used in the SecurityContext.',
    )


class PodSecurityPolicySpec(BaseModel):
    allowPrivilegeEscalation: Optional[bool] = Field(
        None,
        description='allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true.',
    )
    allowedCSIDrivers: Optional[List[AllowedCSIDriver]] = Field(
        None,
        description='AllowedCSIDrivers is a whitelist of inline CSI drivers that must be explicitly set to be embedded within a pod spec. An empty value indicates that any CSI driver can be used for inline ephemeral volumes. This is an alpha field, and is only honored if the API server enables the CSIInlineVolume feature gate.',
    )
    allowedCapabilities: Optional[List[str]] = Field(
        None,
        description="allowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities.",
    )
    allowedFlexVolumes: Optional[List[AllowedFlexVolume]] = Field(
        None,
        description='allowedFlexVolumes is a whitelist of allowed Flexvolumes.  Empty or nil indicates that all Flexvolumes may be used.  This parameter is effective only when the usage of the Flexvolumes is allowed in the "volumes" field.',
    )
    allowedHostPaths: Optional[List[AllowedHostPath]] = Field(
        None,
        description='allowedHostPaths is a white list of allowed host paths. Empty indicates that all host paths may be used.',
    )
    allowedProcMountTypes: Optional[List[str]] = Field(
        None,
        description='AllowedProcMountTypes is a whitelist of allowed ProcMountTypes. Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled.',
    )
    allowedUnsafeSysctls: Optional[List[str]] = Field(
        None,
        description='allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to whitelist all allowed unsafe sysctls explicitly to avoid rejection.\n\nExamples: e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*" allows "foo.bar", "foo.baz", etc.',
    )
    defaultAddCapabilities: Optional[List[str]] = Field(
        None,
        description='defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list.',
    )
    defaultAllowPrivilegeEscalation: Optional[bool] = Field(
        None,
        description='defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process.',
    )
    forbiddenSysctls: Optional[List[str]] = Field(
        None,
        description='forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden.\n\nExamples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc. e.g. "foo.*" forbids "foo.bar", "foo.baz", etc.',
    )
    fsGroup: FSGroupStrategyOptions = Field(
        ...,
        description='fsGroup is the strategy that will dictate what fs group is used by the SecurityContext.',
    )
    hostIPC: Optional[bool] = Field(
        None,
        description='hostIPC determines if the policy allows the use of HostIPC in the pod spec.',
    )
    hostNetwork: Optional[bool] = Field(
        None,
        description='hostNetwork determines if the policy allows the use of HostNetwork in the pod spec.',
    )
    hostPID: Optional[bool] = Field(
        None,
        description='hostPID determines if the policy allows the use of HostPID in the pod spec.',
    )
    hostPorts: Optional[List[HostPortRange]] = Field(
        None,
        description='hostPorts determines which host port ranges are allowed to be exposed.',
    )
    privileged: Optional[bool] = Field(
        None,
        description='privileged determines if a pod can request to be run as privileged.',
    )
    readOnlyRootFilesystem: Optional[bool] = Field(
        None,
        description='readOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.',
    )
    requiredDropCapabilities: Optional[List[str]] = Field(
        None,
        description='requiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added.',
    )
    runAsGroup: Optional[RunAsGroupStrategyOptions] = Field(
        None,
        description="RunAsGroup is the strategy that will dictate the allowable RunAsGroup values that may be set. If this field is omitted, the pod's RunAsGroup can take any value. This field requires the RunAsGroup feature gate to be enabled.",
    )
    runAsUser: RunAsUserStrategyOptions = Field(
        ...,
        description='runAsUser is the strategy that will dictate the allowable RunAsUser values that may be set.',
    )
    runtimeClass: Optional[RuntimeClassStrategyOptions] = Field(
        None,
        description="runtimeClass is the strategy that will dictate the allowable RuntimeClasses for a pod. If this field is omitted, the pod's runtimeClassName field is unrestricted. Enforcement of this field depends on the RuntimeClass feature gate being enabled.",
    )
    seLinux: SELinuxStrategyOptions = Field(
        ...,
        description='seLinux is the strategy that will dictate the allowable labels that may be set.',
    )
    supplementalGroups: SupplementalGroupsStrategyOptions = Field(
        ...,
        description='supplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext.',
    )
    volumes: Optional[List[str]] = Field(
        None,
        description="volumes is a white list of allowed volume plugins. Empty indicates that no volumes may be used. To allow all volumes you may use '*'.",
    )


class Eviction(BaseModel):
    apiVersion: Optional[str] = Field(
        'v1beta1',
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    deleteOptions: Optional[v1.DeleteOptions] = Field(
        None, description='DeleteOptions may be provided'
    )
    kind: Optional[Kind128] = Field(
        'Eviction',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None, description='ObjectMeta describes the pod that is being evicted.'
    )


class PodDisruptionBudgetSpec(BaseModel):
    maxUnavailable: Optional[intstr.IntOrString] = Field(
        None,
        description='An eviction is allowed if at most "maxUnavailable" pods selected by "selector" are unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting with "minAvailable".',
    )
    minAvailable: Optional[intstr.IntOrString] = Field(
        None,
        description='An eviction is allowed if at least "minAvailable" pods selected by "selector" will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying "100%".',
    )
    selector: Optional[v1.LabelSelector] = Field(
        None,
        description='Label query over pods whose evictions are managed by the disruption budget.',
    )


class PodSecurityPolicy(BaseModel):
    apiVersion: Optional[str] = Field(
        'v1beta1',
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[Kind131] = Field(
        'PodSecurityPolicy',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[PodSecurityPolicySpec] = Field(
        None, description='spec defines the policy enforced.'
    )


class PodSecurityPolicyList(BaseModel):
    apiVersion: Optional[str] = Field(
        'v1beta1',
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[PodSecurityPolicy] = Field(
        ..., description='items is a list of schema objects.'
    )
    kind: Optional[Kind132] = Field(
        'PodSecurityPolicyList',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata',
    )


class PodDisruptionBudget(BaseModel):
    apiVersion: Optional[str] = Field(
        'v1beta1',
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[Kind129] = Field(
        'PodDisruptionBudget',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: Optional[PodDisruptionBudgetSpec] = Field(
        None,
        description='Specification of the desired behavior of the PodDisruptionBudget.',
    )
    status: Optional[PodDisruptionBudgetStatus] = Field(
        None, description='Most recently observed status of the PodDisruptionBudget.'
    )


class PodDisruptionBudgetList(BaseModel):
    apiVersion: Optional[str] = Field(
        'v1beta1',
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[PodDisruptionBudget]
    kind: Optional[Kind130] = Field(
        'PodDisruptionBudgetList',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = None
