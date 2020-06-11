# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Kind57, Kind58
from ...apimachinery.pkg.apis.meta import v1
from ..core import v1 as v1_1


class JobCondition(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    last_probe_time: Optional[v1.Time] = Field(
        None, alias="lastProbeTime", description="Last time the condition was checked."
    )
    last_transition_time: Optional[v1.Time] = Field(
        None,
        alias="lastTransitionTime",
        description="Last time the condition transit from one status to another.",
    )
    message: Optional[str] = Field(
        None,
        description="Human readable message indicating details about last transition.",
    )
    reason: Optional[str] = Field(
        None, description="(brief) reason for the condition's last transition."
    )
    type: str = Field(..., description="Type of job condition, Complete or Failed.")


class JobStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    active: Optional[int] = Field(
        None, description="The number of actively running pods."
    )
    completion_time: Optional[v1.Time] = Field(
        None,
        alias="completionTime",
        description="Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.",
    )
    conditions: Optional[List[JobCondition]] = Field(
        None,
        description="The latest available observations of an object's current state. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/",
    )
    failed: Optional[int] = Field(
        None, description="The number of pods which reached phase Failed."
    )
    start_time: Optional[v1.Time] = Field(
        None,
        alias="startTime",
        description="Represents time when the job was acknowledged by the job controller. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.",
    )
    succeeded: Optional[int] = Field(
        None, description="The number of pods which reached phase Succeeded."
    )


class JobSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    active_deadline_seconds: Optional[int] = Field(
        None,
        alias="activeDeadlineSeconds",
        description="Specifies the duration in seconds relative to the startTime that the job may be active before the system tries to terminate it; value must be positive integer",
    )
    backoff_limit: Optional[int] = Field(
        None,
        alias="backoffLimit",
        description="Specifies the number of retries before marking this job failed. Defaults to 6",
    )
    completions: Optional[int] = Field(
        None,
        description="Specifies the desired number of successfully finished pods the job should be run with.  Setting to nil means that the success of any pod signals the success of all pods, and allows parallelism to have any positive value.  Setting to 1 means that parallelism is limited to 1 and the success of that pod signals the success of the job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/",
    )
    manual_selector: Optional[bool] = Field(
        None,
        alias="manualSelector",
        description="manualSelector controls generation of pod labels and pod selectors. Leave `manualSelector` unset unless you are certain what you are doing. When false or unset, the system pick labels unique to this job and appends those labels to the pod template.  When true, the user is responsible for picking unique labels and specifying the selector.  Failure to pick a unique label may cause this and other jobs to not function correctly.  However, You may see `manualSelector=true` in jobs that were created with the old `extensions/v1beta1` API. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#specifying-your-own-pod-selector",
    )
    parallelism: Optional[int] = Field(
        None,
        description="Specifies the maximum desired number of pods the job should run at any given time. The actual number of pods running in steady state will be less than this number when ((.spec.completions - .status.successful) < .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/",
    )
    selector: Optional[v1.LabelSelector] = Field(
        None,
        description="A label query over pods that should match the pod count. Normally, the system sets this field for you. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors",
    )
    template: v1_1.PodTemplateSpec = Field(
        ...,
        description="Describes the pod that will be created when executing a job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/",
    )
    ttl_seconds_after_finished: Optional[int] = Field(
        None,
        alias="ttlSecondsAfterFinished",
        description="ttlSecondsAfterFinished limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, ttlSecondsAfterFinished after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is unset, the Job won't be automatically deleted. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes. This field is alpha-level and is only honored by servers that enable the TTLAfterFinished feature.",
    )


class Job(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "batch/v1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind57] = Field(
        "Job",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[JobSpec] = Field(
        None,
        description="Specification of the desired behavior of a job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class JobList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "batch/v1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[Job] = Field(..., description="items is the list of Jobs.")
    kind: Optional[Kind58] = Field(
        "JobList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
