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


class UsersInbound(object):
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
        'display_time_format': 'str',
        'phone': 'str',
        'user': 'User',
        'purchased_at': 'datetime',
        'expire_at': 'datetime',
        'status': 'str',
        'country': 'Country'
    }

    attribute_map = {
        'id': 'id',
        'display_time_format': 'displayTimeFormat',
        'phone': 'phone',
        'user': 'user',
        'purchased_at': 'purchasedAt',
        'expire_at': 'expireAt',
        'status': 'status',
        'country': 'country'
    }

    def __init__(self, id=None, display_time_format=None, phone=None, user=None, purchased_at=None, expire_at=None, status=None, country=None):  # noqa: E501
        """UsersInbound - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._display_time_format = None
        self._phone = None
        self._user = None
        self._purchased_at = None
        self._expire_at = None
        self._status = None
        self._country = None
        self.discriminator = None

        self.id = id
        if display_time_format is not None:
            self.display_time_format = display_time_format
        if phone is not None:
            self.phone = phone
        self.user = user
        self.purchased_at = purchased_at
        self.expire_at = expire_at
        self.status = status
        self.country = country

    @property
    def id(self):
        """Gets the id of this UsersInbound.  # noqa: E501

        Dedicated number ID.  # noqa: E501

        :return: The id of this UsersInbound.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UsersInbound.

        Dedicated number ID.  # noqa: E501

        :param id: The id of this UsersInbound.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def display_time_format(self):
        """Gets the display_time_format of this UsersInbound.  # noqa: E501

        Format for representation of time  # noqa: E501

        :return: The display_time_format of this UsersInbound.  # noqa: E501
        :rtype: str
        """
        return self._display_time_format

    @display_time_format.setter
    def display_time_format(self, display_time_format):
        """Sets the display_time_format of this UsersInbound.

        Format for representation of time  # noqa: E501

        :param display_time_format: The display_time_format of this UsersInbound.  # noqa: E501
        :type: str
        """

        self._display_time_format = display_time_format

    @property
    def phone(self):
        """Gets the phone of this UsersInbound.  # noqa: E501

        Dedicated phone number.  # noqa: E501

        :return: The phone of this UsersInbound.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UsersInbound.

        Dedicated phone number.  # noqa: E501

        :param phone: The phone of this UsersInbound.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def user(self):
        """Gets the user of this UsersInbound.  # noqa: E501


        :return: The user of this UsersInbound.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UsersInbound.


        :param user: The user of this UsersInbound.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def purchased_at(self):
        """Gets the purchased_at of this UsersInbound.  # noqa: E501

        Time when the dedicated number was purchased.  # noqa: E501

        :return: The purchased_at of this UsersInbound.  # noqa: E501
        :rtype: datetime
        """
        return self._purchased_at

    @purchased_at.setter
    def purchased_at(self, purchased_at):
        """Sets the purchased_at of this UsersInbound.

        Time when the dedicated number was purchased.  # noqa: E501

        :param purchased_at: The purchased_at of this UsersInbound.  # noqa: E501
        :type: datetime
        """

        self._purchased_at = purchased_at

    @property
    def expire_at(self):
        """Gets the expire_at of this UsersInbound.  # noqa: E501

        Dedicated number subscription expiration time.  # noqa: E501

        :return: The expire_at of this UsersInbound.  # noqa: E501
        :rtype: datetime
        """
        return self._expire_at

    @expire_at.setter
    def expire_at(self, expire_at):
        """Sets the expire_at of this UsersInbound.

        Dedicated number subscription expiration time.  # noqa: E501

        :param expire_at: The expire_at of this UsersInbound.  # noqa: E501
        :type: datetime
        """

        self._expire_at = expire_at

    @property
    def status(self):
        """Gets the status of this UsersInbound.  # noqa: E501

        Number status: *   **U** for Unused. No messages have been sent from (or received to) this number; *   **A** for Active.   # noqa: E501

        :return: The status of this UsersInbound.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UsersInbound.

        Number status: *   **U** for Unused. No messages have been sent from (or received to) this number; *   **A** for Active.   # noqa: E501

        :param status: The status of this UsersInbound.  # noqa: E501
        :type: str
        """
        allowed_values = ["U", "A"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def country(self):
        """Gets the country of this UsersInbound.  # noqa: E501


        :return: The country of this UsersInbound.  # noqa: E501
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this UsersInbound.


        :param country: The country of this UsersInbound.  # noqa: E501
        :type: Country
        """

        self._country = country

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
        if issubclass(UsersInbound, dict):
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
        if not isinstance(other, UsersInbound):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
