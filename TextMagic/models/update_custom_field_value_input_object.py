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


class UpdateCustomFieldValueInputObject(object):
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
        'contact_id': 'int',
        'value': 'str'
    }

    attribute_map = {
        'contact_id': 'contactId',
        'value': 'value'
    }

    def __init__(self, contact_id=None, value=None):  # noqa: E501
        """UpdateCustomFieldValueInputObject - a model defined in Swagger"""  # noqa: E501

        self._contact_id = None
        self._value = None
        self.discriminator = None

        if contact_id is not None:
            self.contact_id = contact_id
        if value is not None:
            self.value = value

    @property
    def contact_id(self):
        """Gets the contact_id of this UpdateCustomFieldValueInputObject.  # noqa: E501

        Contact ID. See [Contact](https://docs.textmagic.com/#tag/Contacts).   # noqa: E501

        :return: The contact_id of this UpdateCustomFieldValueInputObject.  # noqa: E501
        :rtype: int
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this UpdateCustomFieldValueInputObject.

        Contact ID. See [Contact](https://docs.textmagic.com/#tag/Contacts).   # noqa: E501

        :param contact_id: The contact_id of this UpdateCustomFieldValueInputObject.  # noqa: E501
        :type: int
        """

        self._contact_id = contact_id

    @property
    def value(self):
        """Gets the value of this UpdateCustomFieldValueInputObject.  # noqa: E501

        Custom field value. Note that this value is not parsed in any way; it is stored and used in tags exactly as you send it.  # noqa: E501

        :return: The value of this UpdateCustomFieldValueInputObject.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UpdateCustomFieldValueInputObject.

        Custom field value. Note that this value is not parsed in any way; it is stored and used in tags exactly as you send it.  # noqa: E501

        :param value: The value of this UpdateCustomFieldValueInputObject.  # noqa: E501
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
        if issubclass(UpdateCustomFieldValueInputObject, dict):
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
        if not isinstance(other, UpdateCustomFieldValueInputObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
