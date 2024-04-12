# coding: utf-8

"""
    Textmagic API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CustomFieldListItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'value': 'str'
    }

    attribute_map = {
        'id': 'id',
        'value': 'value'
    }

    def __init__(self, id=None, value=None):  # noqa: E501
        """CustomFieldListItem - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._value = None
        self.discriminator = None

        self.id = id
        self.value = value

    @property
    def id(self):
        """Gets the id of this CustomFieldListItem.  # noqa: E501

        Custom Field ID.  # noqa: E501

        :return: The id of this CustomFieldListItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomFieldListItem.

        Custom Field ID.  # noqa: E501

        :param id: The id of this CustomFieldListItem.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def value(self):
        """Gets the value of this CustomFieldListItem.  # noqa: E501

        Custom Field value.  # noqa: E501

        :return: The value of this CustomFieldListItem.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CustomFieldListItem.

        Custom Field value.  # noqa: E501

        :param value: The value of this CustomFieldListItem.  # noqa: E501
        :type: str
        """

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CustomFieldListItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomFieldListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
