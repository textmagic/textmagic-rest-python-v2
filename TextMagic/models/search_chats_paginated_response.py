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


class SearchChatsPaginatedResponse(object):
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
        'page': 'int',
        'page_count': 'int',
        'limit': 'int',
        'resources': 'list[Chat]'
    }

    attribute_map = {
        'page': 'page',
        'page_count': 'pageCount',
        'limit': 'limit',
        'resources': 'resources'
    }

    def __init__(self, page=None, page_count=None, limit=None, resources=None):  # noqa: E501
        """SearchChatsPaginatedResponse - a model defined in Swagger"""  # noqa: E501

        self._page = None
        self._page_count = None
        self._limit = None
        self._resources = None
        self.discriminator = None

        self.page = page
        self.page_count = page_count
        self.limit = limit
        self.resources = resources

    @property
    def page(self):
        """Gets the page of this SearchChatsPaginatedResponse.  # noqa: E501


        :return: The page of this SearchChatsPaginatedResponse.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this SearchChatsPaginatedResponse.


        :param page: The page of this SearchChatsPaginatedResponse.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_count(self):
        """Gets the page_count of this SearchChatsPaginatedResponse.  # noqa: E501

        The total number of pages.  # noqa: E501

        :return: The page_count of this SearchChatsPaginatedResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this SearchChatsPaginatedResponse.

        The total number of pages.  # noqa: E501

        :param page_count: The page_count of this SearchChatsPaginatedResponse.  # noqa: E501
        :type: int
        """

        self._page_count = page_count

    @property
    def limit(self):
        """Gets the limit of this SearchChatsPaginatedResponse.  # noqa: E501

        The number of results per page.  # noqa: E501

        :return: The limit of this SearchChatsPaginatedResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchChatsPaginatedResponse.

        The number of results per page.  # noqa: E501

        :param limit: The limit of this SearchChatsPaginatedResponse.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def resources(self):
        """Gets the resources of this SearchChatsPaginatedResponse.  # noqa: E501


        :return: The resources of this SearchChatsPaginatedResponse.  # noqa: E501
        :rtype: list[Chat]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this SearchChatsPaginatedResponse.


        :param resources: The resources of this SearchChatsPaginatedResponse.  # noqa: E501
        :type: list[Chat]
        """

        self._resources = resources

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
        if issubclass(SearchChatsPaginatedResponse, dict):
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
        if not isinstance(other, SearchChatsPaginatedResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
