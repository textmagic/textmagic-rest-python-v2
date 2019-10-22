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


class GetMessagePriceResponse(object):
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
        'total': 'float',
        'parts': 'int',
        'countries': 'list[GetMessagePriceResponseCountriesItem]'
    }

    attribute_map = {
        'total': 'total',
        'parts': 'parts',
        'countries': 'countries'
    }

    def __init__(self, total=None, parts=None, countries=None):  # noqa: E501
        """GetMessagePriceResponse - a model defined in Swagger"""  # noqa: E501

        self._total = None
        self._parts = None
        self._countries = None
        self.discriminator = None

        self.total = total
        self.parts = parts
        self.countries = countries

    @property
    def total(self):
        """Gets the total of this GetMessagePriceResponse.  # noqa: E501

        Total price of the mesasge.  # noqa: E501

        :return: The total of this GetMessagePriceResponse.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this GetMessagePriceResponse.

        Total price of the mesasge.  # noqa: E501

        :param total: The total of this GetMessagePriceResponse.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def parts(self):
        """Gets the parts of this GetMessagePriceResponse.  # noqa: E501

        Message parts (multiples of 160 characters) count.  # noqa: E501

        :return: The parts of this GetMessagePriceResponse.  # noqa: E501
        :rtype: int
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this GetMessagePriceResponse.

        Message parts (multiples of 160 characters) count.  # noqa: E501

        :param parts: The parts of this GetMessagePriceResponse.  # noqa: E501
        :type: int
        """

        self._parts = parts

    @property
    def countries(self):
        """Gets the countries of this GetMessagePriceResponse.  # noqa: E501


        :return: The countries of this GetMessagePriceResponse.  # noqa: E501
        :rtype: list[GetMessagePriceResponseCountriesItem]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this GetMessagePriceResponse.


        :param countries: The countries of this GetMessagePriceResponse.  # noqa: E501
        :type: list[GetMessagePriceResponseCountriesItem]
        """

        self._countries = countries

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
        if issubclass(GetMessagePriceResponse, dict):
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
        if not isinstance(other, GetMessagePriceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
