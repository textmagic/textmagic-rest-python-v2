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


class GetAvailableDedicatedNumbersResponse(object):
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
        'numbers': 'list[str]',
        'price': 'float'
    }

    attribute_map = {
        'numbers': 'numbers',
        'price': 'price'
    }

    def __init__(self, numbers=None, price=None):  # noqa: E501
        """GetAvailableDedicatedNumbersResponse - a model defined in Swagger"""  # noqa: E501

        self._numbers = None
        self._price = None
        self.discriminator = None

        self.numbers = numbers
        self.price = price

    @property
    def numbers(self):
        """Gets the numbers of this GetAvailableDedicatedNumbersResponse.  # noqa: E501

        Array of phone numbers.  # noqa: E501

        :return: The numbers of this GetAvailableDedicatedNumbersResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._numbers

    @numbers.setter
    def numbers(self, numbers):
        """Sets the numbers of this GetAvailableDedicatedNumbersResponse.

        Array of phone numbers.  # noqa: E501

        :param numbers: The numbers of this GetAvailableDedicatedNumbersResponse.  # noqa: E501
        :type: list[str]
        """

        self._numbers = numbers

    @property
    def price(self):
        """Gets the price of this GetAvailableDedicatedNumbersResponse.  # noqa: E501

        Dedicated number monthly fee for this country. Returned in current [account](http://docs.textmagictesting.com/#tag/User) currency.  # noqa: E501

        :return: The price of this GetAvailableDedicatedNumbersResponse.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this GetAvailableDedicatedNumbersResponse.

        Dedicated number monthly fee for this country. Returned in current [account](http://docs.textmagictesting.com/#tag/User) currency.  # noqa: E501

        :param price: The price of this GetAvailableDedicatedNumbersResponse.  # noqa: E501
        :type: float
        """

        self._price = price

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
        if issubclass(GetAvailableDedicatedNumbersResponse, dict):
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
        if not isinstance(other, GetAvailableDedicatedNumbersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
