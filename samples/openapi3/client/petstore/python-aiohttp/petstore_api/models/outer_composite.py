# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictBool, StrictStr

class OuterComposite(BaseModel):
    """
    OuterComposite
    """
    my_number: Optional[float] = None
    my_string: Optional[StrictStr] = None
    my_boolean: Optional[StrictBool] = None
    __properties = ["my_number", "my_string", "my_boolean"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> OuterComposite:
        """Create an instance of OuterComposite from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OuterComposite:
        """Create an instance of OuterComposite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OuterComposite.model_validate(obj)

        _obj = OuterComposite.model_validate({
            "my_number": obj.get("my_number"),
            "my_string": obj.get("my_string"),
            "my_boolean": obj.get("my_boolean")
        })
        return _obj


