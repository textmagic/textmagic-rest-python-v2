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


class MessagePriceItem(object):
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
        'name': 'str',
        'price': 'str',
        'country': 'str'
    }

    attribute_map = {
        'name': 'name',
        'price': 'price',
        'country': 'country'
    }

    def __init__(self, name=None, price=None, country=None):  # noqa: E501
        """MessagePriceItem - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._price = None
        self._country = None
        self.discriminator = None

        self.name = name
        self.price = price
        self.country = country

    @property
    def name(self):
        """Gets the name of this MessagePriceItem.  # noqa: E501

        Country name.  # noqa: E501

        :return: The name of this MessagePriceItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MessagePriceItem.

        Country name.  # noqa: E501

        :param name: The name of this MessagePriceItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def price(self):
        """Gets the price of this MessagePriceItem.  # noqa: E501

        Price to send message to desired country.  # noqa: E501

        :return: The price of this MessagePriceItem.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this MessagePriceItem.

        Price to send message to desired country.  # noqa: E501

        :param price: The price of this MessagePriceItem.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def country(self):
        """Gets the country of this MessagePriceItem.  # noqa: E501

        The 2-letter ISO country code of the recipient's phone number.  # noqa: E501

        :return: The country of this MessagePriceItem.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this MessagePriceItem.

        The 2-letter ISO country code of the recipient's phone number.  # noqa: E501

        :param country: The country of this MessagePriceItem.  # noqa: E501
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
        if issubclass(MessagePriceItem, dict):
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
        if not isinstance(other, MessagePriceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
