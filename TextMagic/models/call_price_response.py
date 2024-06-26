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


class CallPriceResponse(object):
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
        'outbound': 'float',
        'inbound': 'float',
        'forward': 'float',
        'country': 'str'
    }

    attribute_map = {
        'outbound': 'outbound',
        'inbound': 'inbound',
        'forward': 'forward',
        'country': 'country'
    }

    def __init__(self, outbound=None, inbound=None, forward=None, country=None):  # noqa: E501
        """CallPriceResponse - a model defined in Swagger"""  # noqa: E501

        self._outbound = None
        self._inbound = None
        self._forward = None
        self._country = None
        self.discriminator = None

        self.outbound = outbound
        self.inbound = inbound
        self.forward = forward
        self.country = country

    @property
    def outbound(self):
        """Gets the outbound of this CallPriceResponse.  # noqa: E501

        Price for outbound message.  # noqa: E501

        :return: The outbound of this CallPriceResponse.  # noqa: E501
        :rtype: float
        """
        return self._outbound

    @outbound.setter
    def outbound(self, outbound):
        """Sets the outbound of this CallPriceResponse.

        Price for outbound message.  # noqa: E501

        :param outbound: The outbound of this CallPriceResponse.  # noqa: E501
        :type: float
        """

        self._outbound = outbound

    @property
    def inbound(self):
        """Gets the inbound of this CallPriceResponse.  # noqa: E501

        Price for inbound message.  # noqa: E501

        :return: The inbound of this CallPriceResponse.  # noqa: E501
        :rtype: float
        """
        return self._inbound

    @inbound.setter
    def inbound(self, inbound):
        """Sets the inbound of this CallPriceResponse.

        Price for inbound message.  # noqa: E501

        :param inbound: The inbound of this CallPriceResponse.  # noqa: E501
        :type: float
        """

        self._inbound = inbound

    @property
    def forward(self):
        """Gets the forward of this CallPriceResponse.  # noqa: E501

        Price for forward.  # noqa: E501

        :return: The forward of this CallPriceResponse.  # noqa: E501
        :rtype: float
        """
        return self._forward

    @forward.setter
    def forward(self, forward):
        """Sets the forward of this CallPriceResponse.

        Price for forward.  # noqa: E501

        :param forward: The forward of this CallPriceResponse.  # noqa: E501
        :type: float
        """

        self._forward = forward

    @property
    def country(self):
        """Gets the country of this CallPriceResponse.  # noqa: E501

        The 2-letter ISO country code for local phone numbers, used when local is  set to true. Default is account country.  # noqa: E501

        :return: The country of this CallPriceResponse.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CallPriceResponse.

        The 2-letter ISO country code for local phone numbers, used when local is  set to true. Default is account country.  # noqa: E501

        :param country: The country of this CallPriceResponse.  # noqa: E501
        :type: str
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
        if issubclass(CallPriceResponse, dict):
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
        if not isinstance(other, CallPriceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
