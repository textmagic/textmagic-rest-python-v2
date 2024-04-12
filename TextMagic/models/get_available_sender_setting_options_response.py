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


class GetAvailableSenderSettingOptionsResponse(object):
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
        'dedicated': 'list[str]',
        'user': 'list[str]',
        'shared': 'list[str]',
        'sender_ids': 'list[str]',
        'user_carrier_twilio': 'list[str]',
        'user_carrier_vonage': 'list[str]'
    }

    attribute_map = {
        'dedicated': 'dedicated',
        'user': 'user',
        'shared': 'shared',
        'sender_ids': 'senderIds',
        'user_carrier_twilio': 'userCarrierTwilio',
        'user_carrier_vonage': 'userCarrierVonage'
    }

    def __init__(self, dedicated=None, user=None, shared=None, sender_ids=None, user_carrier_twilio=None, user_carrier_vonage=None):  # noqa: E501
        """GetAvailableSenderSettingOptionsResponse - a model defined in Swagger"""  # noqa: E501

        self._dedicated = None
        self._user = None
        self._shared = None
        self._sender_ids = None
        self._user_carrier_twilio = None
        self._user_carrier_vonage = None
        self.discriminator = None

        self.dedicated = dedicated
        self.user = user
        self.shared = shared
        self.sender_ids = sender_ids
        self.user_carrier_twilio = user_carrier_twilio
        self.user_carrier_vonage = user_carrier_vonage

    @property
    def dedicated(self):
        """Gets the dedicated of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501

        Array of dedicated number strings.  # noqa: E501

        :return: The dedicated of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._dedicated

    @dedicated.setter
    def dedicated(self, dedicated):
        """Sets the dedicated of this GetAvailableSenderSettingOptionsResponse.

        Array of dedicated number strings.  # noqa: E501

        :param dedicated: The dedicated of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :type: list[str]
        """

        self._dedicated = dedicated

    @property
    def user(self):
        """Gets the user of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501

        Array of verified account phone numbers (currently only one).  # noqa: E501

        :return: The user of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this GetAvailableSenderSettingOptionsResponse.

        Array of verified account phone numbers (currently only one).  # noqa: E501

        :param user: The user of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :type: list[str]
        """

        self._user = user

    @property
    def shared(self):
        """Gets the shared of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501

        Array of shared number strings.  # noqa: E501

        :return: The shared of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this GetAvailableSenderSettingOptionsResponse.

        Array of shared number strings.  # noqa: E501

        :param shared: The shared of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :type: list[str]
        """

        self._shared = shared

    @property
    def sender_ids(self):
        """Gets the sender_ids of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501

        Array of alphanumeric sender IDs.  # noqa: E501

        :return: The sender_ids of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._sender_ids

    @sender_ids.setter
    def sender_ids(self, sender_ids):
        """Sets the sender_ids of this GetAvailableSenderSettingOptionsResponse.

        Array of alphanumeric sender IDs.  # noqa: E501

        :param sender_ids: The sender_ids of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :type: list[str]
        """

        self._sender_ids = sender_ids

    @property
    def user_carrier_twilio(self):
        """Gets the user_carrier_twilio of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501

        Array of alphanumeric sender IDs.  # noqa: E501

        :return: The user_carrier_twilio of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_carrier_twilio

    @user_carrier_twilio.setter
    def user_carrier_twilio(self, user_carrier_twilio):
        """Sets the user_carrier_twilio of this GetAvailableSenderSettingOptionsResponse.

        Array of alphanumeric sender IDs.  # noqa: E501

        :param user_carrier_twilio: The user_carrier_twilio of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :type: list[str]
        """

        self._user_carrier_twilio = user_carrier_twilio

    @property
    def user_carrier_vonage(self):
        """Gets the user_carrier_vonage of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501

        Array of alphanumeric sender IDs.  # noqa: E501

        :return: The user_carrier_vonage of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_carrier_vonage

    @user_carrier_vonage.setter
    def user_carrier_vonage(self, user_carrier_vonage):
        """Sets the user_carrier_vonage of this GetAvailableSenderSettingOptionsResponse.

        Array of alphanumeric sender IDs.  # noqa: E501

        :param user_carrier_vonage: The user_carrier_vonage of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :type: list[str]
        """

        self._user_carrier_vonage = user_carrier_vonage

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
        if issubclass(GetAvailableSenderSettingOptionsResponse, dict):
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
        if not isinstance(other, GetAvailableSenderSettingOptionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
