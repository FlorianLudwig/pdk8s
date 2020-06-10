# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel


class Model(BaseModel):
    __root__: Any


class Kind(Enum):
    mutating_webhook_configuration = "MutatingWebhookConfiguration"


class Kind1(Enum):
    mutating_webhook_configuration_list = "MutatingWebhookConfigurationList"


class Kind2(Enum):
    validating_webhook_configuration = "ValidatingWebhookConfiguration"


class Kind3(Enum):
    validating_webhook_configuration_list = "ValidatingWebhookConfigurationList"


class Kind4(Enum):
    mutating_webhook_configuration = "MutatingWebhookConfiguration"


class Kind5(Enum):
    mutating_webhook_configuration_list = "MutatingWebhookConfigurationList"


class Kind6(Enum):
    validating_webhook_configuration = "ValidatingWebhookConfiguration"


class Kind7(Enum):
    validating_webhook_configuration_list = "ValidatingWebhookConfigurationList"


class Kind8(Enum):
    controller_revision = "ControllerRevision"


class Kind9(Enum):
    controller_revision_list = "ControllerRevisionList"


class Kind10(Enum):
    daemon_set = "DaemonSet"


class Kind11(Enum):
    daemon_set_list = "DaemonSetList"


class Kind12(Enum):
    deployment = "Deployment"


class Kind13(Enum):
    deployment_list = "DeploymentList"


class Kind14(Enum):
    replica_set = "ReplicaSet"


class Kind15(Enum):
    replica_set_list = "ReplicaSetList"


class Kind16(Enum):
    stateful_set = "StatefulSet"


class Kind17(Enum):
    stateful_set_list = "StatefulSetList"


class Kind18(Enum):
    controller_revision = "ControllerRevision"


class Kind19(Enum):
    controller_revision_list = "ControllerRevisionList"


class Kind20(Enum):
    deployment = "Deployment"


class Kind21(Enum):
    deployment_list = "DeploymentList"


class Kind22(Enum):
    deployment_rollback = "DeploymentRollback"


class Kind23(Enum):
    scale = "Scale"


class Kind24(Enum):
    stateful_set = "StatefulSet"


class Kind25(Enum):
    stateful_set_list = "StatefulSetList"


class Kind26(Enum):
    controller_revision = "ControllerRevision"


class Kind27(Enum):
    controller_revision_list = "ControllerRevisionList"


class Kind28(Enum):
    daemon_set = "DaemonSet"


class Kind29(Enum):
    daemon_set_list = "DaemonSetList"


class Kind30(Enum):
    deployment = "Deployment"


class Kind31(Enum):
    deployment_list = "DeploymentList"


class Kind32(Enum):
    replica_set = "ReplicaSet"


class Kind33(Enum):
    replica_set_list = "ReplicaSetList"


class Kind34(Enum):
    scale = "Scale"


class Kind35(Enum):
    stateful_set = "StatefulSet"


class Kind36(Enum):
    stateful_set_list = "StatefulSetList"


class Kind37(Enum):
    audit_sink = "AuditSink"


class Kind38(Enum):
    audit_sink_list = "AuditSinkList"


class Kind39(Enum):
    token_request = "TokenRequest"


class Kind40(Enum):
    token_review = "TokenReview"


class Kind41(Enum):
    token_review = "TokenReview"


class Kind42(Enum):
    local_subject_access_review = "LocalSubjectAccessReview"


class Kind43(Enum):
    self_subject_access_review = "SelfSubjectAccessReview"


class Kind44(Enum):
    self_subject_rules_review = "SelfSubjectRulesReview"


class Kind45(Enum):
    subject_access_review = "SubjectAccessReview"


class Kind46(Enum):
    local_subject_access_review = "LocalSubjectAccessReview"


class Kind47(Enum):
    self_subject_access_review = "SelfSubjectAccessReview"


class Kind48(Enum):
    self_subject_rules_review = "SelfSubjectRulesReview"


class Kind49(Enum):
    subject_access_review = "SubjectAccessReview"


class Kind50(Enum):
    horizontal_pod_autoscaler = "HorizontalPodAutoscaler"


class Kind51(Enum):
    horizontal_pod_autoscaler_list = "HorizontalPodAutoscalerList"


class Kind52(Enum):
    scale = "Scale"


class Kind53(Enum):
    horizontal_pod_autoscaler = "HorizontalPodAutoscaler"


class Kind54(Enum):
    horizontal_pod_autoscaler_list = "HorizontalPodAutoscalerList"


class Kind55(Enum):
    horizontal_pod_autoscaler = "HorizontalPodAutoscaler"


class Kind56(Enum):
    horizontal_pod_autoscaler_list = "HorizontalPodAutoscalerList"


class Kind57(Enum):
    job = "Job"


class Kind58(Enum):
    job_list = "JobList"


class Kind59(Enum):
    cron_job = "CronJob"


class Kind60(Enum):
    cron_job_list = "CronJobList"


class Kind61(Enum):
    cron_job = "CronJob"


class Kind62(Enum):
    cron_job_list = "CronJobList"


class Kind63(Enum):
    certificate_signing_request = "CertificateSigningRequest"


class Kind64(Enum):
    certificate_signing_request_list = "CertificateSigningRequestList"


class Kind65(Enum):
    lease = "Lease"


class Kind66(Enum):
    lease_list = "LeaseList"


class Kind67(Enum):
    lease = "Lease"


class Kind68(Enum):
    lease_list = "LeaseList"


class Kind69(Enum):
    binding = "Binding"


class Kind70(Enum):
    component_status = "ComponentStatus"


class Kind71(Enum):
    component_status_list = "ComponentStatusList"


class Kind72(Enum):
    config_map = "ConfigMap"


class Kind73(Enum):
    config_map_list = "ConfigMapList"


class Kind74(Enum):
    endpoints = "Endpoints"


class Kind75(Enum):
    endpoints_list = "EndpointsList"


class Kind76(Enum):
    event = "Event"


class Kind77(Enum):
    event_list = "EventList"


class Kind78(Enum):
    limit_range = "LimitRange"


class Kind79(Enum):
    limit_range_list = "LimitRangeList"


class Kind80(Enum):
    namespace = "Namespace"


class Kind81(Enum):
    namespace_list = "NamespaceList"


class Kind82(Enum):
    node = "Node"


class Kind83(Enum):
    node_list = "NodeList"


class Kind84(Enum):
    persistent_volume = "PersistentVolume"


class Kind85(Enum):
    persistent_volume_claim = "PersistentVolumeClaim"


class Kind86(Enum):
    persistent_volume_claim_list = "PersistentVolumeClaimList"


class Kind87(Enum):
    persistent_volume_list = "PersistentVolumeList"


class Kind88(Enum):
    pod = "Pod"


class Kind89(Enum):
    pod_list = "PodList"


class Kind90(Enum):
    pod_template = "PodTemplate"


class Kind91(Enum):
    pod_template_list = "PodTemplateList"


class Kind92(Enum):
    replication_controller = "ReplicationController"


class Kind93(Enum):
    replication_controller_list = "ReplicationControllerList"


class Kind94(Enum):
    resource_quota = "ResourceQuota"


class Kind95(Enum):
    resource_quota_list = "ResourceQuotaList"


class Kind96(Enum):
    secret = "Secret"


class Kind97(Enum):
    secret_list = "SecretList"


class Kind98(Enum):
    service = "Service"


class Kind99(Enum):
    service_account = "ServiceAccount"


class Kind100(Enum):
    service_account_list = "ServiceAccountList"


class Kind101(Enum):
    service_list = "ServiceList"


class Kind102(Enum):
    endpoint_slice = "EndpointSlice"


class Kind103(Enum):
    endpoint_slice_list = "EndpointSliceList"


class Kind104(Enum):
    event = "Event"


class Kind105(Enum):
    event_list = "EventList"


class Kind106(Enum):
    daemon_set = "DaemonSet"


class Kind107(Enum):
    daemon_set_list = "DaemonSetList"


class Kind108(Enum):
    deployment = "Deployment"


class Kind109(Enum):
    deployment_list = "DeploymentList"


class Kind110(Enum):
    deployment_rollback = "DeploymentRollback"


class Kind111(Enum):
    ingress = "Ingress"


class Kind112(Enum):
    ingress_list = "IngressList"


class Kind113(Enum):
    network_policy = "NetworkPolicy"


class Kind114(Enum):
    network_policy_list = "NetworkPolicyList"


class Kind115(Enum):
    pod_security_policy = "PodSecurityPolicy"


class Kind116(Enum):
    pod_security_policy_list = "PodSecurityPolicyList"


class Kind117(Enum):
    replica_set = "ReplicaSet"


class Kind118(Enum):
    replica_set_list = "ReplicaSetList"


class Kind119(Enum):
    scale = "Scale"


class Kind120(Enum):
    network_policy = "NetworkPolicy"


class Kind121(Enum):
    network_policy_list = "NetworkPolicyList"


class Kind122(Enum):
    ingress = "Ingress"


class Kind123(Enum):
    ingress_list = "IngressList"


class Kind124(Enum):
    runtime_class = "RuntimeClass"


class Kind125(Enum):
    runtime_class_list = "RuntimeClassList"


class Kind126(Enum):
    runtime_class = "RuntimeClass"


class Kind127(Enum):
    runtime_class_list = "RuntimeClassList"


class Kind128(Enum):
    eviction = "Eviction"


class Kind129(Enum):
    pod_disruption_budget = "PodDisruptionBudget"


class Kind130(Enum):
    pod_disruption_budget_list = "PodDisruptionBudgetList"


class Kind131(Enum):
    pod_security_policy = "PodSecurityPolicy"


class Kind132(Enum):
    pod_security_policy_list = "PodSecurityPolicyList"


class Kind133(Enum):
    cluster_role = "ClusterRole"


class Kind134(Enum):
    cluster_role_binding = "ClusterRoleBinding"


class Kind135(Enum):
    cluster_role_binding_list = "ClusterRoleBindingList"


class Kind136(Enum):
    cluster_role_list = "ClusterRoleList"


class Kind137(Enum):
    role = "Role"


class Kind138(Enum):
    role_binding = "RoleBinding"


class Kind139(Enum):
    role_binding_list = "RoleBindingList"


class Kind140(Enum):
    role_list = "RoleList"


class Kind141(Enum):
    cluster_role = "ClusterRole"


class Kind142(Enum):
    cluster_role_binding = "ClusterRoleBinding"


class Kind143(Enum):
    cluster_role_binding_list = "ClusterRoleBindingList"


class Kind144(Enum):
    cluster_role_list = "ClusterRoleList"


class Kind145(Enum):
    role = "Role"


class Kind146(Enum):
    role_binding = "RoleBinding"


class Kind147(Enum):
    role_binding_list = "RoleBindingList"


class Kind148(Enum):
    role_list = "RoleList"


class Kind149(Enum):
    cluster_role = "ClusterRole"


class Kind150(Enum):
    cluster_role_binding = "ClusterRoleBinding"


class Kind151(Enum):
    cluster_role_binding_list = "ClusterRoleBindingList"


class Kind152(Enum):
    cluster_role_list = "ClusterRoleList"


class Kind153(Enum):
    role = "Role"


class Kind154(Enum):
    role_binding = "RoleBinding"


class Kind155(Enum):
    role_binding_list = "RoleBindingList"


class Kind156(Enum):
    role_list = "RoleList"


class Kind157(Enum):
    priority_class = "PriorityClass"


class Kind158(Enum):
    priority_class_list = "PriorityClassList"


class Kind159(Enum):
    priority_class = "PriorityClass"


class Kind160(Enum):
    priority_class_list = "PriorityClassList"


class Kind161(Enum):
    priority_class = "PriorityClass"


class Kind162(Enum):
    priority_class_list = "PriorityClassList"


class Kind163(Enum):
    pod_preset = "PodPreset"


class Kind164(Enum):
    pod_preset_list = "PodPresetList"


class Kind165(Enum):
    storage_class = "StorageClass"


class Kind166(Enum):
    storage_class_list = "StorageClassList"


class Kind167(Enum):
    volume_attachment = "VolumeAttachment"


class Kind168(Enum):
    volume_attachment_list = "VolumeAttachmentList"


class Kind169(Enum):
    volume_attachment = "VolumeAttachment"


class Kind170(Enum):
    volume_attachment_list = "VolumeAttachmentList"


class Kind171(Enum):
    csi_driver = "CSIDriver"


class Kind172(Enum):
    csi_driver_list = "CSIDriverList"


class Kind173(Enum):
    csi_node = "CSINode"


class Kind174(Enum):
    csi_node_list = "CSINodeList"


class Kind175(Enum):
    storage_class = "StorageClass"


class Kind176(Enum):
    storage_class_list = "StorageClassList"


class Kind177(Enum):
    volume_attachment = "VolumeAttachment"


class Kind178(Enum):
    volume_attachment_list = "VolumeAttachmentList"


class Kind179(Enum):
    custom_resource_definition = "CustomResourceDefinition"


class Kind180(Enum):
    custom_resource_definition_list = "CustomResourceDefinitionList"


class Kind181(Enum):
    custom_resource_definition = "CustomResourceDefinition"


class Kind182(Enum):
    custom_resource_definition_list = "CustomResourceDefinitionList"


class Kind183(Enum):
    api_group = "APIGroup"


class Kind184(Enum):
    api_group_list = "APIGroupList"


class Kind185(Enum):
    api_resource_list = "APIResourceList"


class Kind186(Enum):
    api_versions = "APIVersions"


class Kind187(Enum):
    delete_options = "DeleteOptions"


class Kind188(Enum):
    status = "Status"


class Kind189(Enum):
    api_service = "APIService"


class Kind190(Enum):
    api_service_list = "APIServiceList"


class Kind191(Enum):
    api_service = "APIService"


class Kind192(Enum):
    api_service_list = "APIServiceList"
