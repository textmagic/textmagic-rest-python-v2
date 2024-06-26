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


class Invoice(object):
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
        'bundle': 'int',
        'currency': 'str',
        'vat': 'float',
        'payment_method': 'str'
    }

    attribute_map = {
        'id': 'id',
        'bundle': 'bundle',
        'currency': 'currency',
        'vat': 'vat',
        'payment_method': 'paymentMethod'
    }

    def __init__(self, id=None, bundle=None, currency=None, vat=None, payment_method=None):  # noqa: E501
        """Invoice - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._bundle = None
        self._currency = None
        self._vat = None
        self._payment_method = None
        self.discriminator = None

        self.id = id
        self.bundle = bundle
        self.currency = currency
        self.vat = vat
        self.payment_method = payment_method

    @property
    def id(self):
        """Gets the id of this Invoice.  # noqa: E501

        The invoice ID.  # noqa: E501

        :return: The id of this Invoice.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Invoice.

        The invoice ID.  # noqa: E501

        :param id: The id of this Invoice.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def bundle(self):
        """Gets the bundle of this Invoice.  # noqa: E501

        Top-up amount.  # noqa: E501

        :return: The bundle of this Invoice.  # noqa: E501
        :rtype: int
        """
        return self._bundle

    @bundle.setter
    def bundle(self, bundle):
        """Sets the bundle of this Invoice.

        Top-up amount.  # noqa: E501

        :param bundle: The bundle of this Invoice.  # noqa: E501
        :type: int
        """

        self._bundle = bundle

    @property
    def currency(self):
        """Gets the currency of this Invoice.  # noqa: E501

        Top-up currency.  # noqa: E501

        :return: The currency of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Invoice.

        Top-up currency.  # noqa: E501

        :param currency: The currency of this Invoice.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def vat(self):
        """Gets the vat of this Invoice.  # noqa: E501

        VAT charged (if any).  # noqa: E501

        :return: The vat of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._vat

    @vat.setter
    def vat(self, vat):
        """Sets the vat of this Invoice.

        VAT charged (if any).  # noqa: E501

        :param vat: The vat of this Invoice.  # noqa: E501
        :type: float
        """

        self._vat = vat

    @property
    def payment_method(self):
        """Gets the payment_method of this Invoice.  # noqa: E501

        Payment method description.  # noqa: E501

        :return: The payment_method of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this Invoice.

        Payment method description.  # noqa: E501

        :param payment_method: The payment_method of this Invoice.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

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
        if issubclass(Invoice, dict):
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
        if not isinstance(other, Invoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
