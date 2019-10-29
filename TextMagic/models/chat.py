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


class Chat(object):
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
        'original_id': 'int',
        'phone': 'str',
        'contact': 'Contact',
        'unsubscribed_contact_id': 'int',
        'unread': 'int',
        'updated_at': 'datetime',
        'status': 'str',
        'mute': 'int',
        'last_message': 'str',
        'direction': 'str',
        '_from': 'str',
        'muted_until': 'datetime',
        'time_left_mute': 'int',
        'country': 'Country'
    }

    attribute_map = {
        'id': 'id',
        'original_id': 'originalId',
        'phone': 'phone',
        'contact': 'contact',
        'unsubscribed_contact_id': 'unsubscribedContactId',
        'unread': 'unread',
        'updated_at': 'updatedAt',
        'status': 'status',
        'mute': 'mute',
        'last_message': 'lastMessage',
        'direction': 'direction',
        '_from': 'from',
        'muted_until': 'mutedUntil',
        'time_left_mute': 'timeLeftMute',
        'country': 'country'
    }

    def __init__(self, id=None, original_id=None, phone=None, contact=None, unsubscribed_contact_id=None, unread=None, updated_at=None, status=None, mute=None, last_message=None, direction=None, _from=None, muted_until=None, time_left_mute=None, country=None):  # noqa: E501
        """Chat - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._original_id = None
        self._phone = None
        self._contact = None
        self._unsubscribed_contact_id = None
        self._unread = None
        self._updated_at = None
        self._status = None
        self._mute = None
        self._last_message = None
        self._direction = None
        self.__from = None
        self._muted_until = None
        self._time_left_mute = None
        self._country = None
        self.discriminator = None

        self.id = id
        self.original_id = original_id
        self.phone = phone
        self.contact = contact
        self.unsubscribed_contact_id = unsubscribed_contact_id
        self.unread = unread
        self.updated_at = updated_at
        self.status = status
        self.mute = mute
        self.last_message = last_message
        self.direction = direction
        self._from = _from
        self.muted_until = muted_until
        self.time_left_mute = time_left_mute
        self.country = country

    @property
    def id(self):
        """Gets the id of this Chat.  # noqa: E501

        Chat ID.  # noqa: E501

        :return: The id of this Chat.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Chat.

        Chat ID.  # noqa: E501

        :param id: The id of this Chat.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def original_id(self):
        """Gets the original_id of this Chat.  # noqa: E501


        :return: The original_id of this Chat.  # noqa: E501
        :rtype: int
        """
        return self._original_id

    @original_id.setter
    def original_id(self, original_id):
        """Sets the original_id of this Chat.


        :param original_id: The original_id of this Chat.  # noqa: E501
        :type: int
        """

        self._original_id = original_id

    @property
    def phone(self):
        """Gets the phone of this Chat.  # noqa: E501

        Chat partner's phone number.  # noqa: E501

        :return: The phone of this Chat.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Chat.

        Chat partner's phone number.  # noqa: E501

        :param phone: The phone of this Chat.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def contact(self):
        """Gets the contact of this Chat.  # noqa: E501


        :return: The contact of this Chat.  # noqa: E501
        :rtype: Contact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Chat.


        :param contact: The contact of this Chat.  # noqa: E501
        :type: Contact
        """

        self._contact = contact

    @property
    def unsubscribed_contact_id(self):
        """Gets the unsubscribed_contact_id of this Chat.  # noqa: E501

        If this field has a value, it means that the chat phone number has been unsubscribed from you and this value is an ID of an Unsubscribed contact entity. See [Get all unsubscribed contacts](http://docs.textmagictesting.com/#operation/getUnsubscribers).  # noqa: E501

        :return: The unsubscribed_contact_id of this Chat.  # noqa: E501
        :rtype: int
        """
        return self._unsubscribed_contact_id

    @unsubscribed_contact_id.setter
    def unsubscribed_contact_id(self, unsubscribed_contact_id):
        """Sets the unsubscribed_contact_id of this Chat.

        If this field has a value, it means that the chat phone number has been unsubscribed from you and this value is an ID of an Unsubscribed contact entity. See [Get all unsubscribed contacts](http://docs.textmagictesting.com/#operation/getUnsubscribers).  # noqa: E501

        :param unsubscribed_contact_id: The unsubscribed_contact_id of this Chat.  # noqa: E501
        :type: int
        """

        self._unsubscribed_contact_id = unsubscribed_contact_id

    @property
    def unread(self):
        """Gets the unread of this Chat.  # noqa: E501

        Total unread incoming messages.  # noqa: E501

        :return: The unread of this Chat.  # noqa: E501
        :rtype: int
        """
        return self._unread

    @unread.setter
    def unread(self, unread):
        """Sets the unread of this Chat.

        Total unread incoming messages.  # noqa: E501

        :param unread: The unread of this Chat.  # noqa: E501
        :type: int
        """

        self._unread = unread

    @property
    def updated_at(self):
        """Gets the updated_at of this Chat.  # noqa: E501

        Time when the last incoming message arrived at this chat.  # noqa: E501

        :return: The updated_at of this Chat.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Chat.

        Time when the last incoming message arrived at this chat.  # noqa: E501

        :param updated_at: The updated_at of this Chat.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def status(self):
        """Gets the status of this Chat.  # noqa: E501

        Chat status:   * **a** - Active;   * **c** - Closed;   * **d** - Deleted.   # noqa: E501

        :return: The status of this Chat.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Chat.

        Chat status:   * **a** - Active;   * **c** - Closed;   * **d** - Deleted.   # noqa: E501

        :param status: The status of this Chat.  # noqa: E501
        :type: str
        """
        allowed_values = ["a", "c", "d"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def mute(self):
        """Gets the mute of this Chat.  # noqa: E501

        Indicates when the chat is muted.  # noqa: E501

        :return: The mute of this Chat.  # noqa: E501
        :rtype: int
        """
        return self._mute

    @mute.setter
    def mute(self, mute):
        """Sets the mute of this Chat.

        Indicates when the chat is muted.  # noqa: E501

        :param mute: The mute of this Chat.  # noqa: E501
        :type: int
        """

        self._mute = mute

    @property
    def last_message(self):
        """Gets the last_message of this Chat.  # noqa: E501

        The last message content of a chat.  # noqa: E501

        :return: The last_message of this Chat.  # noqa: E501
        :rtype: str
        """
        return self._last_message

    @last_message.setter
    def last_message(self, last_message):
        """Sets the last_message of this Chat.

        The last message content of a chat.  # noqa: E501

        :param last_message: The last_message of this Chat.  # noqa: E501
        :type: str
        """

        self._last_message = last_message

    @property
    def direction(self):
        """Gets the direction of this Chat.  # noqa: E501

        Last message type: * **ci** - incoming call; * **co** - outgoing call; * **i** - incoming message; * **o** - outgoing message.   # noqa: E501

        :return: The direction of this Chat.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this Chat.

        Last message type: * **ci** - incoming call; * **co** - outgoing call; * **i** - incoming message; * **o** - outgoing message.   # noqa: E501

        :param direction: The direction of this Chat.  # noqa: E501
        :type: str
        """
        allowed_values = ["ci", "co", "i", "o"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def _from(self):
        """Gets the _from of this Chat.  # noqa: E501

        If filled, the value will be used as a sender number for all outgoing messages of a chat.  # noqa: E501

        :return: The _from of this Chat.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this Chat.

        If filled, the value will be used as a sender number for all outgoing messages of a chat.  # noqa: E501

        :param _from: The _from of this Chat.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def muted_until(self):
        """Gets the muted_until of this Chat.  # noqa: E501

        Date and time until the chat will be muted.  # noqa: E501

        :return: The muted_until of this Chat.  # noqa: E501
        :rtype: datetime
        """
        return self._muted_until

    @muted_until.setter
    def muted_until(self, muted_until):
        """Sets the muted_until of this Chat.

        Date and time until the chat will be muted.  # noqa: E501

        :param muted_until: The muted_until of this Chat.  # noqa: E501
        :type: datetime
        """

        self._muted_until = muted_until

    @property
    def time_left_mute(self):
        """Gets the time_left_mute of this Chat.  # noqa: E501

        Time left untill the chat will be unmuted (seconds).  # noqa: E501

        :return: The time_left_mute of this Chat.  # noqa: E501
        :rtype: int
        """
        return self._time_left_mute

    @time_left_mute.setter
    def time_left_mute(self, time_left_mute):
        """Sets the time_left_mute of this Chat.

        Time left untill the chat will be unmuted (seconds).  # noqa: E501

        :param time_left_mute: The time_left_mute of this Chat.  # noqa: E501
        :type: int
        """

        self._time_left_mute = time_left_mute

    @property
    def country(self):
        """Gets the country of this Chat.  # noqa: E501


        :return: The country of this Chat.  # noqa: E501
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Chat.


        :param country: The country of this Chat.  # noqa: E501
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
        if issubclass(Chat, dict):
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
        if not isinstance(other, Chat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
