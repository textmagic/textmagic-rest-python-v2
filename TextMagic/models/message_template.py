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


class MessageTemplate(object):
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
        'name': 'str',
        'content': 'str',
        'last_modified': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'content': 'content',
        'last_modified': 'lastModified'
    }

    def __init__(self, id=None, name=None, content=None, last_modified=None):  # noqa: E501
        """MessageTemplate - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._content = None
        self._last_modified = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.content = content
        self.last_modified = last_modified

    @property
    def id(self):
        """Gets the id of this MessageTemplate.  # noqa: E501

        Template ID.  # noqa: E501

        :return: The id of this MessageTemplate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MessageTemplate.

        Template ID.  # noqa: E501

        :param id: The id of this MessageTemplate.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MessageTemplate.  # noqa: E501

        Template name.  # noqa: E501

        :return: The name of this MessageTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MessageTemplate.

        Template name.  # noqa: E501

        :param name: The name of this MessageTemplate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def content(self):
        """Gets the content of this MessageTemplate.  # noqa: E501

        Template text. May contain tags inside braces. See the [Custom fields list](https://docs.textmagic.com/#section/Custom-fields-list-(Merge-tags)).  # noqa: E501

        :return: The content of this MessageTemplate.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this MessageTemplate.

        Template text. May contain tags inside braces. See the [Custom fields list](https://docs.textmagic.com/#section/Custom-fields-list-(Merge-tags)).  # noqa: E501

        :param content: The content of this MessageTemplate.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def last_modified(self):
        """Gets the last_modified of this MessageTemplate.  # noqa: E501

        Time when the template was last modified.  # noqa: E501

        :return: The last_modified of this MessageTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this MessageTemplate.

        Time when the template was last modified.  # noqa: E501

        :param last_modified: The last_modified of this MessageTemplate.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

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
        if issubclass(MessageTemplate, dict):
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
        if not isinstance(other, MessageTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
