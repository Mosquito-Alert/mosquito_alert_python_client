# coding: utf-8

"""
    Mosquito Alert API

    Introducing API v1 for Mosquito Alert platform, a project desgined to facilitate citizen science initiatives and enable collaboration among scientists, public health officials, and environmental managers in the investigation and control of disease-carrying mosquitoes.

    The version of the OpenAPI document: v1
    Contact: it@mosquitoalert.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mosquito_alert_api.models.device_request import DeviceRequest
from mosquito_alert_api.models.package_request import PackageRequest
from mosquito_alert_api.models.report_location_request import ReportLocationRequest
from mosquito_alert_api.models.report_photo_request import ReportPhotoRequest
from typing import Optional, Set
from typing_extensions import Self

class ObservationRequest(BaseModel):
    """
    ObservationRequest
    """ # noqa: E501
    created_at: datetime
    sent_at: datetime
    location: ReportLocationRequest
    note: Optional[StrictStr] = Field(default=None, description="Note user attached to report.")
    tags: Optional[List[Annotated[str, Field(min_length=1, strict=True)]]] = None
    package: Optional[PackageRequest] = None
    device: Optional[DeviceRequest] = None
    photos: List[ReportPhotoRequest]
    event_environment: Optional[StrictStr] = Field(default=None, description="The environment where the event took place.")
    event_moment: Optional[StrictStr] = Field(default=None, description="The moment of the day when the event took place.")
    user_perceived_mosquito_specie: Optional[StrictStr] = Field(default=None, description="The mosquito specie perceived by the user.")
    user_perceived_mosquito_thorax: Optional[StrictStr] = Field(default=None, description="The species of mosquito that the thorax resembles, according to the user.")
    user_perceived_mosquito_abdomen: Optional[StrictStr] = Field(default=None, description="The species of mosquito that the abdomen resembles, according to the user.")
    user_perceived_mosquito_legs: Optional[StrictStr] = Field(default=None, description="The species of mosquito that the leg resembles, according to the user.")
    __properties: ClassVar[List[str]] = ["created_at", "sent_at", "location", "note", "tags", "package", "device", "photos", "event_environment", "event_moment", "user_perceived_mosquito_specie", "user_perceived_mosquito_thorax", "user_perceived_mosquito_abdomen", "user_perceived_mosquito_legs"]

    @field_validator('event_environment')
    def event_environment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['indoors', 'outdoors', 'vehicle', '']):
            raise ValueError("must be one of enum values ('indoors', 'outdoors', 'vehicle', '')")
        return value

    @field_validator('event_moment')
    def event_moment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['now', 'last_morning', 'last_midday', 'last_afternoon', 'last_night', '']):
            raise ValueError("must be one of enum values ('now', 'last_morning', 'last_midday', 'last_afternoon', 'last_night', '')")
        return value

    @field_validator('user_perceived_mosquito_specie')
    def user_perceived_mosquito_specie_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['albopictus', 'aegypti', 'japonicus', 'koreicus', 'culex', 'other', '']):
            raise ValueError("must be one of enum values ('albopictus', 'aegypti', 'japonicus', 'koreicus', 'culex', 'other', '')")
        return value

    @field_validator('user_perceived_mosquito_thorax')
    def user_perceived_mosquito_thorax_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['albopictus', 'aegypti', 'japonicus', 'koreicus', 'culex', 'other', '']):
            raise ValueError("must be one of enum values ('albopictus', 'aegypti', 'japonicus', 'koreicus', 'culex', 'other', '')")
        return value

    @field_validator('user_perceived_mosquito_abdomen')
    def user_perceived_mosquito_abdomen_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['albopictus', 'aegypti', 'japonicus', 'koreicus', 'culex', 'other', '']):
            raise ValueError("must be one of enum values ('albopictus', 'aegypti', 'japonicus', 'koreicus', 'culex', 'other', '')")
        return value

    @field_validator('user_perceived_mosquito_legs')
    def user_perceived_mosquito_legs_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['albopictus', 'aegypti', 'japonicus', 'koreicus', 'culex', 'other', '']):
            raise ValueError("must be one of enum values ('albopictus', 'aegypti', 'japonicus', 'koreicus', 'culex', 'other', '')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ObservationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of package
        if self.package:
            _dict['package'] = self.package.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device
        if self.device:
            _dict['device'] = self.device.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in photos (list)
        _items = []
        if self.photos:
            for _item_photos in self.photos:
                if _item_photos:
                    _items.append(_item_photos.to_dict())
            _dict['photos'] = _items
        # set to None if note (nullable) is None
        # and model_fields_set contains the field
        if self.note is None and "note" in self.model_fields_set:
            _dict['note'] = None

        # set to None if event_environment (nullable) is None
        # and model_fields_set contains the field
        if self.event_environment is None and "event_environment" in self.model_fields_set:
            _dict['event_environment'] = None

        # set to None if event_moment (nullable) is None
        # and model_fields_set contains the field
        if self.event_moment is None and "event_moment" in self.model_fields_set:
            _dict['event_moment'] = None

        # set to None if user_perceived_mosquito_specie (nullable) is None
        # and model_fields_set contains the field
        if self.user_perceived_mosquito_specie is None and "user_perceived_mosquito_specie" in self.model_fields_set:
            _dict['user_perceived_mosquito_specie'] = None

        # set to None if user_perceived_mosquito_thorax (nullable) is None
        # and model_fields_set contains the field
        if self.user_perceived_mosquito_thorax is None and "user_perceived_mosquito_thorax" in self.model_fields_set:
            _dict['user_perceived_mosquito_thorax'] = None

        # set to None if user_perceived_mosquito_abdomen (nullable) is None
        # and model_fields_set contains the field
        if self.user_perceived_mosquito_abdomen is None and "user_perceived_mosquito_abdomen" in self.model_fields_set:
            _dict['user_perceived_mosquito_abdomen'] = None

        # set to None if user_perceived_mosquito_legs (nullable) is None
        # and model_fields_set contains the field
        if self.user_perceived_mosquito_legs is None and "user_perceived_mosquito_legs" in self.model_fields_set:
            _dict['user_perceived_mosquito_legs'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObservationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "sent_at": obj.get("sent_at"),
            "location": ReportLocationRequest.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "note": obj.get("note"),
            "tags": obj.get("tags"),
            "package": PackageRequest.from_dict(obj["package"]) if obj.get("package") is not None else None,
            "device": DeviceRequest.from_dict(obj["device"]) if obj.get("device") is not None else None,
            "photos": [ReportPhotoRequest.from_dict(_item) for _item in obj["photos"]] if obj.get("photos") is not None else None,
            "event_environment": obj.get("event_environment"),
            "event_moment": obj.get("event_moment"),
            "user_perceived_mosquito_specie": obj.get("user_perceived_mosquito_specie"),
            "user_perceived_mosquito_thorax": obj.get("user_perceived_mosquito_thorax"),
            "user_perceived_mosquito_abdomen": obj.get("user_perceived_mosquito_abdomen"),
            "user_perceived_mosquito_legs": obj.get("user_perceived_mosquito_legs")
        })
        return _obj

