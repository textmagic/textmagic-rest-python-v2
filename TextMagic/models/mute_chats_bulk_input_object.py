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


class MuteChatsBulkInputObject(object):
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
        'ids': 'str',
        'all': 'bool',
        '_for': 'int'
    }

    attribute_map = {
        'ids': 'ids',
        'all': 'all',
        '_for': 'for'
    }

    def __init__(self, ids=None, all=None, _for=None):  # noqa: E501
        """MuteChatsBulkInputObject - a model defined in Swagger"""  # noqa: E501

        self._ids = None
        self._all = None
        self.__for = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if all is not None:
            self.all = all
        if _for is not None:
            self._for = _for

    @property
    def ids(self):
        """Gets the ids of this MuteChatsBulkInputObject.  # noqa: E501

        Entity ID(s), separated by comma  # noqa: E501

        :return: The ids of this MuteChatsBulkInputObject.  # noqa: E501
        :rtype: str
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this MuteChatsBulkInputObject.

        Entity ID(s), separated by comma  # noqa: E501

        :param ids: The ids of this MuteChatsBulkInputObject.  # noqa: E501
        :type: str
        """

        self._ids = ids

    @property
    def all(self):
        """Gets the all of this MuteChatsBulkInputObject.  # noqa: E501

        Entity ID(s), separated by comma  # noqa: E501

        :return: The all of this MuteChatsBulkInputObject.  # noqa: E501
        :rtype: bool
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this MuteChatsBulkInputObject.

        Entity ID(s), separated by comma  # noqa: E501

        :param all: The all of this MuteChatsBulkInputObject.  # noqa: E501
        :type: bool
        """

        self._all = all

    @property
    def _for(self):
        """Gets the _for of this MuteChatsBulkInputObject.  # noqa: E501

        Mute for N hours  # noqa: E501

        :return: The _for of this MuteChatsBulkInputObject.  # noqa: E501
        :rtype: int
        """
        return self.__for

    @_for.setter
    def _for(self, _for):
        """Sets the _for of this MuteChatsBulkInputObject.

        Mute for N hours  # noqa: E501

        :param _for: The _for of this MuteChatsBulkInputObject.  # noqa: E501
        :type: int
        """

        self.__for = _for

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
        if issubclass(MuteChatsBulkInputObject, dict):
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
        if not isinstance(other, MuteChatsBulkInputObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
