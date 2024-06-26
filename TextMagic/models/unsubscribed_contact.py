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


class UnsubscribedContact(object):
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
        'phone': 'str',
        'unsubscribe_time': 'datetime',
        'first_name': 'str',
        'last_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'phone': 'phone',
        'unsubscribe_time': 'unsubscribeTime',
        'first_name': 'firstName',
        'last_name': 'lastName'
    }

    def __init__(self, id=None, phone=None, unsubscribe_time=None, first_name=None, last_name=None):  # noqa: E501
        """UnsubscribedContact - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._phone = None
        self._unsubscribe_time = None
        self._first_name = None
        self._last_name = None
        self.discriminator = None

        self.id = id
        self.phone = phone
        self.unsubscribe_time = unsubscribe_time
        self.first_name = first_name
        self.last_name = last_name

    @property
    def id(self):
        """Gets the id of this UnsubscribedContact.  # noqa: E501

        Unsubscribed contact ID.  # noqa: E501

        :return: The id of this UnsubscribedContact.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UnsubscribedContact.

        Unsubscribed contact ID.  # noqa: E501

        :param id: The id of this UnsubscribedContact.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def phone(self):
        """Gets the phone of this UnsubscribedContact.  # noqa: E501

        Phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164).  # noqa: E501

        :return: The phone of this UnsubscribedContact.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UnsubscribedContact.

        Phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164).  # noqa: E501

        :param phone: The phone of this UnsubscribedContact.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def unsubscribe_time(self):
        """Gets the unsubscribe_time of this UnsubscribedContact.  # noqa: E501

        Time when contact was opted-out.  # noqa: E501

        :return: The unsubscribe_time of this UnsubscribedContact.  # noqa: E501
        :rtype: datetime
        """
        return self._unsubscribe_time

    @unsubscribe_time.setter
    def unsubscribe_time(self, unsubscribe_time):
        """Sets the unsubscribe_time of this UnsubscribedContact.

        Time when contact was opted-out.  # noqa: E501

        :param unsubscribe_time: The unsubscribe_time of this UnsubscribedContact.  # noqa: E501
        :type: datetime
        """

        self._unsubscribe_time = unsubscribe_time

    @property
    def first_name(self):
        """Gets the first_name of this UnsubscribedContact.  # noqa: E501

        Unsubscribed contact first name.  # noqa: E501

        :return: The first_name of this UnsubscribedContact.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UnsubscribedContact.

        Unsubscribed contact first name.  # noqa: E501

        :param first_name: The first_name of this UnsubscribedContact.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UnsubscribedContact.  # noqa: E501

        Unsubscribed contact last name.  # noqa: E501

        :return: The last_name of this UnsubscribedContact.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UnsubscribedContact.

        Unsubscribed contact last name.  # noqa: E501

        :param last_name: The last_name of this UnsubscribedContact.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

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
        if issubclass(UnsubscribedContact, dict):
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
        if not isinstance(other, UnsubscribedContact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
