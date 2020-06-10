# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from ..... import Kind165, Kind166, Kind167, Kind168
from ...apimachinery.pkg.apis.meta import v1 as v1_1
from ..core import v1


class VolumeError(BaseModel):
    message: Optional[str] = Field(
        None,
        description="String detailing the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information.",
    )
    time: Optional[v1.Time] = Field(None, description="Time the error was encountered.")


class StorageClass(BaseModel):
    allowVolumeExpansion: Optional[bool] = Field(
        None,
        description="AllowVolumeExpansion shows whether the storage class allow volume expand",
    )
    allowedTopologies: Optional[List[v1.TopologySelectorTerm]] = Field(
        None,
        description="Restrict the node topologies where volumes can be dynamically provisioned. Each volume plugin defines its own supported topology specifications. An empty TopologySelectorTerm list means there is no topology restriction. This field is only honored by servers that enable the VolumeScheduling feature.",
    )
    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind165] = Field(
        "StorageClass",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1_1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    mountOptions: Optional[List[str]] = Field(
        None,
        description='Dynamically provisioned PersistentVolumes of this storage class are created with these mountOptions, e.g. ["ro", "soft"]. Not validated - mount of the PVs will simply fail if one is invalid.',
    )
    parameters: Optional[Dict[str, Any]] = Field(
        None,
        description="Parameters holds the parameters for the provisioner that should create volumes of this storage class.",
    )
    provisioner: str = Field(
        ..., description="Provisioner indicates the type of the provisioner."
    )
    reclaimPolicy: Optional[str] = Field(
        None,
        description="Dynamically provisioned PersistentVolumes of this storage class are created with this reclaimPolicy. Defaults to Delete.",
    )
    volumeBindingMode: Optional[str] = Field(
        None,
        description="VolumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.  When unset, VolumeBindingImmediate is used. This field is only honored by servers that enable the VolumeScheduling feature.",
    )


class StorageClassList(BaseModel):
    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[StorageClass] = Field(
        ..., description="Items is the list of StorageClasses"
    )
    kind: Optional[Kind166] = Field(
        "StorageClassList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )


class VolumeAttachmentSource(BaseModel):
    inlineVolumeSpec: Optional[v1.PersistentVolumeSpec] = Field(
        None,
        description="inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is alpha-level and is only honored by servers that enabled the CSIMigration feature.",
    )
    persistentVolumeName: Optional[str] = Field(
        None, description="Name of the persistent volume to attach."
    )


class VolumeAttachmentSpec(BaseModel):
    attacher: str = Field(
        ...,
        description="Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().",
    )
    nodeName: str = Field(
        ..., description="The node that the volume should be attached to."
    )
    source: VolumeAttachmentSource = Field(
        ..., description="Source represents the volume that should be attached."
    )


class VolumeAttachmentStatus(BaseModel):
    attachError: Optional[VolumeError] = Field(
        None,
        description="The last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.",
    )
    attached: bool = Field(
        ...,
        description="Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.",
    )
    attachmentMetadata: Optional[Dict[str, Any]] = Field(
        None,
        description="Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.",
    )
    detachError: Optional[VolumeError] = Field(
        None,
        description="The last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher.",
    )


class VolumeAttachment(BaseModel):
    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind167] = Field(
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
    status: Optional[VolumeAttachmentStatus] = Field(
        None,
        description="Status of the VolumeAttachment request. Populated by the entity completing the attach or detach operation, i.e. the external-attacher.",
    )


class VolumeAttachmentList(BaseModel):
    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[VolumeAttachment] = Field(
        ..., description="Items is the list of VolumeAttachments"
    )
    kind: Optional[Kind168] = Field(
        "VolumeAttachmentList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
