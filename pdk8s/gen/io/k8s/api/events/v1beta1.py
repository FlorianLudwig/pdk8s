# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

import pdk8s.model

from ..... import Kind104, Kind105
from ...apimachinery.pkg.apis.meta import v1
from ..core import v1 as v1_1


class EventSeries(BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "forbid"

    count: int = Field(
        ...,
        description="Number of occurrences in this series up to the last heartbeat time",
    )
    last_observed_time: v1.MicroTime = Field(
        ...,
        alias="lastObservedTime",
        description="Time when last Event from the series was seen before last heartbeat.",
    )
    state: str = Field(
        ...,
        description="Information whether this series is ongoing or finished. Deprecated. Planned removal for 1.18",
    )


class Event(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    action: Optional[str] = Field(
        None,
        description="What action was taken/failed regarding to the regarding object.",
    )
    api_version: Optional[str] = Field(
        "events.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    deprecated_count: Optional[int] = Field(
        None,
        alias="deprecatedCount",
        description="Deprecated field assuring backward compatibility with core.v1 Event type",
    )
    deprecated_first_timestamp: Optional[v1.Time] = Field(
        None,
        alias="deprecatedFirstTimestamp",
        description="Deprecated field assuring backward compatibility with core.v1 Event type",
    )
    deprecated_last_timestamp: Optional[v1.Time] = Field(
        None,
        alias="deprecatedLastTimestamp",
        description="Deprecated field assuring backward compatibility with core.v1 Event type",
    )
    deprecated_source: Optional[v1_1.EventSource] = Field(
        None,
        alias="deprecatedSource",
        description="Deprecated field assuring backward compatibility with core.v1 Event type",
    )
    event_time: v1.MicroTime = Field(
        ...,
        alias="eventTime",
        description="Required. Time when this Event was first observed.",
    )
    kind: Optional[Kind104] = Field(
        "Event",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = None
    note: Optional[str] = Field(
        None,
        description="Optional. A human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB.",
    )
    reason: Optional[str] = Field(None, description="Why the action was taken.")
    regarding: Optional[v1_1.ObjectReference] = Field(
        None,
        description="The object this Event is about. In most cases it's an Object reporting controller implements. E.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object.",
    )
    related: Optional[v1_1.ObjectReference] = Field(
        None,
        description="Optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object.",
    )
    reporting_controller: Optional[str] = Field(
        None,
        alias="reportingController",
        description="Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.",
    )
    reporting_instance: Optional[str] = Field(
        None,
        alias="reportingInstance",
        description="ID of the controller instance, e.g. `kubelet-xyzf`.",
    )
    series: Optional[EventSeries] = Field(
        None,
        description="Data about the Event series this event represents or nil if it's a singleton Event.",
    )
    type: Optional[str] = Field(
        None,
        description="Type of this event (Normal, Warning), new types could be added in the future.",
    )


class EventList(pdk8s.model.NamedModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        extra = "allow"

    api_version: Optional[str] = Field(
        "events.k8s.io/v1beta1",
        alias="apiVersion",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[Event] = Field(..., description="Items is a list of schema objects.")
    kind: Optional[Kind105] = Field(
        "EventList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
