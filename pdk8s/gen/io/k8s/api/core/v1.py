# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from ..... import (
    Kind69,
    Kind70,
    Kind71,
    Kind72,
    Kind73,
    Kind74,
    Kind75,
    Kind76,
    Kind77,
    Kind78,
    Kind79,
    Kind80,
    Kind81,
    Kind82,
    Kind83,
    Kind84,
    Kind85,
    Kind86,
    Kind87,
    Kind88,
    Kind89,
    Kind90,
    Kind91,
    Kind92,
    Kind93,
    Kind94,
    Kind95,
    Kind96,
    Kind97,
    Kind98,
    Kind99,
    Kind100,
    Kind101,
)
from ...apimachinery.pkg.api import resource
from ...apimachinery.pkg.apis.meta import v1
from ...apimachinery.pkg.util import intstr


class AWSElasticBlockStoreVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    fsType: Optional[str] = Field(
        None,
        description='Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore',
    )
    partition: Optional[int] = Field(
        None,
        description='The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).',
    )
    readOnly: Optional[bool] = Field(
        None,
        description='Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". If omitted, the default is "false". More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore',
    )
    volumeID: str = Field(
        ...,
        description="Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore",
    )


class AttachedVolume(BaseModel):
    class Config:
        extra = "forbid"

    devicePath: str = Field(
        ...,
        description="DevicePath represents the device path where the volume should be available",
    )
    name: str = Field(..., description="Name of the attached volume")


class AzureDiskVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    cachingMode: Optional[str] = Field(
        None, description="Host Caching mode: None, Read Only, Read Write."
    )
    diskName: str = Field(
        ..., description="The Name of the data disk in the blob storage"
    )
    diskURI: str = Field(..., description="The URI the data disk in the blob storage")
    fsType: Optional[str] = Field(
        None,
        description='Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.',
    )
    kind: Optional[str] = Field(
        None,
        description="Expected values Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared",
    )
    readOnly: Optional[bool] = Field(
        None,
        description="Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.",
    )


class AzureFilePersistentVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    readOnly: Optional[bool] = Field(
        None,
        description="Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.",
    )
    secretName: str = Field(
        ...,
        description="the name of secret that contains Azure Storage Account Name and Key",
    )
    secretNamespace: Optional[str] = Field(
        None,
        description="the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod",
    )
    shareName: str = Field(..., description="Share Name")


class AzureFileVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    readOnly: Optional[bool] = Field(
        None,
        description="Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.",
    )
    secretName: str = Field(
        ...,
        description="the name of secret that contains Azure Storage Account Name and Key",
    )
    shareName: str = Field(..., description="Share Name")


class Capabilities(BaseModel):
    class Config:
        extra = "forbid"

    add: Optional[List[str]] = Field(None, description="Added capabilities")
    drop: Optional[List[str]] = Field(None, description="Removed capabilities")


class ClientIPConfig(BaseModel):
    class Config:
        extra = "forbid"

    timeoutSeconds: Optional[int] = Field(
        None,
        description='timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value must be >0 && <=86400(for 1 day) if ServiceAffinity == "ClientIP". Default value is 10800(for 3 hours).',
    )


class ComponentCondition(BaseModel):
    class Config:
        extra = "forbid"

    error: Optional[str] = Field(
        None,
        description="Condition error code for a component. For example, a health check error code.",
    )
    message: Optional[str] = Field(
        None,
        description="Message about the condition for a component. For example, information about a health check.",
    )
    status: str = Field(
        ...,
        description='Status of the condition for a component. Valid values for "Healthy": "True", "False", or "Unknown".',
    )
    type: str = Field(
        ..., description='Type of condition for a component. Valid value: "Healthy"'
    )


class ConfigMapEnvSource(BaseModel):
    class Config:
        extra = "forbid"

    name: Optional[str] = Field(
        None,
        description="Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names",
    )
    optional: Optional[bool] = Field(
        None, description="Specify whether the ConfigMap must be defined"
    )


class ConfigMapKeySelector(BaseModel):
    class Config:
        extra = "forbid"

    key: str = Field(..., description="The key to select.")
    name: Optional[str] = Field(
        None,
        description="Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names",
    )
    optional: Optional[bool] = Field(
        None, description="Specify whether the ConfigMap or its key must be defined"
    )


class ConfigMapNodeConfigSource(BaseModel):
    class Config:
        extra = "forbid"

    kubeletConfigKey: str = Field(
        ...,
        description="KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.",
    )
    name: str = Field(
        ...,
        description="Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.",
    )
    namespace: str = Field(
        ...,
        description="Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases.",
    )
    resourceVersion: Optional[str] = Field(
        None,
        description="ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.",
    )
    uid: Optional[str] = Field(
        None,
        description="UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.",
    )


class ContainerImage(BaseModel):
    class Config:
        extra = "forbid"

    names: List[str] = Field(
        ...,
        description='Names by which this image is known. e.g. ["k8s.gcr.io/hyperkube:v1.0.7", "dockerhub.io/google_containers/hyperkube:v1.0.7"]',
    )
    sizeBytes: Optional[int] = Field(
        None, description="The size of the image in bytes."
    )


class ContainerPort(BaseModel):
    class Config:
        extra = "forbid"

    containerPort: int = Field(
        ...,
        description="Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536.",
    )
    hostIP: Optional[str] = Field(
        None, description="What host IP to bind the external port to."
    )
    hostPort: Optional[int] = Field(
        None,
        description="Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.",
    )
    name: Optional[str] = Field(
        None,
        description="If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.",
    )
    protocol: Optional[str] = Field(
        None,
        description='Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".',
    )


class ContainerStateWaiting(BaseModel):
    class Config:
        extra = "forbid"

    message: Optional[str] = Field(
        None, description="Message regarding why the container is not yet running."
    )
    reason: Optional[str] = Field(
        None, description="(brief) reason the container is not yet running."
    )


class DaemonEndpoint(BaseModel):
    class Config:
        extra = "forbid"

    Port: int = Field(..., description="Port number of the given endpoint.")


class EndpointPort(BaseModel):
    class Config:
        extra = "forbid"

    name: Optional[str] = Field(
        None,
        description="The name of this port.  This must match the 'name' field in the corresponding ServicePort. Must be a DNS_LABEL. Optional only if one port is defined.",
    )
    port: int = Field(..., description="The port number of the endpoint.")
    protocol: Optional[str] = Field(
        None,
        description="The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.",
    )


class EventSource(BaseModel):
    class Config:
        extra = "forbid"

    component: Optional[str] = Field(
        None, description="Component from which the event is generated."
    )
    host: Optional[str] = Field(
        None, description="Node name on which the event is generated."
    )


class ExecAction(BaseModel):
    class Config:
        extra = "forbid"

    command: Optional[List[str]] = Field(
        None,
        description="Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.",
    )


class FCVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    fsType: Optional[str] = Field(
        None,
        description='Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.',
    )
    lun: Optional[int] = Field(None, description="Optional: FC target lun number")
    readOnly: Optional[bool] = Field(
        None,
        description="Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.",
    )
    targetWWNs: Optional[List[str]] = Field(
        None, description="Optional: FC target worldwide names (WWNs)"
    )
    wwids: Optional[List[str]] = Field(
        None,
        description="Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.",
    )


class FlockerVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    datasetName: Optional[str] = Field(
        None,
        description="Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated",
    )
    datasetUUID: Optional[str] = Field(
        None,
        description="UUID of the dataset. This is unique identifier of a Flocker dataset",
    )


class GCEPersistentDiskVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    fsType: Optional[str] = Field(
        None,
        description='Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk',
    )
    partition: Optional[int] = Field(
        None,
        description='The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk',
    )
    pdName: str = Field(
        ...,
        description="Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk",
    )
    readOnly: Optional[bool] = Field(
        None,
        description="ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk",
    )


class GitRepoVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    directory: Optional[str] = Field(
        None,
        description="Target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.",
    )
    repository: str = Field(..., description="Repository URL")
    revision: Optional[str] = Field(
        None, description="Commit hash for the specified revision."
    )


class GlusterfsPersistentVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    endpoints: str = Field(
        ...,
        description="EndpointsName is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod",
    )
    endpointsNamespace: Optional[str] = Field(
        None,
        description="EndpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod",
    )
    path: str = Field(
        ...,
        description="Path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod",
    )
    readOnly: Optional[bool] = Field(
        None,
        description="ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod",
    )


class GlusterfsVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    endpoints: str = Field(
        ...,
        description="EndpointsName is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod",
    )
    path: str = Field(
        ...,
        description="Path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod",
    )
    readOnly: Optional[bool] = Field(
        None,
        description="ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod",
    )


class HTTPHeader(BaseModel):
    class Config:
        extra = "forbid"

    name: str = Field(..., description="The header field name")
    value: str = Field(..., description="The header field value")


class HostAlias(BaseModel):
    class Config:
        extra = "forbid"

    hostnames: Optional[List[str]] = Field(
        None, description="Hostnames for the above IP address."
    )
    ip: Optional[str] = Field(None, description="IP address of the host file entry.")


class HostPathVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    path: str = Field(
        ...,
        description="Path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath",
    )
    type: Optional[str] = Field(
        None,
        description='Type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath',
    )


class KeyToPath(BaseModel):
    class Config:
        extra = "forbid"

    key: str = Field(..., description="The key to project.")
    mode: Optional[int] = Field(
        None,
        description="Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.",
    )
    path: str = Field(
        ...,
        description="The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.",
    )


class LimitRangeItem(BaseModel):
    class Config:
        extra = "forbid"

    default: Optional[Dict[str, Any]] = Field(
        None,
        description="Default resource requirement limit value by resource name if resource limit is omitted.",
    )
    defaultRequest: Optional[Dict[str, Any]] = Field(
        None,
        description="DefaultRequest is the default resource requirement request value by resource name if resource request is omitted.",
    )
    max: Optional[Dict[str, Any]] = Field(
        None, description="Max usage constraints on this kind by resource name."
    )
    maxLimitRequestRatio: Optional[Dict[str, Any]] = Field(
        None,
        description="MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource.",
    )
    min: Optional[Dict[str, Any]] = Field(
        None, description="Min usage constraints on this kind by resource name."
    )
    type: Optional[str] = Field(
        None, description="Type of resource that this limit applies to."
    )


class LimitRangeSpec(BaseModel):
    class Config:
        extra = "forbid"

    limits: List[LimitRangeItem] = Field(
        ...,
        description="Limits is the list of LimitRangeItem objects that are enforced.",
    )


class LoadBalancerIngress(BaseModel):
    class Config:
        extra = "forbid"

    hostname: Optional[str] = Field(
        None,
        description="Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers)",
    )
    ip: Optional[str] = Field(
        None,
        description="IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers)",
    )


class LoadBalancerStatus(BaseModel):
    class Config:
        extra = "forbid"

    ingress: Optional[List[LoadBalancerIngress]] = Field(
        None,
        description="Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points.",
    )


class LocalObjectReference(BaseModel):
    class Config:
        extra = "forbid"

    name: Optional[str] = Field(
        None,
        description="Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names",
    )


class LocalVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    fsType: Optional[str] = Field(
        None,
        description='Filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default value is to auto-select a fileystem if unspecified.',
    )
    path: str = Field(
        ...,
        description="The full path to the volume on the node. It can be either a directory or block device (disk, partition, ...).",
    )


class NFSVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    path: str = Field(
        ...,
        description="Path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs",
    )
    readOnly: Optional[bool] = Field(
        None,
        description="ReadOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs",
    )
    server: str = Field(
        ...,
        description="Server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs",
    )


class NamespaceSpec(BaseModel):
    class Config:
        extra = "forbid"

    finalizers: Optional[List[str]] = Field(
        None,
        description="Finalizers is an opaque list of values that must be empty to permanently remove object from storage. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/",
    )


class NodeAddress(BaseModel):
    class Config:
        extra = "forbid"

    address: str = Field(..., description="The node address.")
    type: str = Field(
        ..., description="Node address type, one of Hostname, ExternalIP or InternalIP."
    )


class NodeConfigSource(BaseModel):
    class Config:
        extra = "forbid"

    configMap: Optional[ConfigMapNodeConfigSource] = Field(
        None, description="ConfigMap is a reference to a Node's ConfigMap"
    )


class NodeConfigStatus(BaseModel):
    class Config:
        extra = "forbid"

    active: Optional[NodeConfigSource] = Field(
        None,
        description="Active reports the checkpointed config the node is actively using. Active will represent either the current version of the Assigned config, or the current LastKnownGood config, depending on whether attempting to use the Assigned config results in an error.",
    )
    assigned: Optional[NodeConfigSource] = Field(
        None,
        description="Assigned reports the checkpointed config the node will try to use. When Node.Spec.ConfigSource is updated, the node checkpoints the associated config payload to local disk, along with a record indicating intended config. The node refers to this record to choose its config checkpoint, and reports this record in Assigned. Assigned only updates in the status after the record has been checkpointed to disk. When the Kubelet is restarted, it tries to make the Assigned config the Active config by loading and validating the checkpointed payload identified by Assigned.",
    )
    error: Optional[str] = Field(
        None,
        description="Error describes any problems reconciling the Spec.ConfigSource to the Active config. Errors may occur, for example, attempting to checkpoint Spec.ConfigSource to the local Assigned record, attempting to checkpoint the payload associated with Spec.ConfigSource, attempting to load or validate the Assigned config, etc. Errors may occur at different points while syncing config. Earlier errors (e.g. download or checkpointing errors) will not result in a rollback to LastKnownGood, and may resolve across Kubelet retries. Later errors (e.g. loading or validating a checkpointed config) will result in a rollback to LastKnownGood. In the latter case, it is usually possible to resolve the error by fixing the config assigned in Spec.ConfigSource. You can find additional information for debugging by searching the error message in the Kubelet log. Error is a human-readable description of the error state; machines can check whether or not Error is empty, but should not rely on the stability of the Error text across Kubelet versions.",
    )
    lastKnownGood: Optional[NodeConfigSource] = Field(
        None,
        description="LastKnownGood reports the checkpointed config the node will fall back to when it encounters an error attempting to use the Assigned config. The Assigned config becomes the LastKnownGood config when the node determines that the Assigned config is stable and correct. This is currently implemented as a 10-minute soak period starting when the local record of Assigned config is updated. If the Assigned config is Active at the end of this period, it becomes the LastKnownGood. Note that if Spec.ConfigSource is reset to nil (use local defaults), the LastKnownGood is also immediately reset to nil, because the local default config is always assumed good. You should not make assumptions about the node's method of determining config stability and correctness, as this may change or become configurable in the future.",
    )


class NodeDaemonEndpoints(BaseModel):
    class Config:
        extra = "forbid"

    kubeletEndpoint: Optional[DaemonEndpoint] = Field(
        None, description="Endpoint on which Kubelet is listening."
    )


class NodeSelectorRequirement(BaseModel):
    class Config:
        extra = "forbid"

    key: str = Field(..., description="The label key that the selector applies to.")
    operator: str = Field(
        ...,
        description="Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.",
    )
    values: Optional[List[str]] = Field(
        None,
        description="An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.",
    )


class NodeSelectorTerm(BaseModel):
    class Config:
        extra = "forbid"

    matchExpressions: Optional[List[NodeSelectorRequirement]] = Field(
        None, description="A list of node selector requirements by node's labels."
    )
    matchFields: Optional[List[NodeSelectorRequirement]] = Field(
        None, description="A list of node selector requirements by node's fields."
    )


class NodeSystemInfo(BaseModel):
    class Config:
        extra = "forbid"

    architecture: str = Field(..., description="The Architecture reported by the node")
    bootID: str = Field(..., description="Boot ID reported by the node.")
    containerRuntimeVersion: str = Field(
        ...,
        description="ContainerRuntime Version reported by the node through runtime remote API (e.g. docker://1.5.0).",
    )
    kernelVersion: str = Field(
        ...,
        description="Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).",
    )
    kubeProxyVersion: str = Field(
        ..., description="KubeProxy Version reported by the node."
    )
    kubeletVersion: str = Field(
        ..., description="Kubelet Version reported by the node."
    )
    machineID: str = Field(
        ...,
        description="MachineID reported by the node. For unique machine identification in the cluster this field is preferred. Learn more from man(5) machine-id: http://man7.org/linux/man-pages/man5/machine-id.5.html",
    )
    operatingSystem: str = Field(
        ..., description="The Operating System reported by the node"
    )
    osImage: str = Field(
        ...,
        description="OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).",
    )
    systemUUID: str = Field(
        ...,
        description="SystemUUID reported by the node. For unique machine identification MachineID is preferred. This field is specific to Red Hat hosts https://access.redhat.com/documentation/en-US/Red_Hat_Subscription_Management/1/html/RHSM/getting-system-uuid.html",
    )


class ObjectFieldSelector(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description='Version of the schema the FieldPath is written in terms of, defaults to "v1".',
    )
    fieldPath: str = Field(
        ..., description="Path of the field to select in the specified API version."
    )


class ObjectReference(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field("v1", description="API version of the referent.")
    fieldPath: Optional[str] = Field(
        None,
        description='If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.',
    )
    kind: Optional[str] = Field(
        None,
        description="Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    name: Optional[str] = Field(
        None,
        description="Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names",
    )
    namespace: Optional[str] = Field(
        None,
        description="Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/",
    )
    resourceVersion: Optional[str] = Field(
        None,
        description="Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency",
    )
    uid: Optional[str] = Field(
        None,
        description="UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids",
    )


class PersistentVolumeClaimVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    claimName: str = Field(
        ...,
        description="ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims",
    )
    readOnly: Optional[bool] = Field(
        None,
        description="Will force the ReadOnly setting in VolumeMounts. Default false.",
    )


class PersistentVolumeStatus(BaseModel):
    class Config:
        extra = "forbid"

    message: Optional[str] = Field(
        None,
        description="A human-readable message indicating details about why the volume is in this state.",
    )
    phase: Optional[str] = Field(
        None,
        description="Phase indicates if a volume is available, bound to a claim, or released by a claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase",
    )
    reason: Optional[str] = Field(
        None,
        description="Reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI.",
    )


class PhotonPersistentDiskVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    fsType: Optional[str] = Field(
        None,
        description='Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.',
    )
    pdID: str = Field(
        ..., description="ID that identifies Photon Controller persistent disk"
    )


class PodDNSConfigOption(BaseModel):
    class Config:
        extra = "forbid"

    name: Optional[str] = Field(None, description="Required.")
    value: Optional[str] = None


class PodIP(BaseModel):
    class Config:
        extra = "forbid"

    ip: Optional[str] = Field(
        None, description="ip is an IP address (IPv4 or IPv6) assigned to the pod"
    )


class PodReadinessGate(BaseModel):
    class Config:
        extra = "forbid"

    conditionType: str = Field(
        ...,
        description="ConditionType refers to a condition in the pod's condition list with matching type.",
    )


class PortworxVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    fsType: Optional[str] = Field(
        None,
        description='FSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.',
    )
    readOnly: Optional[bool] = Field(
        None,
        description="Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.",
    )
    volumeID: str = Field(
        ..., description="VolumeID uniquely identifies a Portworx volume"
    )


class PreferredSchedulingTerm(BaseModel):
    class Config:
        extra = "forbid"

    preference: NodeSelectorTerm = Field(
        ...,
        description="A node selector term, associated with the corresponding weight.",
    )
    weight: int = Field(
        ...,
        description="Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.",
    )


class QuobyteVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    group: Optional[str] = Field(
        None, description="Group to map volume access to Default is no group"
    )
    readOnly: Optional[bool] = Field(
        None,
        description="ReadOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.",
    )
    registry: str = Field(
        ...,
        description="Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes",
    )
    tenant: Optional[str] = Field(
        None,
        description="Tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin",
    )
    user: Optional[str] = Field(
        None, description="User to map volume access to Defaults to serivceaccount user"
    )
    volume: str = Field(
        ...,
        description="Volume is a string that references an already created Quobyte volume by name.",
    )


class RBDVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    fsType: Optional[str] = Field(
        None,
        description='Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd',
    )
    image: str = Field(
        ...,
        description="The rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it",
    )
    keyring: Optional[str] = Field(
        None,
        description="Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it",
    )
    monitors: List[str] = Field(
        ...,
        description="A collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it",
    )
    pool: Optional[str] = Field(
        None,
        description="The rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it",
    )
    readOnly: Optional[bool] = Field(
        None,
        description="ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it",
    )
    secretRef: Optional[LocalObjectReference] = Field(
        None,
        description="SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it",
    )
    user: Optional[str] = Field(
        None,
        description="The rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it",
    )


class ResourceQuotaStatus(BaseModel):
    class Config:
        extra = "forbid"

    hard: Optional[Dict[str, Any]] = Field(
        None,
        description="Hard is the set of enforced hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/",
    )
    used: Optional[Dict[str, Any]] = Field(
        None,
        description="Used is the current observed total usage of the resource in the namespace.",
    )


class ResourceRequirements(BaseModel):
    class Config:
        extra = "forbid"

    limits: Optional[Dict[str, Any]] = Field(
        None,
        description="Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/",
    )
    requests: Optional[Dict[str, Any]] = Field(
        None,
        description="Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/",
    )


class SELinuxOptions(BaseModel):
    class Config:
        extra = "forbid"

    level: Optional[str] = Field(
        None, description="Level is SELinux level label that applies to the container."
    )
    role: Optional[str] = Field(
        None, description="Role is a SELinux role label that applies to the container."
    )
    type: Optional[str] = Field(
        None, description="Type is a SELinux type label that applies to the container."
    )
    user: Optional[str] = Field(
        None, description="User is a SELinux user label that applies to the container."
    )


class ScaleIOVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    fsType: Optional[str] = Field(
        None,
        description='Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs".',
    )
    gateway: str = Field(
        ..., description="The host address of the ScaleIO API Gateway."
    )
    protectionDomain: Optional[str] = Field(
        None,
        description="The name of the ScaleIO Protection Domain for the configured storage.",
    )
    readOnly: Optional[bool] = Field(
        None,
        description="Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.",
    )
    secretRef: LocalObjectReference = Field(
        ...,
        description="SecretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.",
    )
    sslEnabled: Optional[bool] = Field(
        None,
        description="Flag to enable/disable SSL communication with Gateway, default false",
    )
    storageMode: Optional[str] = Field(
        None,
        description="Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.",
    )
    storagePool: Optional[str] = Field(
        None,
        description="The ScaleIO Storage Pool associated with the protection domain.",
    )
    system: str = Field(
        ..., description="The name of the storage system as configured in ScaleIO."
    )
    volumeName: Optional[str] = Field(
        None,
        description="The name of a volume already created in the ScaleIO system that is associated with this volume source.",
    )


class ScopedResourceSelectorRequirement(BaseModel):
    class Config:
        extra = "forbid"

    operator: str = Field(
        ...,
        description="Represents a scope's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist.",
    )
    scopeName: str = Field(
        ..., description="The name of the scope that the selector applies to."
    )
    values: Optional[List[str]] = Field(
        None,
        description="An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.",
    )


class SecretEnvSource(BaseModel):
    class Config:
        extra = "forbid"

    name: Optional[str] = Field(
        None,
        description="Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names",
    )
    optional: Optional[bool] = Field(
        None, description="Specify whether the Secret must be defined"
    )


class SecretKeySelector(BaseModel):
    class Config:
        extra = "forbid"

    key: str = Field(
        ...,
        description="The key of the secret to select from.  Must be a valid secret key.",
    )
    name: Optional[str] = Field(
        None,
        description="Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names",
    )
    optional: Optional[bool] = Field(
        None, description="Specify whether the Secret or its key must be defined"
    )


class SecretProjection(BaseModel):
    class Config:
        extra = "forbid"

    items: Optional[List[KeyToPath]] = Field(
        None,
        description="If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.",
    )
    name: Optional[str] = Field(
        None,
        description="Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names",
    )
    optional: Optional[bool] = Field(
        None, description="Specify whether the Secret or its key must be defined"
    )


class SecretReference(BaseModel):
    class Config:
        extra = "forbid"

    name: Optional[str] = Field(
        None,
        description="Name is unique within a namespace to reference a secret resource.",
    )
    namespace: Optional[str] = Field(
        None,
        description="Namespace defines the space within which the secret name must be unique.",
    )


class SecretVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    defaultMode: Optional[int] = Field(
        None,
        description="Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.",
    )
    items: Optional[List[KeyToPath]] = Field(
        None,
        description="If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.",
    )
    optional: Optional[bool] = Field(
        None, description="Specify whether the Secret or its keys must be defined"
    )
    secretName: Optional[str] = Field(
        None,
        description="Name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret",
    )


class ServiceAccountTokenProjection(BaseModel):
    class Config:
        extra = "forbid"

    audience: Optional[str] = Field(
        None,
        description="Audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.",
    )
    expirationSeconds: Optional[int] = Field(
        None,
        description="ExpirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.",
    )
    path: str = Field(
        ...,
        description="Path is the path relative to the mount point of the file to project the token into.",
    )


class ServiceStatus(BaseModel):
    class Config:
        extra = "forbid"

    loadBalancer: Optional[LoadBalancerStatus] = Field(
        None,
        description="LoadBalancer contains the current status of the load-balancer, if one is present.",
    )


class SessionAffinityConfig(BaseModel):
    class Config:
        extra = "forbid"

    clientIP: Optional[ClientIPConfig] = Field(
        None,
        description="clientIP contains the configurations of Client IP based session affinity.",
    )


class StorageOSPersistentVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    fsType: Optional[str] = Field(
        None,
        description='Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.',
    )
    readOnly: Optional[bool] = Field(
        None,
        description="Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.",
    )
    secretRef: Optional[ObjectReference] = Field(
        None,
        description="SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.",
    )
    volumeName: Optional[str] = Field(
        None,
        description="VolumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.",
    )
    volumeNamespace: Optional[str] = Field(
        None,
        description='VolumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod\'s namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.',
    )


class StorageOSVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    fsType: Optional[str] = Field(
        None,
        description='Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.',
    )
    readOnly: Optional[bool] = Field(
        None,
        description="Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.",
    )
    secretRef: Optional[LocalObjectReference] = Field(
        None,
        description="SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.",
    )
    volumeName: Optional[str] = Field(
        None,
        description="VolumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.",
    )
    volumeNamespace: Optional[str] = Field(
        None,
        description='VolumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod\'s namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.',
    )


class Sysctl(BaseModel):
    class Config:
        extra = "forbid"

    name: str = Field(..., description="Name of a property to set")
    value: str = Field(..., description="Value of a property to set")


class Toleration(BaseModel):
    class Config:
        extra = "forbid"

    effect: Optional[str] = Field(
        None,
        description="Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.",
    )
    key: Optional[str] = Field(
        None,
        description="Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.",
    )
    operator: Optional[str] = Field(
        None,
        description="Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.",
    )
    tolerationSeconds: Optional[int] = Field(
        None,
        description="TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.",
    )
    value: Optional[str] = Field(
        None,
        description="Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.",
    )


class TopologySelectorLabelRequirement(BaseModel):
    class Config:
        extra = "forbid"

    key: str = Field(..., description="The label key that the selector applies to.")
    values: List[str] = Field(
        ...,
        description="An array of string values. One value must match the label to be selected. Each entry in Values is ORed.",
    )


class TopologySelectorTerm(BaseModel):
    class Config:
        extra = "forbid"

    matchLabelExpressions: Optional[List[TopologySelectorLabelRequirement]] = Field(
        None, description="A list of topology selector requirements by labels."
    )


class TypedLocalObjectReference(BaseModel):
    class Config:
        extra = "forbid"

    apiGroup: Optional[str] = Field(
        None,
        description="APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.",
    )
    kind: str = Field(..., description="Kind is the type of resource being referenced")
    name: str = Field(..., description="Name is the name of resource being referenced")


class VolumeDevice(BaseModel):
    class Config:
        extra = "forbid"

    devicePath: str = Field(
        ...,
        description="devicePath is the path inside of the container that the device will be mapped to.",
    )
    name: str = Field(
        ...,
        description="name must match the name of a persistentVolumeClaim in the pod",
    )


class VolumeMount(BaseModel):
    class Config:
        extra = "forbid"

    mountPath: str = Field(
        ...,
        description="Path within the container at which the volume should be mounted.  Must not contain ':'.",
    )
    mountPropagation: Optional[str] = Field(
        None,
        description="mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10.",
    )
    name: str = Field(..., description="This must match the Name of a Volume.")
    readOnly: Optional[bool] = Field(
        None,
        description="Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.",
    )
    subPath: Optional[str] = Field(
        None,
        description="Path within the volume from which the container's volume should be mounted. Defaults to \"\" (volume's root).",
    )
    subPathExpr: Optional[str] = Field(
        None,
        description="Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to \"\" (volume's root). SubPathExpr and SubPath are mutually exclusive. This field is beta in 1.15.",
    )


class VsphereVirtualDiskVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    fsType: Optional[str] = Field(
        None,
        description='Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.',
    )
    storagePolicyID: Optional[str] = Field(
        None,
        description="Storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.",
    )
    storagePolicyName: Optional[str] = Field(
        None, description="Storage Policy Based Management (SPBM) profile name."
    )
    volumePath: str = Field(..., description="Path that identifies vSphere volume vmdk")


class WindowsSecurityContextOptions(BaseModel):
    class Config:
        extra = "forbid"

    gmsaCredentialSpec: Optional[str] = Field(
        None,
        description="GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.",
    )
    gmsaCredentialSpecName: Optional[str] = Field(
        None,
        description="GMSACredentialSpecName is the name of the GMSA credential spec to use. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.",
    )
    runAsUserName: Optional[str] = Field(
        None,
        description="The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. This field is alpha-level and it is only honored by servers that enable the WindowsRunAsUserName feature flag.",
    )


class CSIPersistentVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    controllerExpandSecretRef: Optional[SecretReference] = Field(
        None,
        description="ControllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This is an alpha field and requires enabling ExpandCSIVolumes feature gate. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.",
    )
    controllerPublishSecretRef: Optional[SecretReference] = Field(
        None,
        description="ControllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.",
    )
    driver: str = Field(
        ...,
        description="Driver is the name of the driver to use for this volume. Required.",
    )
    fsType: Optional[str] = Field(
        None,
        description='Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs".',
    )
    nodePublishSecretRef: Optional[SecretReference] = Field(
        None,
        description="NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.",
    )
    nodeStageSecretRef: Optional[SecretReference] = Field(
        None,
        description="NodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.",
    )
    readOnly: Optional[bool] = Field(
        None,
        description="Optional: The value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write).",
    )
    volumeAttributes: Optional[Dict[str, Any]] = Field(
        None, description="Attributes of the volume to publish."
    )
    volumeHandle: str = Field(
        ...,
        description="VolumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required.",
    )


class CSIVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    driver: str = Field(
        ...,
        description="Driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster.",
    )
    fsType: Optional[str] = Field(
        None,
        description='Filesystem type to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply.',
    )
    nodePublishSecretRef: Optional[LocalObjectReference] = Field(
        None,
        description="NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.",
    )
    readOnly: Optional[bool] = Field(
        None,
        description="Specifies a read-only configuration for the volume. Defaults to false (read/write).",
    )
    volumeAttributes: Optional[Dict[str, Any]] = Field(
        None,
        description="VolumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values.",
    )


class CephFSPersistentVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    monitors: List[str] = Field(
        ...,
        description="Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it",
    )
    path: Optional[str] = Field(
        None,
        description="Optional: Used as the mounted root, rather than the full Ceph tree, default is /",
    )
    readOnly: Optional[bool] = Field(
        None,
        description="Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it",
    )
    secretFile: Optional[str] = Field(
        None,
        description="Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it",
    )
    secretRef: Optional[SecretReference] = Field(
        None,
        description="Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it",
    )
    user: Optional[str] = Field(
        None,
        description="Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it",
    )


class CephFSVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    monitors: List[str] = Field(
        ...,
        description="Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it",
    )
    path: Optional[str] = Field(
        None,
        description="Optional: Used as the mounted root, rather than the full Ceph tree, default is /",
    )
    readOnly: Optional[bool] = Field(
        None,
        description="Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it",
    )
    secretFile: Optional[str] = Field(
        None,
        description="Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it",
    )
    secretRef: Optional[LocalObjectReference] = Field(
        None,
        description="Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it",
    )
    user: Optional[str] = Field(
        None,
        description="Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it",
    )


class CinderPersistentVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    fsType: Optional[str] = Field(
        None,
        description='Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md',
    )
    readOnly: Optional[bool] = Field(
        None,
        description="Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md",
    )
    secretRef: Optional[SecretReference] = Field(
        None,
        description="Optional: points to a secret object containing parameters used to connect to OpenStack.",
    )
    volumeID: str = Field(
        ...,
        description="volume id used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md",
    )


class CinderVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    fsType: Optional[str] = Field(
        None,
        description='Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md',
    )
    readOnly: Optional[bool] = Field(
        None,
        description="Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md",
    )
    secretRef: Optional[LocalObjectReference] = Field(
        None,
        description="Optional: points to a secret object containing parameters used to connect to OpenStack.",
    )
    volumeID: str = Field(
        ...,
        description="volume id used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md",
    )


class ConfigMapProjection(BaseModel):
    class Config:
        extra = "forbid"

    items: Optional[List[KeyToPath]] = Field(
        None,
        description="If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.",
    )
    name: Optional[str] = Field(
        None,
        description="Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names",
    )
    optional: Optional[bool] = Field(
        None, description="Specify whether the ConfigMap or its keys must be defined"
    )


class ConfigMapVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    defaultMode: Optional[int] = Field(
        None,
        description="Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.",
    )
    items: Optional[List[KeyToPath]] = Field(
        None,
        description="If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.",
    )
    name: Optional[str] = Field(
        None,
        description="Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names",
    )
    optional: Optional[bool] = Field(
        None, description="Specify whether the ConfigMap or its keys must be defined"
    )


class ContainerStateRunning(BaseModel):
    class Config:
        extra = "forbid"

    startedAt: Optional[v1.Time] = Field(
        None, description="Time at which the container was last (re-)started"
    )


class ContainerStateTerminated(BaseModel):
    class Config:
        extra = "forbid"

    containerID: Optional[str] = Field(
        None, description="Container's ID in the format 'docker://<container_id>'"
    )
    exitCode: int = Field(
        ..., description="Exit status from the last termination of the container"
    )
    finishedAt: Optional[v1.Time] = Field(
        None, description="Time at which the container last terminated"
    )
    message: Optional[str] = Field(
        None, description="Message regarding the last termination of the container"
    )
    reason: Optional[str] = Field(
        None, description="(brief) reason from the last termination of the container"
    )
    signal: Optional[int] = Field(
        None, description="Signal from the last termination of the container"
    )
    startedAt: Optional[v1.Time] = Field(
        None, description="Time at which previous execution of the container started"
    )


class EmptyDirVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    medium: Optional[str] = Field(
        None,
        description='What type of storage medium should back this directory. The default is "" which means to use the node\'s default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir',
    )
    sizeLimit: Optional[resource.Quantity] = Field(
        None,
        description="Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir",
    )


class EndpointAddress(BaseModel):
    class Config:
        extra = "forbid"

    hostname: Optional[str] = Field(None, description="The Hostname of this endpoint")
    ip: str = Field(
        ...,
        description="The IP of this endpoint. May not be loopback (127.0.0.0/8), link-local (169.254.0.0/16), or link-local multicast ((224.0.0.0/24). IPv6 is also accepted but not fully supported on all platforms. Also, certain kubernetes components, like kube-proxy, are not IPv6 ready.",
    )
    nodeName: Optional[str] = Field(
        None,
        description="Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node.",
    )
    targetRef: Optional[ObjectReference] = Field(
        None, description="Reference to object providing the endpoint."
    )


class EndpointSubset(BaseModel):
    class Config:
        extra = "forbid"

    addresses: Optional[List[EndpointAddress]] = Field(
        None,
        description="IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize.",
    )
    notReadyAddresses: Optional[List[EndpointAddress]] = Field(
        None,
        description="IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check.",
    )
    ports: Optional[List[EndpointPort]] = Field(
        None, description="Port numbers available on the related IP addresses."
    )


class EnvFromSource(BaseModel):
    class Config:
        extra = "forbid"

    configMapRef: Optional[ConfigMapEnvSource] = Field(
        None, description="The ConfigMap to select from"
    )
    prefix: Optional[str] = Field(
        None,
        description="An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.",
    )
    secretRef: Optional[SecretEnvSource] = Field(
        None, description="The Secret to select from"
    )


class EventSeries(BaseModel):
    class Config:
        extra = "forbid"

    count: Optional[int] = Field(
        None,
        description="Number of occurrences in this series up to the last heartbeat time",
    )
    lastObservedTime: Optional[v1.MicroTime] = Field(
        None, description="Time of the last occurrence observed"
    )
    state: Optional[str] = Field(
        None,
        description="State of this Series: Ongoing or Finished Deprecated. Planned removal for 1.18",
    )


class FlexPersistentVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    driver: str = Field(
        ..., description="Driver is the name of the driver to use for this volume."
    )
    fsType: Optional[str] = Field(
        None,
        description='Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.',
    )
    options: Optional[Dict[str, Any]] = Field(
        None, description="Optional: Extra command options if any."
    )
    readOnly: Optional[bool] = Field(
        None,
        description="Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.",
    )
    secretRef: Optional[SecretReference] = Field(
        None,
        description="Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.",
    )


class FlexVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    driver: str = Field(
        ..., description="Driver is the name of the driver to use for this volume."
    )
    fsType: Optional[str] = Field(
        None,
        description='Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.',
    )
    options: Optional[Dict[str, Any]] = Field(
        None, description="Optional: Extra command options if any."
    )
    readOnly: Optional[bool] = Field(
        None,
        description="Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.",
    )
    secretRef: Optional[LocalObjectReference] = Field(
        None,
        description="Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.",
    )


class HTTPGetAction(BaseModel):
    class Config:
        extra = "forbid"

    host: Optional[str] = Field(
        None,
        description='Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.',
    )
    httpHeaders: Optional[List[HTTPHeader]] = Field(
        None,
        description="Custom headers to set in the request. HTTP allows repeated headers.",
    )
    path: Optional[str] = Field(None, description="Path to access on the HTTP server.")
    port: intstr.IntOrString = Field(
        ...,
        description="Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.",
    )
    scheme: Optional[str] = Field(
        None, description="Scheme to use for connecting to the host. Defaults to HTTP."
    )


class ISCSIPersistentVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    chapAuthDiscovery: Optional[bool] = Field(
        None, description="whether support iSCSI Discovery CHAP authentication"
    )
    chapAuthSession: Optional[bool] = Field(
        None, description="whether support iSCSI Session CHAP authentication"
    )
    fsType: Optional[str] = Field(
        None,
        description='Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi',
    )
    initiatorName: Optional[str] = Field(
        None,
        description="Custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.",
    )
    iqn: str = Field(..., description="Target iSCSI Qualified Name.")
    iscsiInterface: Optional[str] = Field(
        None,
        description="iSCSI Interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).",
    )
    lun: int = Field(..., description="iSCSI Target Lun number.")
    portals: Optional[List[str]] = Field(
        None,
        description="iSCSI Target Portal List. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).",
    )
    readOnly: Optional[bool] = Field(
        None,
        description="ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.",
    )
    secretRef: Optional[SecretReference] = Field(
        None, description="CHAP Secret for iSCSI target and initiator authentication"
    )
    targetPortal: str = Field(
        ...,
        description="iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).",
    )


class ISCSIVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    chapAuthDiscovery: Optional[bool] = Field(
        None, description="whether support iSCSI Discovery CHAP authentication"
    )
    chapAuthSession: Optional[bool] = Field(
        None, description="whether support iSCSI Session CHAP authentication"
    )
    fsType: Optional[str] = Field(
        None,
        description='Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi',
    )
    initiatorName: Optional[str] = Field(
        None,
        description="Custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.",
    )
    iqn: str = Field(..., description="Target iSCSI Qualified Name.")
    iscsiInterface: Optional[str] = Field(
        None,
        description="iSCSI Interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).",
    )
    lun: int = Field(..., description="iSCSI Target Lun number.")
    portals: Optional[List[str]] = Field(
        None,
        description="iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).",
    )
    readOnly: Optional[bool] = Field(
        None,
        description="ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.",
    )
    secretRef: Optional[LocalObjectReference] = Field(
        None, description="CHAP Secret for iSCSI target and initiator authentication"
    )
    targetPortal: str = Field(
        ...,
        description="iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).",
    )


class NamespaceCondition(BaseModel):
    class Config:
        extra = "forbid"

    lastTransitionTime: Optional[v1.Time] = None
    message: Optional[str] = None
    reason: Optional[str] = None
    status: str = Field(
        ..., description="Status of the condition, one of True, False, Unknown."
    )
    type: str = Field(..., description="Type of namespace controller condition.")


class NamespaceStatus(BaseModel):
    class Config:
        extra = "forbid"

    conditions: Optional[List[NamespaceCondition]] = Field(
        None,
        description="Represents the latest available observations of a namespace's current state.",
    )
    phase: Optional[str] = Field(
        None,
        description="Phase is the current lifecycle phase of the namespace. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/",
    )


class NodeCondition(BaseModel):
    class Config:
        extra = "forbid"

    lastHeartbeatTime: Optional[v1.Time] = Field(
        None, description="Last time we got an update on a given condition."
    )
    lastTransitionTime: Optional[v1.Time] = Field(
        None, description="Last time the condition transit from one status to another."
    )
    message: Optional[str] = Field(
        None,
        description="Human readable message indicating details about last transition.",
    )
    reason: Optional[str] = Field(
        None, description="(brief) reason for the condition's last transition."
    )
    status: str = Field(
        ..., description="Status of the condition, one of True, False, Unknown."
    )
    type: str = Field(..., description="Type of node condition.")


class NodeSelector(BaseModel):
    class Config:
        extra = "forbid"

    nodeSelectorTerms: List[NodeSelectorTerm] = Field(
        ..., description="Required. A list of node selector terms. The terms are ORed."
    )


class NodeStatus(BaseModel):
    class Config:
        extra = "forbid"

    addresses: Optional[List[NodeAddress]] = Field(
        None,
        description="List of addresses reachable to the node. Queried from cloud provider, if available. More info: https://kubernetes.io/docs/concepts/nodes/node/#addresses Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See http://pr.k8s.io/79391 for an example.",
    )
    allocatable: Optional[Dict[str, Any]] = Field(
        None,
        description="Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity.",
    )
    capacity: Optional[Dict[str, Any]] = Field(
        None,
        description="Capacity represents the total resources of a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity",
    )
    conditions: Optional[List[NodeCondition]] = Field(
        None,
        description="Conditions is an array of current observed node conditions. More info: https://kubernetes.io/docs/concepts/nodes/node/#condition",
    )
    config: Optional[NodeConfigStatus] = Field(
        None,
        description="Status of the config assigned to the node via the dynamic Kubelet config feature.",
    )
    daemonEndpoints: Optional[NodeDaemonEndpoints] = Field(
        None, description="Endpoints of daemons running on the Node."
    )
    images: Optional[List[ContainerImage]] = Field(
        None, description="List of container images on this node"
    )
    nodeInfo: Optional[NodeSystemInfo] = Field(
        None,
        description="Set of ids/uuids to uniquely identify the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#info",
    )
    phase: Optional[str] = Field(
        None,
        description="NodePhase is the recently observed lifecycle phase of the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#phase The field is never populated, and now is deprecated.",
    )
    volumesAttached: Optional[List[AttachedVolume]] = Field(
        None, description="List of volumes that are attached to the node."
    )
    volumesInUse: Optional[List[str]] = Field(
        None, description="List of attachable volumes in use (mounted) by the node."
    )


class PersistentVolumeClaimCondition(BaseModel):
    class Config:
        extra = "forbid"

    lastProbeTime: Optional[v1.Time] = Field(
        None, description="Last time we probed the condition."
    )
    lastTransitionTime: Optional[v1.Time] = Field(
        None,
        description="Last time the condition transitioned from one status to another.",
    )
    message: Optional[str] = Field(
        None,
        description="Human-readable message indicating details about last transition.",
    )
    reason: Optional[str] = Field(
        None,
        description='Unique, this should be a short, machine understandable string that gives the reason for condition\'s last transition. If it reports "ResizeStarted" that means the underlying persistent volume is being resized.',
    )
    status: str
    type: str


class PersistentVolumeClaimStatus(BaseModel):
    class Config:
        extra = "forbid"

    accessModes: Optional[List[str]] = Field(
        None,
        description="AccessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1",
    )
    capacity: Optional[Dict[str, Any]] = Field(
        None, description="Represents the actual resources of the underlying volume."
    )
    conditions: Optional[List[PersistentVolumeClaimCondition]] = Field(
        None,
        description="Current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'.",
    )
    phase: Optional[str] = Field(
        None, description="Phase represents the current phase of PersistentVolumeClaim."
    )


class PodCondition(BaseModel):
    class Config:
        extra = "forbid"

    lastProbeTime: Optional[v1.Time] = Field(
        None, description="Last time we probed the condition."
    )
    lastTransitionTime: Optional[v1.Time] = Field(
        None,
        description="Last time the condition transitioned from one status to another.",
    )
    message: Optional[str] = Field(
        None,
        description="Human-readable message indicating details about last transition.",
    )
    reason: Optional[str] = Field(
        None,
        description="Unique, one-word, CamelCase reason for the condition's last transition.",
    )
    status: str = Field(
        ...,
        description="Status is the status of the condition. Can be True, False, Unknown. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions",
    )
    type: str = Field(
        ...,
        description="Type is the type of the condition. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions",
    )


class PodDNSConfig(BaseModel):
    class Config:
        extra = "forbid"

    nameservers: Optional[List[str]] = Field(
        None,
        description="A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed.",
    )
    options: Optional[List[PodDNSConfigOption]] = Field(
        None,
        description="A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy.",
    )
    searches: Optional[List[str]] = Field(
        None,
        description="A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed.",
    )


class PodSecurityContext(BaseModel):
    class Config:
        extra = "forbid"

    fsGroup: Optional[int] = Field(
        None,
        description="A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:\n\n1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw----\n\nIf unset, the Kubelet will not modify the ownership and permissions of any volume.",
    )
    runAsGroup: Optional[int] = Field(
        None,
        description="The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.",
    )
    runAsNonRoot: Optional[bool] = Field(
        None,
        description="Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.",
    )
    runAsUser: Optional[int] = Field(
        None,
        description="The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.",
    )
    seLinuxOptions: Optional[SELinuxOptions] = Field(
        None,
        description="The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.",
    )
    supplementalGroups: Optional[List[int]] = Field(
        None,
        description="A list of groups applied to the first process run in each container, in addition to the container's primary GID.  If unspecified, no groups will be added to any container.",
    )
    sysctls: Optional[List[Sysctl]] = Field(
        None,
        description="Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch.",
    )
    windowsOptions: Optional[WindowsSecurityContextOptions] = Field(
        None,
        description="The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.",
    )


class RBDPersistentVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    fsType: Optional[str] = Field(
        None,
        description='Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd',
    )
    image: str = Field(
        ...,
        description="The rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it",
    )
    keyring: Optional[str] = Field(
        None,
        description="Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it",
    )
    monitors: List[str] = Field(
        ...,
        description="A collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it",
    )
    pool: Optional[str] = Field(
        None,
        description="The rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it",
    )
    readOnly: Optional[bool] = Field(
        None,
        description="ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it",
    )
    secretRef: Optional[SecretReference] = Field(
        None,
        description="SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it",
    )
    user: Optional[str] = Field(
        None,
        description="The rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it",
    )


class ReplicationControllerCondition(BaseModel):
    class Config:
        extra = "forbid"

    lastTransitionTime: Optional[v1.Time] = Field(
        None,
        description="The last time the condition transitioned from one status to another.",
    )
    message: Optional[str] = Field(
        None,
        description="A human readable message indicating details about the transition.",
    )
    reason: Optional[str] = Field(
        None, description="The reason for the condition's last transition."
    )
    status: str = Field(
        ..., description="Status of the condition, one of True, False, Unknown."
    )
    type: str = Field(..., description="Type of replication controller condition.")


class ReplicationControllerStatus(BaseModel):
    class Config:
        extra = "forbid"

    availableReplicas: Optional[int] = Field(
        None,
        description="The number of available replicas (ready for at least minReadySeconds) for this replication controller.",
    )
    conditions: Optional[List[ReplicationControllerCondition]] = Field(
        None,
        description="Represents the latest available observations of a replication controller's current state.",
    )
    fullyLabeledReplicas: Optional[int] = Field(
        None,
        description="The number of pods that have labels matching the labels of the pod template of the replication controller.",
    )
    observedGeneration: Optional[int] = Field(
        None,
        description="ObservedGeneration reflects the generation of the most recently observed replication controller.",
    )
    readyReplicas: Optional[int] = Field(
        None,
        description="The number of ready replicas for this replication controller.",
    )
    replicas: int = Field(
        ...,
        description="Replicas is the most recently oberved number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller",
    )


class ResourceFieldSelector(BaseModel):
    class Config:
        extra = "forbid"

    containerName: Optional[str] = Field(
        None, description="Container name: required for volumes, optional for env vars"
    )
    divisor: Optional[resource.Quantity] = Field(
        None,
        description='Specifies the output format of the exposed resources, defaults to "1"',
    )
    resource: str = Field(..., description="Required: resource to select")


class ScaleIOPersistentVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    fsType: Optional[str] = Field(
        None,
        description='Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs"',
    )
    gateway: str = Field(
        ..., description="The host address of the ScaleIO API Gateway."
    )
    protectionDomain: Optional[str] = Field(
        None,
        description="The name of the ScaleIO Protection Domain for the configured storage.",
    )
    readOnly: Optional[bool] = Field(
        None,
        description="Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.",
    )
    secretRef: SecretReference = Field(
        ...,
        description="SecretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.",
    )
    sslEnabled: Optional[bool] = Field(
        None,
        description="Flag to enable/disable SSL communication with Gateway, default false",
    )
    storageMode: Optional[str] = Field(
        None,
        description="Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.",
    )
    storagePool: Optional[str] = Field(
        None,
        description="The ScaleIO Storage Pool associated with the protection domain.",
    )
    system: str = Field(
        ..., description="The name of the storage system as configured in ScaleIO."
    )
    volumeName: Optional[str] = Field(
        None,
        description="The name of a volume already created in the ScaleIO system that is associated with this volume source.",
    )


class ScopeSelector(BaseModel):
    class Config:
        extra = "forbid"

    matchExpressions: Optional[List[ScopedResourceSelectorRequirement]] = Field(
        None,
        description="A list of scope selector requirements by scope of the resources.",
    )


class SecurityContext(BaseModel):
    class Config:
        extra = "forbid"

    allowPrivilegeEscalation: Optional[bool] = Field(
        None,
        description="AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN",
    )
    capabilities: Optional[Capabilities] = Field(
        None,
        description="The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.",
    )
    privileged: Optional[bool] = Field(
        None,
        description="Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.",
    )
    procMount: Optional[str] = Field(
        None,
        description="procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled.",
    )
    readOnlyRootFilesystem: Optional[bool] = Field(
        None,
        description="Whether this container has a read-only root filesystem. Default is false.",
    )
    runAsGroup: Optional[int] = Field(
        None,
        description="The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.",
    )
    runAsNonRoot: Optional[bool] = Field(
        None,
        description="Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.",
    )
    runAsUser: Optional[int] = Field(
        None,
        description="The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.",
    )
    seLinuxOptions: Optional[SELinuxOptions] = Field(
        None,
        description="The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.",
    )
    windowsOptions: Optional[WindowsSecurityContextOptions] = Field(
        None,
        description="The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.",
    )


class ServicePort(BaseModel):
    class Config:
        extra = "forbid"

    name: Optional[str] = Field(
        None,
        description="The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. When considering the endpoints for a Service, this must match the 'name' field in the EndpointPort. Optional if only one ServicePort is defined on this service.",
    )
    nodePort: Optional[int] = Field(
        None,
        description="The port on each node on which this service is exposed when type=NodePort or LoadBalancer. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ServiceType of this Service requires one. More info: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport",
    )
    port: int = Field(..., description="The port that will be exposed by this service.")
    protocol: Optional[str] = Field(
        None,
        description='The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP.',
    )
    targetPort: Optional[intstr.IntOrString] = Field(
        None,
        description="Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field. More info: https://kubernetes.io/docs/concepts/services-networking/service/#defining-a-service",
    )


class ServiceSpec(BaseModel):
    class Config:
        extra = "forbid"

    clusterIP: Optional[str] = Field(
        None,
        description='clusterIP is the IP address of the service and is usually assigned randomly by the master. If an address is specified manually and is not in use by others, it will be allocated to the service; otherwise, creation of the service will fail. This field can not be changed through updates. Valid values are "None", empty string (""), or a valid IP address. "None" can be specified for headless services when proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies',
    )
    externalIPs: Optional[List[str]] = Field(
        None,
        description="externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system.",
    )
    externalName: Optional[str] = Field(
        None,
        description="externalName is the external reference that kubedns or equivalent will return as a CNAME record for this service. No proxying will be involved. Must be a valid RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires Type to be ExternalName.",
    )
    externalTrafficPolicy: Optional[str] = Field(
        None,
        description='externalTrafficPolicy denotes if this Service desires to route external traffic to node-local or cluster-wide endpoints. "Local" preserves the client source IP and avoids a second hop for LoadBalancer and Nodeport type services, but risks potentially imbalanced traffic spreading. "Cluster" obscures the client source IP and may cause a second hop to another node, but should have good overall load-spreading.',
    )
    healthCheckNodePort: Optional[int] = Field(
        None,
        description="healthCheckNodePort specifies the healthcheck nodePort for the service. If not specified, HealthCheckNodePort is created by the service api backend with the allocated nodePort. Will use user-specified nodePort value if specified by the client. Only effects when Type is set to LoadBalancer and ExternalTrafficPolicy is set to Local.",
    )
    ipFamily: Optional[str] = Field(
        None,
        description="ipFamily specifies whether this Service has a preference for a particular IP family (e.g. IPv4 vs. IPv6).  If a specific IP family is requested, the clusterIP field will be allocated from that family, if it is available in the cluster.  If no IP family is requested, the cluster's primary IP family will be used. Other IP fields (loadBalancerIP, loadBalancerSourceRanges, externalIPs) and controllers which allocate external load-balancers should use the same IP family.  Endpoints for this Service will be of this family.  This field is immutable after creation. Assigning a ServiceIPFamily not available in the cluster (e.g. IPv6 in IPv4 only cluster) is an error condition and will fail during clusterIP assignment.",
    )
    loadBalancerIP: Optional[str] = Field(
        None,
        description="Only applies to Service Type: LoadBalancer LoadBalancer will get created with the IP specified in this field. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature.",
    )
    loadBalancerSourceRanges: Optional[List[str]] = Field(
        None,
        description='If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature." More info: https://kubernetes.io/docs/tasks/access-application-cluster/configure-cloud-provider-firewall/',
    )
    ports: Optional[List[ServicePort]] = Field(
        None,
        description="The list of ports that are exposed by this service. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies",
    )
    publishNotReadyAddresses: Optional[bool] = Field(
        None,
        description="publishNotReadyAddresses, when set to true, indicates that DNS implementations must publish the notReadyAddresses of subsets for the Endpoints associated with the Service. The default value is false. The primary use case for setting this field is to use a StatefulSet's Headless Service to propagate SRV records for its Pods without respect to their readiness for purpose of peer discovery.",
    )
    selector: Optional[Dict[str, Any]] = Field(
        None,
        description="Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/",
    )
    sessionAffinity: Optional[str] = Field(
        None,
        description='Supports "ClientIP" and "None". Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies',
    )
    sessionAffinityConfig: Optional[SessionAffinityConfig] = Field(
        None,
        description="sessionAffinityConfig contains the configurations of session affinity.",
    )
    type: Optional[str] = Field(
        None,
        description='type determines how the Service is exposed. Defaults to ClusterIP. Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer. "ExternalName" maps to the specified externalName. "ClusterIP" allocates a cluster-internal IP address for load-balancing to endpoints. Endpoints are determined by the selector or if that is not specified, by manual construction of an Endpoints object. If clusterIP is "None", no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a stable IP. "NodePort" builds on ClusterIP and allocates a port on every node which routes to the clusterIP. "LoadBalancer" builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the clusterIP. More info: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types',
    )


class TCPSocketAction(BaseModel):
    class Config:
        extra = "forbid"

    host: Optional[str] = Field(
        None, description="Optional: Host name to connect to, defaults to the pod IP."
    )
    port: intstr.IntOrString = Field(
        ...,
        description="Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.",
    )


class Taint(BaseModel):
    class Config:
        extra = "forbid"

    effect: str = Field(
        ...,
        description="Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.",
    )
    key: str = Field(
        ..., description="Required. The taint key to be applied to a node."
    )
    timeAdded: Optional[v1.Time] = Field(
        None,
        description="TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.",
    )
    value: Optional[str] = Field(
        None, description="Required. The taint value corresponding to the taint key."
    )


class VolumeNodeAffinity(BaseModel):
    class Config:
        extra = "forbid"

    required: Optional[NodeSelector] = Field(
        None, description="Required specifies hard node constraints that must be met."
    )


class Binding(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind69] = Field(
        "Binding",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    target: ObjectReference = Field(
        ...,
        description="The target object that you want to bind to the standard object.",
    )


class ComponentStatus(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    conditions: Optional[List[ComponentCondition]] = Field(
        None, description="List of component conditions observed"
    )
    kind: Optional[Kind70] = Field(
        "ComponentStatus",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )


class ComponentStatusList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[ComponentStatus] = Field(
        ..., description="List of ComponentStatus objects."
    )
    kind: Optional[Kind71] = Field(
        "ComponentStatusList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )


class ConfigMap(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    binaryData: Optional[Dict[str, Any]] = Field(
        None,
        description="BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet.",
    )
    data: Optional[Dict[str, Any]] = Field(
        None,
        description="Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process.",
    )
    kind: Optional[Kind72] = Field(
        "ConfigMap",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )


class ConfigMapList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[ConfigMap] = Field(..., description="Items is the list of ConfigMaps.")
    kind: Optional[Kind73] = Field(
        "ConfigMapList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )


class ContainerState(BaseModel):
    class Config:
        extra = "forbid"

    running: Optional[ContainerStateRunning] = Field(
        None, description="Details about a running container"
    )
    terminated: Optional[ContainerStateTerminated] = Field(
        None, description="Details about a terminated container"
    )
    waiting: Optional[ContainerStateWaiting] = Field(
        None, description="Details about a waiting container"
    )


class ContainerStatus(BaseModel):
    class Config:
        extra = "forbid"

    containerID: Optional[str] = Field(
        None, description="Container's ID in the format 'docker://<container_id>'."
    )
    image: str = Field(
        ...,
        description="The image the container is running. More info: https://kubernetes.io/docs/concepts/containers/images",
    )
    imageID: str = Field(..., description="ImageID of the container's image.")
    lastState: Optional[ContainerState] = Field(
        None, description="Details about the container's last termination condition."
    )
    name: str = Field(
        ...,
        description="This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be updated.",
    )
    ready: bool = Field(
        ...,
        description="Specifies whether the container has passed its readiness probe.",
    )
    restartCount: int = Field(
        ...,
        description="The number of times the container has been restarted, currently based on the number of dead containers that have not yet been removed. Note that this is calculated from dead containers. But those containers are subject to garbage collection. This value will get capped at 5 by GC.",
    )
    started: Optional[bool] = Field(
        None,
        description="Specifies whether the container has passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. Is always true when no startupProbe is defined.",
    )
    state: Optional[ContainerState] = Field(
        None, description="Details about the container's current condition."
    )


class DownwardAPIVolumeFile(BaseModel):
    class Config:
        extra = "forbid"

    fieldRef: Optional[ObjectFieldSelector] = Field(
        None,
        description="Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.",
    )
    mode: Optional[int] = Field(
        None,
        description="Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.",
    )
    path: str = Field(
        ...,
        description="Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'",
    )
    resourceFieldRef: Optional[ResourceFieldSelector] = Field(
        None,
        description="Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.",
    )


class DownwardAPIVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    defaultMode: Optional[int] = Field(
        None,
        description="Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.",
    )
    items: Optional[List[DownwardAPIVolumeFile]] = Field(
        None, description="Items is a list of downward API volume file"
    )


class Endpoints(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind74] = Field(
        "Endpoints",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    subsets: Optional[List[EndpointSubset]] = Field(
        None,
        description="The set of all endpoints is the union of all subsets. Addresses are placed into subsets according to the IPs they share. A single address with multiple ports, some of which are ready and some of which are not (because they come from different containers) will result in the address being displayed in different subsets for the different ports. No address will appear in both Addresses and NotReadyAddresses in the same subset. Sets of addresses and ports that comprise a service.",
    )


class EndpointsList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[Endpoints] = Field(..., description="List of endpoints.")
    kind: Optional[Kind75] = Field(
        "EndpointsList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )


class EnvVarSource(BaseModel):
    class Config:
        extra = "forbid"

    configMapKeyRef: Optional[ConfigMapKeySelector] = Field(
        None, description="Selects a key of a ConfigMap."
    )
    fieldRef: Optional[ObjectFieldSelector] = Field(
        None,
        description="Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels, metadata.annotations, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP.",
    )
    resourceFieldRef: Optional[ResourceFieldSelector] = Field(
        None,
        description="Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.",
    )
    secretKeyRef: Optional[SecretKeySelector] = Field(
        None, description="Selects a key of a secret in the pod's namespace"
    )


class Event(BaseModel):
    class Config:
        extra = "forbid"

    action: Optional[str] = Field(
        None,
        description="What action was taken/failed regarding to the Regarding object.",
    )
    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    count: Optional[int] = Field(
        None, description="The number of times this event has occurred."
    )
    eventTime: Optional[v1.MicroTime] = Field(
        None, description="Time when this Event was first observed."
    )
    firstTimestamp: Optional[v1.Time] = Field(
        None,
        description="The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)",
    )
    involvedObject: ObjectReference = Field(
        ..., description="The object that this event is about."
    )
    kind: Optional[Kind76] = Field(
        "Event",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    lastTimestamp: Optional[v1.Time] = Field(
        None,
        description="The time at which the most recent occurrence of this event was recorded.",
    )
    message: Optional[str] = Field(
        None,
        description="A human-readable description of the status of this operation.",
    )
    metadata: v1.ObjectMeta = Field(
        ...,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    reason: Optional[str] = Field(
        None,
        description="This should be a short, machine understandable string that gives the reason for the transition into the object's current status.",
    )
    related: Optional[ObjectReference] = Field(
        None, description="Optional secondary object for more complex actions."
    )
    reportingComponent: Optional[str] = Field(
        None,
        description="Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.",
    )
    reportingInstance: Optional[str] = Field(
        None, description="ID of the controller instance, e.g. `kubelet-xyzf`."
    )
    series: Optional[EventSeries] = Field(
        None,
        description="Data about the Event series this event represents or nil if it's a singleton Event.",
    )
    source: Optional[EventSource] = Field(
        None,
        description="The component reporting this event. Should be a short machine understandable string.",
    )
    type: Optional[str] = Field(
        None,
        description="Type of this event (Normal, Warning), new types could be added in the future",
    )


class EventList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[Event] = Field(..., description="List of events")
    kind: Optional[Kind77] = Field(
        "EventList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )


class Handler(BaseModel):
    class Config:
        extra = "forbid"

    exec: Optional[ExecAction] = Field(
        None,
        description="One and only one of the following should be specified. Exec specifies the action to take.",
    )
    httpGet: Optional[HTTPGetAction] = Field(
        None, description="HTTPGet specifies the http request to perform."
    )
    tcpSocket: Optional[TCPSocketAction] = Field(
        None,
        description="TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported",
    )


class Lifecycle(BaseModel):
    class Config:
        extra = "forbid"

    postStart: Optional[Handler] = Field(
        None,
        description="PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks",
    )
    preStop: Optional[Handler] = Field(
        None,
        description="PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The reason for termination is passed to the handler. The Pod's termination grace period countdown begins before the PreStop hooked is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks",
    )


class LimitRange(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind78] = Field(
        "LimitRange",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[LimitRangeSpec] = Field(
        None,
        description="Spec defines the limits enforced. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class LimitRangeList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[LimitRange] = Field(
        ...,
        description="Items is a list of LimitRange objects. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/",
    )
    kind: Optional[Kind79] = Field(
        "LimitRangeList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )


class Namespace(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind80] = Field(
        "Namespace",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[NamespaceSpec] = Field(
        None,
        description="Spec defines the behavior of the Namespace. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )
    status: Optional[NamespaceStatus] = Field(
        None,
        description="Status describes the current status of a Namespace. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class NamespaceList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[Namespace] = Field(
        ...,
        description="Items is the list of Namespace objects in the list. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/",
    )
    kind: Optional[Kind81] = Field(
        "NamespaceList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )


class NodeAffinity(BaseModel):
    class Config:
        extra = "forbid"

    preferredDuringSchedulingIgnoredDuringExecution: Optional[
        List[PreferredSchedulingTerm]
    ] = Field(
        None,
        description='The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.',
    )
    requiredDuringSchedulingIgnoredDuringExecution: Optional[NodeSelector] = Field(
        None,
        description="If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.",
    )


class NodeSpec(BaseModel):
    class Config:
        extra = "forbid"

    configSource: Optional[NodeConfigSource] = Field(
        None,
        description="If specified, the source to get node configuration from The DynamicKubeletConfig feature gate must be enabled for the Kubelet to use this field",
    )
    externalID: Optional[str] = Field(
        None,
        description="Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966",
    )
    podCIDR: Optional[str] = Field(
        None, description="PodCIDR represents the pod IP range assigned to the node."
    )
    podCIDRs: Optional[List[str]] = Field(
        None,
        description="podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6.",
    )
    providerID: Optional[str] = Field(
        None,
        description="ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>",
    )
    taints: Optional[List[Taint]] = Field(
        None, description="If specified, the node's taints."
    )
    unschedulable: Optional[bool] = Field(
        None,
        description="Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration",
    )


class PersistentVolumeClaimSpec(BaseModel):
    class Config:
        extra = "forbid"

    accessModes: Optional[List[str]] = Field(
        None,
        description="AccessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1",
    )
    dataSource: Optional[TypedLocalObjectReference] = Field(
        None,
        description="This field requires the VolumeSnapshotDataSource alpha feature gate to be enabled and currently VolumeSnapshot is the only supported data source. If the provisioner can support VolumeSnapshot data source, it will create a new volume and data will be restored to the volume at the same time. If the provisioner does not support VolumeSnapshot data source, volume will not be created and the failure will be reported as an event. In the future, we plan to support more data source types and the behavior of the provisioner may change.",
    )
    resources: Optional[ResourceRequirements] = Field(
        None,
        description="Resources represents the minimum resources the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources",
    )
    selector: Optional[v1.LabelSelector] = Field(
        None, description="A label query over volumes to consider for binding."
    )
    storageClassName: Optional[str] = Field(
        None,
        description="Name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1",
    )
    volumeMode: Optional[str] = Field(
        None,
        description="volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. This is a beta feature.",
    )
    volumeName: Optional[str] = Field(
        None,
        description="VolumeName is the binding reference to the PersistentVolume backing this claim.",
    )


class PersistentVolumeSpec(BaseModel):
    class Config:
        extra = "forbid"

    accessModes: Optional[List[str]] = Field(
        None,
        description="AccessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes",
    )
    awsElasticBlockStore: Optional[AWSElasticBlockStoreVolumeSource] = Field(
        None,
        description="AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore",
    )
    azureDisk: Optional[AzureDiskVolumeSource] = Field(
        None,
        description="AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.",
    )
    azureFile: Optional[AzureFilePersistentVolumeSource] = Field(
        None,
        description="AzureFile represents an Azure File Service mount on the host and bind mount to the pod.",
    )
    capacity: Optional[Dict[str, Any]] = Field(
        None,
        description="A description of the persistent volume's resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity",
    )
    cephfs: Optional[CephFSPersistentVolumeSource] = Field(
        None,
        description="CephFS represents a Ceph FS mount on the host that shares a pod's lifetime",
    )
    cinder: Optional[CinderPersistentVolumeSource] = Field(
        None,
        description="Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md",
    )
    claimRef: Optional[ObjectReference] = Field(
        None,
        description="ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding",
    )
    csi: Optional[CSIPersistentVolumeSource] = Field(
        None,
        description="CSI represents storage that is handled by an external CSI driver (Beta feature).",
    )
    fc: Optional[FCVolumeSource] = Field(
        None,
        description="FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.",
    )
    flexVolume: Optional[FlexPersistentVolumeSource] = Field(
        None,
        description="FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.",
    )
    flocker: Optional[FlockerVolumeSource] = Field(
        None,
        description="Flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running",
    )
    gcePersistentDisk: Optional[GCEPersistentDiskVolumeSource] = Field(
        None,
        description="GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk",
    )
    glusterfs: Optional[GlusterfsPersistentVolumeSource] = Field(
        None,
        description="Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: https://examples.k8s.io/volumes/glusterfs/README.md",
    )
    hostPath: Optional[HostPathVolumeSource] = Field(
        None,
        description="HostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath",
    )
    iscsi: Optional[ISCSIPersistentVolumeSource] = Field(
        None,
        description="ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.",
    )
    local: Optional[LocalVolumeSource] = Field(
        None,
        description="Local represents directly-attached storage with node affinity",
    )
    mountOptions: Optional[List[str]] = Field(
        None,
        description='A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options',
    )
    nfs: Optional[NFSVolumeSource] = Field(
        None,
        description="NFS represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs",
    )
    nodeAffinity: Optional[VolumeNodeAffinity] = Field(
        None,
        description="NodeAffinity defines constraints that limit what nodes this volume can be accessed from. This field influences the scheduling of pods that use this volume.",
    )
    persistentVolumeReclaimPolicy: Optional[str] = Field(
        None,
        description="What happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming",
    )
    photonPersistentDisk: Optional[PhotonPersistentDiskVolumeSource] = Field(
        None,
        description="PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine",
    )
    portworxVolume: Optional[PortworxVolumeSource] = Field(
        None,
        description="PortworxVolume represents a portworx volume attached and mounted on kubelets host machine",
    )
    quobyte: Optional[QuobyteVolumeSource] = Field(
        None,
        description="Quobyte represents a Quobyte mount on the host that shares a pod's lifetime",
    )
    rbd: Optional[RBDPersistentVolumeSource] = Field(
        None,
        description="RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md",
    )
    scaleIO: Optional[ScaleIOPersistentVolumeSource] = Field(
        None,
        description="ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.",
    )
    storageClassName: Optional[str] = Field(
        None,
        description="Name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass.",
    )
    storageos: Optional[StorageOSPersistentVolumeSource] = Field(
        None,
        description="StorageOS represents a StorageOS volume that is attached to the kubelet's host machine and mounted into the pod More info: https://examples.k8s.io/volumes/storageos/README.md",
    )
    volumeMode: Optional[str] = Field(
        None,
        description="volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec. This is a beta feature.",
    )
    vsphereVolume: Optional[VsphereVirtualDiskVolumeSource] = Field(
        None,
        description="VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine",
    )


class PodAffinityTerm(BaseModel):
    class Config:
        extra = "forbid"

    labelSelector: Optional[v1.LabelSelector] = Field(
        None, description="A label query over a set of resources, in this case pods."
    )
    namespaces: Optional[List[str]] = Field(
        None,
        description='namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod\'s namespace"',
    )
    topologyKey: str = Field(
        ...,
        description="This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.",
    )


class PodStatus(BaseModel):
    class Config:
        extra = "forbid"

    conditions: Optional[List[PodCondition]] = Field(
        None,
        description="Current service state of pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions",
    )
    containerStatuses: Optional[List[ContainerStatus]] = Field(
        None,
        description="The list has one entry per container in the manifest. Each entry is currently the output of `docker inspect`. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status",
    )
    ephemeralContainerStatuses: Optional[List[ContainerStatus]] = Field(
        None,
        description="Status for any ephemeral containers that have run in this pod. This field is alpha-level and is only populated by servers that enable the EphemeralContainers feature.",
    )
    hostIP: Optional[str] = Field(
        None,
        description="IP address of the host to which the pod is assigned. Empty if not yet scheduled.",
    )
    initContainerStatuses: Optional[List[ContainerStatus]] = Field(
        None,
        description="The list has one entry per init container in the manifest. The most recent successful init container will have ready = true, the most recently started container will have startTime set. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status",
    )
    message: Optional[str] = Field(
        None,
        description="A human readable message indicating details about why the pod is in this condition.",
    )
    nominatedNodeName: Optional[str] = Field(
        None,
        description="nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled.",
    )
    phase: Optional[str] = Field(
        None,
        description="The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:\n\nPending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.\n\nMore info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase",
    )
    podIP: Optional[str] = Field(
        None,
        description="IP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated.",
    )
    podIPs: Optional[List[PodIP]] = Field(
        None,
        description="podIPs holds the IP addresses allocated to the pod. If this field is specified, the 0th entry must match the podIP field. Pods may be allocated at most 1 value for each of IPv4 and IPv6. This list is empty if no IPs have been allocated yet.",
    )
    qosClass: Optional[str] = Field(
        None,
        description="The Quality of Service (QOS) classification assigned to the pod based on resource requirements See PodQOSClass type for available QOS classes More info: https://git.k8s.io/community/contributors/design-proposals/node/resource-qos.md",
    )
    reason: Optional[str] = Field(
        None,
        description="A brief CamelCase message indicating details about why the pod is in this state. e.g. 'Evicted'",
    )
    startTime: Optional[v1.Time] = Field(
        None,
        description="RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod.",
    )


class Probe(BaseModel):
    class Config:
        extra = "forbid"

    exec: Optional[ExecAction] = Field(
        None,
        description="One and only one of the following should be specified. Exec specifies the action to take.",
    )
    failureThreshold: Optional[int] = Field(
        None,
        description="Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.",
    )
    httpGet: Optional[HTTPGetAction] = Field(
        None, description="HTTPGet specifies the http request to perform."
    )
    initialDelaySeconds: Optional[int] = Field(
        None,
        description="Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes",
    )
    periodSeconds: Optional[int] = Field(
        None,
        description="How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.",
    )
    successThreshold: Optional[int] = Field(
        None,
        description="Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.",
    )
    tcpSocket: Optional[TCPSocketAction] = Field(
        None,
        description="TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported",
    )
    timeoutSeconds: Optional[int] = Field(
        None,
        description="Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes",
    )


class ResourceQuotaSpec(BaseModel):
    class Config:
        extra = "forbid"

    hard: Optional[Dict[str, Any]] = Field(
        None,
        description="hard is the set of desired hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/",
    )
    scopeSelector: Optional[ScopeSelector] = Field(
        None,
        description="scopeSelector is also a collection of filters like scopes that must match each object tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched.",
    )
    scopes: Optional[List[str]] = Field(
        None,
        description="A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects.",
    )


class Secret(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    data: Optional[Dict[str, Any]] = Field(
        None,
        description="Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in https://tools.ietf.org/html/rfc4648#section-4",
    )
    kind: Optional[Kind96] = Field(
        "Secret",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    stringData: Optional[Dict[str, Any]] = Field(
        None,
        description="stringData allows specifying non-binary secret data in string form. It is provided as a write-only convenience method. All keys and values are merged into the data field on write, overwriting any existing values. It is never output when reading from the API.",
    )
    type: Optional[str] = Field(
        None, description="Used to facilitate programmatic handling of secret data."
    )


class SecretList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[Secret] = Field(
        ...,
        description="Items is a list of secret objects. More info: https://kubernetes.io/docs/concepts/configuration/secret",
    )
    kind: Optional[Kind97] = Field(
        "SecretList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )


class Service(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind98] = Field(
        "Service",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[ServiceSpec] = Field(
        None,
        description="Spec defines the behavior of a service. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )
    status: Optional[ServiceStatus] = Field(
        None,
        description="Most recently observed status of the service. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class ServiceAccount(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    automountServiceAccountToken: Optional[bool] = Field(
        None,
        description="AutomountServiceAccountToken indicates whether pods running as this service account should have an API token automatically mounted. Can be overridden at the pod level.",
    )
    imagePullSecrets: Optional[List[LocalObjectReference]] = Field(
        None,
        description="ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod",
    )
    kind: Optional[Kind99] = Field(
        "ServiceAccount",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    secrets: Optional[List[ObjectReference]] = Field(
        None,
        description="Secrets is the list of secrets allowed to be used by pods running using this ServiceAccount. More info: https://kubernetes.io/docs/concepts/configuration/secret",
    )


class ServiceAccountList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[ServiceAccount] = Field(
        ...,
        description="List of ServiceAccounts. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/",
    )
    kind: Optional[Kind100] = Field(
        "ServiceAccountList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )


class ServiceList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[Service] = Field(..., description="List of services")
    kind: Optional[Kind101] = Field(
        "ServiceList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )


class TopologySpreadConstraint(BaseModel):
    class Config:
        extra = "forbid"

    labelSelector: Optional[v1.LabelSelector] = Field(
        None,
        description="LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.",
    )
    maxSkew: int = Field(
        ...,
        description="MaxSkew describes the degree to which pods may be unevenly distributed. It's the maximum permitted difference between the number of matching pods in any two topology domains of a given topology type. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 1/1/0: | zone1 | zone2 | zone3 | |   P   |   P   |       | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 1/1/1; scheduling it onto zone1(zone2) would make the ActualSkew(2-0) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. It's a required field. Default value is 1 and 0 is not allowed.",
    )
    topologyKey: str = Field(
        ...,
        description='TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a "bucket", and try to put balanced number of pods into each bucket. It\'s a required field.',
    )
    whenUnsatisfiable: str = Field(
        ...,
        description="WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it - ScheduleAnyway tells the scheduler to still schedule it It's considered as \"Unsatisfiable\" if and only if placing incoming pod on any topology violates \"MaxSkew\". For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.",
    )


class WeightedPodAffinityTerm(BaseModel):
    class Config:
        extra = "forbid"

    podAffinityTerm: PodAffinityTerm = Field(
        ...,
        description="Required. A pod affinity term, associated with the corresponding weight.",
    )
    weight: int = Field(
        ...,
        description="weight associated with matching the corresponding podAffinityTerm, in the range 1-100.",
    )


class DownwardAPIProjection(BaseModel):
    class Config:
        extra = "forbid"

    items: Optional[List[DownwardAPIVolumeFile]] = Field(
        None, description="Items is a list of DownwardAPIVolume file"
    )


class EnvVar(BaseModel):
    class Config:
        extra = "forbid"

    name: str = Field(
        ..., description="Name of the environment variable. Must be a C_IDENTIFIER."
    )
    value: Optional[str] = Field(
        None,
        description='Variable references $(VAR_NAME) are expanded using the previous defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".',
    )
    valueFrom: Optional[EnvVarSource] = Field(
        None,
        description="Source for the environment variable's value. Cannot be used if value is not empty.",
    )


class EphemeralContainer(BaseModel):
    class Config:
        extra = "forbid"

    args: Optional[List[str]] = Field(
        None,
        description="Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell",
    )
    command: Optional[List[str]] = Field(
        None,
        description="Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell",
    )
    env: Optional[List[EnvVar]] = Field(
        None,
        description="List of environment variables to set in the container. Cannot be updated.",
    )
    envFrom: Optional[List[EnvFromSource]] = Field(
        None,
        description="List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.",
    )
    image: Optional[str] = Field(
        None,
        description="Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images",
    )
    imagePullPolicy: Optional[str] = Field(
        None,
        description="Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images",
    )
    lifecycle: Optional[Lifecycle] = Field(
        None, description="Lifecycle is not allowed for ephemeral containers."
    )
    livenessProbe: Optional[Probe] = Field(
        None, description="Probes are not allowed for ephemeral containers."
    )
    name: str = Field(
        ...,
        description="Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers.",
    )
    ports: Optional[List[ContainerPort]] = Field(
        None, description="Ports are not allowed for ephemeral containers."
    )
    readinessProbe: Optional[Probe] = Field(
        None, description="Probes are not allowed for ephemeral containers."
    )
    resources: Optional[ResourceRequirements] = Field(
        None,
        description="Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod.",
    )
    securityContext: Optional[SecurityContext] = Field(
        None, description="SecurityContext is not allowed for ephemeral containers."
    )
    startupProbe: Optional[Probe] = Field(
        None, description="Probes are not allowed for ephemeral containers."
    )
    stdin: Optional[bool] = Field(
        None,
        description="Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.",
    )
    stdinOnce: Optional[bool] = Field(
        None,
        description="Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false",
    )
    targetContainerName: Optional[str] = Field(
        None,
        description="If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container is run in whatever namespaces are shared for the pod. Note that the container runtime must support this feature.",
    )
    terminationMessagePath: Optional[str] = Field(
        None,
        description="Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.",
    )
    terminationMessagePolicy: Optional[str] = Field(
        None,
        description="Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.",
    )
    tty: Optional[bool] = Field(
        None,
        description="Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.",
    )
    volumeDevices: Optional[List[VolumeDevice]] = Field(
        None,
        description="volumeDevices is the list of block devices to be used by the container. This is a beta feature.",
    )
    volumeMounts: Optional[List[VolumeMount]] = Field(
        None,
        description="Pod volumes to mount into the container's filesystem. Cannot be updated.",
    )
    workingDir: Optional[str] = Field(
        None,
        description="Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.",
    )


class Node(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind82] = Field(
        "Node",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[NodeSpec] = Field(
        None,
        description="Spec defines the behavior of a node. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )
    status: Optional[NodeStatus] = Field(
        None,
        description="Most recently observed status of the node. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class NodeList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[Node] = Field(..., description="List of nodes")
    kind: Optional[Kind83] = Field(
        "NodeList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )


class PersistentVolume(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind84] = Field(
        "PersistentVolume",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[PersistentVolumeSpec] = Field(
        None,
        description="Spec defines a specification of a persistent volume owned by the cluster. Provisioned by an administrator. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistent-volumes",
    )
    status: Optional[PersistentVolumeStatus] = Field(
        None,
        description="Status represents the current information/status for the persistent volume. Populated by the system. Read-only. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistent-volumes",
    )


class PersistentVolumeClaim(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind85] = Field(
        "PersistentVolumeClaim",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[PersistentVolumeClaimSpec] = Field(
        None,
        description="Spec defines the desired characteristics of a volume requested by a pod author. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims",
    )
    status: Optional[PersistentVolumeClaimStatus] = Field(
        None,
        description="Status represents the current information/status of a persistent volume claim. Read-only. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims",
    )


class PersistentVolumeClaimList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[PersistentVolumeClaim] = Field(
        ...,
        description="A list of persistent volume claims. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims",
    )
    kind: Optional[Kind86] = Field(
        "PersistentVolumeClaimList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )


class PersistentVolumeList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[PersistentVolume] = Field(
        ...,
        description="List of persistent volumes. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes",
    )
    kind: Optional[Kind87] = Field(
        "PersistentVolumeList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )


class PodAffinity(BaseModel):
    class Config:
        extra = "forbid"

    preferredDuringSchedulingIgnoredDuringExecution: Optional[
        List[WeightedPodAffinityTerm]
    ] = Field(
        None,
        description='The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.',
    )
    requiredDuringSchedulingIgnoredDuringExecution: Optional[
        List[PodAffinityTerm]
    ] = Field(
        None,
        description="If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.",
    )


class PodAntiAffinity(BaseModel):
    class Config:
        extra = "forbid"

    preferredDuringSchedulingIgnoredDuringExecution: Optional[
        List[WeightedPodAffinityTerm]
    ] = Field(
        None,
        description='The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.',
    )
    requiredDuringSchedulingIgnoredDuringExecution: Optional[
        List[PodAffinityTerm]
    ] = Field(
        None,
        description="If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.",
    )


class ResourceQuota(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind94] = Field(
        "ResourceQuota",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[ResourceQuotaSpec] = Field(
        None,
        description="Spec defines the desired quota. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )
    status: Optional[ResourceQuotaStatus] = Field(
        None,
        description="Status defines the actual enforced quota and its current usage. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class ResourceQuotaList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[ResourceQuota] = Field(
        ...,
        description="Items is a list of ResourceQuota objects. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/",
    )
    kind: Optional[Kind95] = Field(
        "ResourceQuotaList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )


class VolumeProjection(BaseModel):
    class Config:
        extra = "forbid"

    configMap: Optional[ConfigMapProjection] = Field(
        None, description="information about the configMap data to project"
    )
    downwardAPI: Optional[DownwardAPIProjection] = Field(
        None, description="information about the downwardAPI data to project"
    )
    secret: Optional[SecretProjection] = Field(
        None, description="information about the secret data to project"
    )
    serviceAccountToken: Optional[ServiceAccountTokenProjection] = Field(
        None, description="information about the serviceAccountToken data to project"
    )


class Affinity(BaseModel):
    class Config:
        extra = "forbid"

    nodeAffinity: Optional[NodeAffinity] = Field(
        None, description="Describes node affinity scheduling rules for the pod."
    )
    podAffinity: Optional[PodAffinity] = Field(
        None,
        description="Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).",
    )
    podAntiAffinity: Optional[PodAntiAffinity] = Field(
        None,
        description="Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).",
    )


class Container(BaseModel):
    class Config:
        extra = "forbid"

    args: Optional[List[str]] = Field(
        None,
        description="Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell",
    )
    command: Optional[List[str]] = Field(
        None,
        description="Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell",
    )
    env: Optional[List[EnvVar]] = Field(
        None,
        description="List of environment variables to set in the container. Cannot be updated.",
    )
    envFrom: Optional[List[EnvFromSource]] = Field(
        None,
        description="List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.",
    )
    image: Optional[str] = Field(
        None,
        description="Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.",
    )
    imagePullPolicy: Optional[str] = Field(
        None,
        description="Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images",
    )
    lifecycle: Optional[Lifecycle] = Field(
        None,
        description="Actions that the management system should take in response to container lifecycle events. Cannot be updated.",
    )
    livenessProbe: Optional[Probe] = Field(
        None,
        description="Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes",
    )
    name: str = Field(
        ...,
        description="Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.",
    )
    ports: Optional[List[ContainerPort]] = Field(
        None,
        description='List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Cannot be updated.',
    )
    readinessProbe: Optional[Probe] = Field(
        None,
        description="Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes",
    )
    resources: Optional[ResourceRequirements] = Field(
        None,
        description="Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/",
    )
    securityContext: Optional[SecurityContext] = Field(
        None,
        description="Security options the pod should run with. More info: https://kubernetes.io/docs/concepts/policy/security-context/ More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/",
    )
    startupProbe: Optional[Probe] = Field(
        None,
        description="StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. This is an alpha feature enabled by the StartupProbe feature flag. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes",
    )
    stdin: Optional[bool] = Field(
        None,
        description="Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.",
    )
    stdinOnce: Optional[bool] = Field(
        None,
        description="Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false",
    )
    terminationMessagePath: Optional[str] = Field(
        None,
        description="Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.",
    )
    terminationMessagePolicy: Optional[str] = Field(
        None,
        description="Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.",
    )
    tty: Optional[bool] = Field(
        None,
        description="Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.",
    )
    volumeDevices: Optional[List[VolumeDevice]] = Field(
        None,
        description="volumeDevices is the list of block devices to be used by the container. This is a beta feature.",
    )
    volumeMounts: Optional[List[VolumeMount]] = Field(
        None,
        description="Pod volumes to mount into the container's filesystem. Cannot be updated.",
    )
    workingDir: Optional[str] = Field(
        None,
        description="Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.",
    )


class ProjectedVolumeSource(BaseModel):
    class Config:
        extra = "forbid"

    defaultMode: Optional[int] = Field(
        None,
        description="Mode bits to use on created files by default. Must be a value between 0 and 0777. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.",
    )
    sources: List[VolumeProjection] = Field(
        ..., description="list of volume projections"
    )


class Volume(BaseModel):
    class Config:
        extra = "forbid"

    awsElasticBlockStore: Optional[AWSElasticBlockStoreVolumeSource] = Field(
        None,
        description="AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore",
    )
    azureDisk: Optional[AzureDiskVolumeSource] = Field(
        None,
        description="AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.",
    )
    azureFile: Optional[AzureFileVolumeSource] = Field(
        None,
        description="AzureFile represents an Azure File Service mount on the host and bind mount to the pod.",
    )
    cephfs: Optional[CephFSVolumeSource] = Field(
        None,
        description="CephFS represents a Ceph FS mount on the host that shares a pod's lifetime",
    )
    cinder: Optional[CinderVolumeSource] = Field(
        None,
        description="Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md",
    )
    configMap: Optional[ConfigMapVolumeSource] = Field(
        None,
        description="ConfigMap represents a configMap that should populate this volume",
    )
    csi: Optional[CSIVolumeSource] = Field(
        None,
        description="CSI (Container Storage Interface) represents storage that is handled by an external CSI driver (Alpha feature).",
    )
    downwardAPI: Optional[DownwardAPIVolumeSource] = Field(
        None,
        description="DownwardAPI represents downward API about the pod that should populate this volume",
    )
    emptyDir: Optional[EmptyDirVolumeSource] = Field(
        None,
        description="EmptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir",
    )
    fc: Optional[FCVolumeSource] = Field(
        None,
        description="FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.",
    )
    flexVolume: Optional[FlexVolumeSource] = Field(
        None,
        description="FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.",
    )
    flocker: Optional[FlockerVolumeSource] = Field(
        None,
        description="Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running",
    )
    gcePersistentDisk: Optional[GCEPersistentDiskVolumeSource] = Field(
        None,
        description="GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk",
    )
    gitRepo: Optional[GitRepoVolumeSource] = Field(
        None,
        description="GitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.",
    )
    glusterfs: Optional[GlusterfsVolumeSource] = Field(
        None,
        description="Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md",
    )
    hostPath: Optional[HostPathVolumeSource] = Field(
        None,
        description="HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath",
    )
    iscsi: Optional[ISCSIVolumeSource] = Field(
        None,
        description="ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md",
    )
    name: str = Field(
        ...,
        description="Volume's name. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names",
    )
    nfs: Optional[NFSVolumeSource] = Field(
        None,
        description="NFS represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs",
    )
    persistentVolumeClaim: Optional[PersistentVolumeClaimVolumeSource] = Field(
        None,
        description="PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims",
    )
    photonPersistentDisk: Optional[PhotonPersistentDiskVolumeSource] = Field(
        None,
        description="PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine",
    )
    portworxVolume: Optional[PortworxVolumeSource] = Field(
        None,
        description="PortworxVolume represents a portworx volume attached and mounted on kubelets host machine",
    )
    projected: Optional[ProjectedVolumeSource] = Field(
        None,
        description="Items for all in one resources secrets, configmaps, and downward API",
    )
    quobyte: Optional[QuobyteVolumeSource] = Field(
        None,
        description="Quobyte represents a Quobyte mount on the host that shares a pod's lifetime",
    )
    rbd: Optional[RBDVolumeSource] = Field(
        None,
        description="RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md",
    )
    scaleIO: Optional[ScaleIOVolumeSource] = Field(
        None,
        description="ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.",
    )
    secret: Optional[SecretVolumeSource] = Field(
        None,
        description="Secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret",
    )
    storageos: Optional[StorageOSVolumeSource] = Field(
        None,
        description="StorageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.",
    )
    vsphereVolume: Optional[VsphereVirtualDiskVolumeSource] = Field(
        None,
        description="VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine",
    )


class PodSpec(BaseModel):
    class Config:
        extra = "forbid"

    activeDeadlineSeconds: Optional[int] = Field(
        None,
        description="Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.",
    )
    affinity: Optional[Affinity] = Field(
        None, description="If specified, the pod's scheduling constraints"
    )
    automountServiceAccountToken: Optional[bool] = Field(
        None,
        description="AutomountServiceAccountToken indicates whether a service account token should be automatically mounted.",
    )
    containers: List[Container] = Field(
        ...,
        description="List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.",
    )
    dnsConfig: Optional[PodDNSConfig] = Field(
        None,
        description="Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy.",
    )
    dnsPolicy: Optional[str] = Field(
        None,
        description="Set DNS policy for the pod. Defaults to \"ClusterFirst\". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.",
    )
    enableServiceLinks: Optional[bool] = Field(
        None,
        description="EnableServiceLinks indicates whether information about services should be injected into pod's environment variables, matching the syntax of Docker links. Optional: Defaults to true.",
    )
    ephemeralContainers: Optional[List[EphemeralContainer]] = Field(
        None,
        description="List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod's ephemeralcontainers subresource. This field is alpha-level and is only honored by servers that enable the EphemeralContainers feature.",
    )
    hostAliases: Optional[List[HostAlias]] = Field(
        None,
        description="HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified. This is only valid for non-hostNetwork pods.",
    )
    hostIPC: Optional[bool] = Field(
        None, description="Use the host's ipc namespace. Optional: Default to false."
    )
    hostNetwork: Optional[bool] = Field(
        None,
        description="Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.",
    )
    hostPID: Optional[bool] = Field(
        None, description="Use the host's pid namespace. Optional: Default to false."
    )
    hostname: Optional[str] = Field(
        None,
        description="Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.",
    )
    imagePullSecrets: Optional[List[LocalObjectReference]] = Field(
        None,
        description="ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod",
    )
    initContainers: Optional[List[Container]] = Field(
        None,
        description="List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/",
    )
    nodeName: Optional[str] = Field(
        None,
        description="NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.",
    )
    nodeSelector: Optional[Dict[str, Any]] = Field(
        None,
        description="NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/",
    )
    overhead: Optional[Dict[str, Any]] = Field(
        None,
        description="Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: https://git.k8s.io/enhancements/keps/sig-node/20190226-pod-overhead.md This field is alpha-level as of Kubernetes v1.16, and is only honored by servers that enable the PodOverhead feature.",
    )
    preemptionPolicy: Optional[str] = Field(
        None,
        description="PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. This field is alpha-level and is only honored by servers that enable the NonPreemptingPriority feature.",
    )
    priority: Optional[int] = Field(
        None,
        description="The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority.",
    )
    priorityClassName: Optional[str] = Field(
        None,
        description='If specified, indicates the pod\'s priority. "system-node-critical" and "system-cluster-critical" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default.',
    )
    readinessGates: Optional[List[PodReadinessGate]] = Field(
        None,
        description='If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: https://git.k8s.io/enhancements/keps/sig-network/0007-pod-ready%2B%2B.md',
    )
    restartPolicy: Optional[str] = Field(
        None,
        description="Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy",
    )
    runtimeClassName: Optional[str] = Field(
        None,
        description='RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://git.k8s.io/enhancements/keps/sig-node/runtime-class.md This is a beta feature as of Kubernetes v1.14.',
    )
    schedulerName: Optional[str] = Field(
        None,
        description="If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler.",
    )
    securityContext: Optional[PodSecurityContext] = Field(
        None,
        description="SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.",
    )
    serviceAccount: Optional[str] = Field(
        None,
        description="DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.",
    )
    serviceAccountName: Optional[str] = Field(
        None,
        description="ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/",
    )
    shareProcessNamespace: Optional[bool] = Field(
        None,
        description="Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false. This field is beta-level and may be disabled with the PodShareProcessNamespace feature.",
    )
    subdomain: Optional[str] = Field(
        None,
        description='If specified, the fully qualified Pod hostname will be "<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>". If not specified, the pod will not have a domainname at all.',
    )
    terminationGracePeriodSeconds: Optional[int] = Field(
        None,
        description="Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.",
    )
    tolerations: Optional[List[Toleration]] = Field(
        None, description="If specified, the pod's tolerations."
    )
    topologySpreadConstraints: Optional[List[TopologySpreadConstraint]] = Field(
        None,
        description="TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. This field is alpha-level and is only honored by clusters that enables the EvenPodsSpread feature. All topologySpreadConstraints are ANDed.",
    )
    volumes: Optional[List[Volume]] = Field(
        None,
        description="List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes",
    )


class PodTemplateSpec(BaseModel):
    class Config:
        extra = "forbid"

    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[PodSpec] = Field(
        None,
        description="Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class ReplicationControllerSpec(BaseModel):
    class Config:
        extra = "forbid"

    minReadySeconds: Optional[int] = Field(
        None,
        description="Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)",
    )
    replicas: Optional[int] = Field(
        None,
        description="Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller",
    )
    selector: Optional[Dict[str, Any]] = Field(
        None,
        description="Selector is a label query over pods that should match the Replicas count. If Selector is empty, it is defaulted to the labels present on the Pod template. Label keys and values that must match in order to be controlled by this replication controller, if empty defaulted to labels on Pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors",
    )
    template: Optional[PodTemplateSpec] = Field(
        None,
        description="Template is the object that describes the pod that will be created if insufficient replicas are detected. This takes precedence over a TemplateRef. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template",
    )


class Pod(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind88] = Field(
        "Pod",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[PodSpec] = Field(
        None,
        description="Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )
    status: Optional[PodStatus] = Field(
        None,
        description="Most recently observed status of the pod. This data may not be up to date. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class PodList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[Pod] = Field(
        ...,
        description="List of pods. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md",
    )
    kind: Optional[Kind89] = Field(
        "PodList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )


class PodTemplate(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind90] = Field(
        "PodTemplate",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    template: Optional[PodTemplateSpec] = Field(
        None,
        description="Template defines the pods that will be created from this pod template. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class PodTemplateList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[PodTemplate] = Field(..., description="List of pod templates")
    kind: Optional[Kind91] = Field(
        "PodTemplateList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )


class ReplicationController(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind92] = Field(
        "ReplicationController",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="If the Labels of a ReplicationController are empty, they are defaulted to be the same as the Pod(s) that the replication controller manages. Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[ReplicationControllerSpec] = Field(
        None,
        description="Spec defines the specification of the desired behavior of the replication controller. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )
    status: Optional[ReplicationControllerStatus] = Field(
        None,
        description="Status is the most recently observed status of the replication controller. This data may be out of date by some window of time. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class ReplicationControllerList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[ReplicationController] = Field(
        ...,
        description="List of replication controllers. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller",
    )
    kind: Optional[Kind93] = Field(
        "ReplicationControllerList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
