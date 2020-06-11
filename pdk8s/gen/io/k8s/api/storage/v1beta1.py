# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Kind171, Kind172, Kind173, Kind174, Kind175, Kind176, Kind177, Kind178
from ...apimachinery.pkg.apis.meta import v1 as v1_1
from ..core import v1


class CSIDriverSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    attach_required: Optional[bool] = Field(
        None,
        alias="attachRequired",
        description="attachRequired indicates this CSI volume driver requires an attach operation (because it implements the CSI ControllerPublishVolume() method), and that the Kubernetes attach detach controller should call the attach volume interface which checks the volumeattachment status and waits until the volume is attached before proceeding to mounting. The CSI external-attacher coordinates with CSI volume driver and updates the volumeattachment status when the attach operation is complete. If the CSIDriverRegistry feature gate is enabled and the value is specified to false, the attach operation will be skipped. Otherwise the attach operation will be called.",
    )
    pod_info_on_mount: Optional[bool] = Field(
        None,
        alias="podInfoOnMount",
        description='If set to true, podInfoOnMount indicates this CSI volume driver requires additional pod information (like podName, podUID, etc.) during mount operations. If set to false, pod information will not be passed on mount. Default is false. The CSI driver specifies podInfoOnMount as part of driver deployment. If true, Kubelet will pass pod information as VolumeContext in the CSI NodePublishVolume() calls. The CSI driver is responsible for parsing and validating the information passed in as VolumeContext. The following VolumeConext will be passed if podInfoOnMount is set to true. This list might grow, but the prefix will be used. "csi.storage.k8s.io/pod.name": pod.Name "csi.storage.k8s.io/pod.namespace": pod.Namespace "csi.storage.k8s.io/pod.uid": string(pod.UID) "csi.storage.k8s.io/ephemeral": "true" iff the volume is an ephemeral inline volume\n                                defined by a CSIVolumeSource, otherwise "false"\n\n"csi.storage.k8s.io/ephemeral" is a new feature in Kubernetes 1.16. It is only required for drivers which support both the "Persistent" and "Ephemeral" VolumeLifecycleMode. Other drivers can leave pod info disabled and/or ignore this field. As Kubernetes 1.15 doesn\'t support this field, drivers can only support one mode when deployed on such a cluster and the deployment determines which mode that is, for example via a command line parameter of the driver.',
    )
    volume_lifecycle_modes: Optional[List[str]] = Field(
        None,
        alias="volumeLifecycleModes",
        description='VolumeLifecycleModes defines what kind of volumes this CSI volume driver supports. The default if the list is empty is "Persistent", which is the usage defined by the CSI specification and implemented in Kubernetes via the usual PV/PVC mechanism. The other mode is "Ephemeral". In this mode, volumes are defined inline inside the pod spec with CSIVolumeSource and their lifecycle is tied to the lifecycle of that pod. A driver has to be aware of this because it is only going to get a NodePublishVolume call for such a volume. For more information about implementing this mode, see https://kubernetes-csi.github.io/docs/ephemeral-local-volumes.html A driver can support one or more of these modes and more modes may be added in the future.',
    )


class VolumeNodeResources(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    count: Optional[int] = Field(
        None,
        description="Maximum number of unique volumes managed by the CSI driver that can be used on a node. A volume that is both attached and mounted on a node is considered to be used once, not twice. The same rule applies for a unique volume that is shared among multiple pods on the same node. If this field is nil, then the supported number of volumes on this node is unbounded.",
    )


class CSINodeDriver(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    allocatable: Optional[VolumeNodeResources] = Field(
        None,
        description="allocatable represents the volume resources of a node that are available for scheduling.",
    )
    name: str = Field(
        ...,
        description="This is the name of the CSI driver that this object refers to. This MUST be the same name returned by the CSI GetPluginName() call for that driver.",
    )
    node_id: str = Field(
        ...,
        alias="nodeID",
        description='nodeID of the node from the driver point of view. This field enables Kubernetes to communicate with storage systems that do not share the same nomenclature for nodes. For example, Kubernetes may refer to a given node as "node1", but the storage system may refer to the same node as "nodeA". When Kubernetes issues a command to the storage system to attach a volume to a specific node, it can use this field to refer to the node name using the ID that the storage system will understand, e.g. "nodeA" instead of "node1". This field is required.',
    )
    topology_keys: Optional[List[str]] = Field(
        None,
        alias="topologyKeys",
        description='topologyKeys is the list of keys supported by the driver. When a driver is initialized on a cluster, it provides a set of topology keys that it understands (e.g. "company.com/zone", "company.com/region"). When a driver is initialized on a node, it provides the same topology keys along with values. Kubelet will expose these topology keys as labels on its own node object. When Kubernetes does topology aware provisioning, it can use this list to determine which labels it should retrieve from the node object and pass back to the driver. It is possible for different nodes to use different topology keys. This can be empty if driver does not support topology.',
    )


class CSINodeSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    drivers: List[CSINodeDriver] = Field(
        ...,
        description="drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty.",
    )


class VolumeError(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    message: Optional[str] = Field(
        None,
        description="String detailing the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information.",
    )
    time: Optional[v1.Time] = Field(None, description="Time the error was encountered.")


class CSIDriver(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "storage.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind171] = Field(
        "CSIDriver",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object metadata. metadata.Name indicates the name of the CSI driver that this object refers to; it MUST be the same name returned by the CSI GetPluginName() call for that driver. The driver name must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), dots (.), and alphanumerics between. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: CSIDriverSpec = Field(..., description="Specification of the CSI Driver.")


class CSIDriverList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "storage.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[CSIDriver] = Field(..., description="items is the list of CSIDriver")
    kind: Optional[Kind172] = Field(
        "CSIDriverList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )


class CSINode(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "storage.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind173] = Field(
        "CSINode",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None, description="metadata.name must be the Kubernetes node name."
    )
    spec: CSINodeSpec = Field(..., description="spec is the specification of CSINode")


class CSINodeList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "storage.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[CSINode] = Field(..., description="items is the list of CSINode")
    kind: Optional[Kind174] = Field(
        "CSINodeList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )


class StorageClass(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    allow_volume_expansion: Optional[bool] = Field(
        None,
        alias="allowVolumeExpansion",
        description="AllowVolumeExpansion shows whether the storage class allow volume expand",
    )
    allowed_topologies: Optional[List[v1.TopologySelectorTerm]] = Field(
        None,
        alias="allowedTopologies",
        description="Restrict the node topologies where volumes can be dynamically provisioned. Each volume plugin defines its own supported topology specifications. An empty TopologySelectorTerm list means there is no topology restriction. This field is only honored by servers that enable the VolumeScheduling feature.",
    )
    api_version: Optional[str] = Field(
        "storage.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind175] = Field(
        "StorageClass",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1_1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    mount_options: Optional[List[str]] = Field(
        None,
        alias="mountOptions",
        description='Dynamically provisioned PersistentVolumes of this storage class are created with these mountOptions, e.g. ["ro", "soft"]. Not validated - mount of the PVs will simply fail if one is invalid.',
    )
    parameters: Optional[Dict[str, Any]] = Field(
        None,
        description="Parameters holds the parameters for the provisioner that should create volumes of this storage class.",
    )
    provisioner: str = Field(
        ..., description="Provisioner indicates the type of the provisioner."
    )
    reclaim_policy: Optional[str] = Field(
        None,
        alias="reclaimPolicy",
        description="Dynamically provisioned PersistentVolumes of this storage class are created with this reclaimPolicy. Defaults to Delete.",
    )
    volume_binding_mode: Optional[str] = Field(
        None,
        alias="volumeBindingMode",
        description="VolumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.  When unset, VolumeBindingImmediate is used. This field is only honored by servers that enable the VolumeScheduling feature.",
    )


class StorageClassList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "storage.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[StorageClass] = Field(
        ..., description="Items is the list of StorageClasses"
    )
    kind: Optional[Kind176] = Field(
        "StorageClassList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )


class VolumeAttachmentSource(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    inline_volume_spec: Optional[v1.PersistentVolumeSpec] = Field(
        None,
        alias="inlineVolumeSpec",
        description="inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is alpha-level and is only honored by servers that enabled the CSIMigration feature.",
    )
    persistent_volume_name: Optional[str] = Field(
        None,
        alias="persistentVolumeName",
        description="Name of the persistent volume to attach.",
    )


class VolumeAttachmentSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    attacher: str = Field(
        ...,
        description="Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().",
    )
    node_name: str = Field(
        ...,
        alias="nodeName",
        description="The node that the volume should be attached to.",
    )
    source: VolumeAttachmentSource = Field(
        ..., description="Source represents the volume that should be attached."
    )


class VolumeAttachmentStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    attach_error: Optional[VolumeError] = Field(
        None,
        alias="attachError",
        description="The last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.",
    )
    attached: bool = Field(
        ...,
        description="Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.",
    )
    attachment_metadata: Optional[Dict[str, Any]] = Field(
        None,
        alias="attachmentMetadata",
        description="Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.",
    )
    detach_error: Optional[VolumeError] = Field(
        None,
        alias="detachError",
        description="The last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher.",
    )


class VolumeAttachment(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "storage.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind177] = Field(
        "VolumeAttachment",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: VolumeAttachmentSpec = Field(
        ...,
        description="Specification of the desired attach/detach volume behavior. Populated by the Kubernetes system.",
    )


class VolumeAttachmentList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "storage.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[VolumeAttachment] = Field(
        ..., description="Items is the list of VolumeAttachments"
    )
    kind: Optional[Kind178] = Field(
        "VolumeAttachmentList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
