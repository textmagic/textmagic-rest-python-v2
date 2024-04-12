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


class GetVersionsResponse(object):
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
        'ios': 'str',
        'android': 'str',
        'desktop': 'str'
    }

    attribute_map = {
        'ios': 'ios',
        'android': 'android',
        'desktop': 'desktop'
    }

    def __init__(self, ios=None, android=None, desktop=None):  # noqa: E501
        """GetVersionsResponse - a model defined in Swagger"""  # noqa: E501

        self._ios = None
        self._android = None
        self._desktop = None
        self.discriminator = None

        self.ios = ios
        self.android = android
        self.desktop = desktop

    @property
    def ios(self):
        """Gets the ios of this GetVersionsResponse.  # noqa: E501


        :return: The ios of this GetVersionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._ios

    @ios.setter
    def ios(self, ios):
        """Sets the ios of this GetVersionsResponse.


        :param ios: The ios of this GetVersionsResponse.  # noqa: E501
        :type: str
        """

        self._ios = ios

    @property
    def android(self):
        """Gets the android of this GetVersionsResponse.  # noqa: E501


        :return: The android of this GetVersionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._android

    @android.setter
    def android(self, android):
        """Sets the android of this GetVersionsResponse.


        :param android: The android of this GetVersionsResponse.  # noqa: E501
        :type: str
        """

        self._android = android

    @property
    def desktop(self):
        """Gets the desktop of this GetVersionsResponse.  # noqa: E501


        :return: The desktop of this GetVersionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._desktop

    @desktop.setter
    def desktop(self, desktop):
        """Sets the desktop of this GetVersionsResponse.


        :param desktop: The desktop of this GetVersionsResponse.  # noqa: E501
        :type: str
        """

        self._desktop = desktop

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
        if issubclass(GetVersionsResponse, dict):
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
        if not isinstance(other, GetVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
