# coding: utf-8

"""
    TextMagic API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InviteSubaccountInputObject(object):
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
        'email': 'str',
        'role': 'str'
    }

    attribute_map = {
        'email': 'email',
        'role': 'role'
    }

    def __init__(self, email=None, role=None):  # noqa: E501
        """InviteSubaccountInputObject - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._role = None
        self.discriminator = None

        self.email = email
        self.role = role

    @property
    def email(self):
        """Gets the email of this InviteSubaccountInputObject.  # noqa: E501

        Invitation email will be sent to this email address.  # noqa: E501

        :return: The email of this InviteSubaccountInputObject.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InviteSubaccountInputObject.

        Invitation email will be sent to this email address.  # noqa: E501

        :param email: The email of this InviteSubaccountInputObject.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def role(self):
        """Gets the role of this InviteSubaccountInputObject.  # noqa: E501

        Type of account: *   **A** for Administrator sub-account *   **U** for Regular User   # noqa: E501

        :return: The role of this InviteSubaccountInputObject.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this InviteSubaccountInputObject.

        Type of account: *   **A** for Administrator sub-account *   **U** for Regular User   # noqa: E501

        :param role: The role of this InviteSubaccountInputObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "U"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

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
        if issubclass(InviteSubaccountInputObject, dict):
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
        if not isinstance(other, InviteSubaccountInputObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
