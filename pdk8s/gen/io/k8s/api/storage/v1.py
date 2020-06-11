# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Kind165, Kind166, Kind167, Kind168
from ...apimachinery.pkg.apis.meta import v1 as v1_1
from ..core import v1


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
        "storage.k8s.io/v1",
        alias="apiVersion",
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
        "storage.k8s.io/v1",
        alias="apiVersion",
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
        "storage.k8s.io/v1",
        alias="apiVersion",
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


class VolumeAttachmentList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "storage.k8s.io/v1",
        alias="apiVersion",
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
