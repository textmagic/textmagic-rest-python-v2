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


class DoCarrierLookupResponse(object):
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
        'cost': 'float',
        'country': 'Country',
        'local': 'str',
        'type': 'str',
        'carrier': 'str',
        'number164': 'str',
        'valid': 'bool'
    }

    attribute_map = {
        'cost': 'cost',
        'country': 'country',
        'local': 'local',
        'type': 'type',
        'carrier': 'carrier',
        'number164': 'number164',
        'valid': 'valid'
    }

    def __init__(self, cost=None, country=None, local=None, type=None, carrier=None, number164=None, valid=None):  # noqa: E501
        """DoCarrierLookupResponse - a model defined in Swagger"""  # noqa: E501

        self._cost = None
        self._country = None
        self._local = None
        self._type = None
        self._carrier = None
        self._number164 = None
        self._valid = None
        self.discriminator = None

        self.cost = cost
        if country is not None:
            self.country = country
        self.local = local
        self.type = type
        self.carrier = carrier
        self.number164 = number164
        self.valid = valid

    @property
    def cost(self):
        """Gets the cost of this DoCarrierLookupResponse.  # noqa: E501

        The cost to check that one number is constant – 0.04 in your account currency.  # noqa: E501

        :return: The cost of this DoCarrierLookupResponse.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this DoCarrierLookupResponse.

        The cost to check that one number is constant – 0.04 in your account currency.  # noqa: E501

        :param cost: The cost of this DoCarrierLookupResponse.  # noqa: E501
        :type: float
        """

        self._cost = cost

    @property
    def country(self):
        """Gets the country of this DoCarrierLookupResponse.  # noqa: E501

        Phone number country.  # noqa: E501

        :return: The country of this DoCarrierLookupResponse.  # noqa: E501
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this DoCarrierLookupResponse.

        Phone number country.  # noqa: E501

        :param country: The country of this DoCarrierLookupResponse.  # noqa: E501
        :type: Country
        """

        self._country = country

    @property
    def local(self):
        """Gets the local of this DoCarrierLookupResponse.  # noqa: E501

        Phone number in [National format](https://en.wikipedia.org/wiki/National_conventions_for_writing_telephone_numbers).  # noqa: E501

        :return: The local of this DoCarrierLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._local

    @local.setter
    def local(self, local):
        """Sets the local of this DoCarrierLookupResponse.

        Phone number in [National format](https://en.wikipedia.org/wiki/National_conventions_for_writing_telephone_numbers).  # noqa: E501

        :param local: The local of this DoCarrierLookupResponse.  # noqa: E501
        :type: str
        """

        self._local = local

    @property
    def type(self):
        """Gets the type of this DoCarrierLookupResponse.  # noqa: E501

        Phone number type.  # noqa: E501

        :return: The type of this DoCarrierLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DoCarrierLookupResponse.

        Phone number type.  # noqa: E501

        :param type: The type of this DoCarrierLookupResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["mobile", "landline", "voip"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def carrier(self):
        """Gets the carrier of this DoCarrierLookupResponse.  # noqa: E501

        Carrier name.  # noqa: E501

        :return: The carrier of this DoCarrierLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this DoCarrierLookupResponse.

        Carrier name.  # noqa: E501

        :param carrier: The carrier of this DoCarrierLookupResponse.  # noqa: E501
        :type: str
        """

        self._carrier = carrier

    @property
    def number164(self):
        """Gets the number164 of this DoCarrierLookupResponse.  # noqa: E501

        Phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164).  # noqa: E501

        :return: The number164 of this DoCarrierLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._number164

    @number164.setter
    def number164(self, number164):
        """Sets the number164 of this DoCarrierLookupResponse.

        Phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164).  # noqa: E501

        :param number164: The number164 of this DoCarrierLookupResponse.  # noqa: E501
        :type: str
        """

        self._number164 = number164

    @property
    def valid(self):
        """Gets the valid of this DoCarrierLookupResponse.  # noqa: E501

        This field shows whether the entered phone number is valid or not.  # noqa: E501

        :return: The valid of this DoCarrierLookupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this DoCarrierLookupResponse.

        This field shows whether the entered phone number is valid or not.  # noqa: E501

        :param valid: The valid of this DoCarrierLookupResponse.  # noqa: E501
        :type: bool
        """

        self._valid = valid

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
        if issubclass(DoCarrierLookupResponse, dict):
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
        if not isinstance(other, DoCarrierLookupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
