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


class BulkSession(object):
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
        'status': 'str',
        'items_processed': 'int',
        'items_total': 'int',
        'created_at': 'datetime',
        'session': 'MessageSession',
        'text': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'items_processed': 'itemsProcessed',
        'items_total': 'itemsTotal',
        'created_at': 'createdAt',
        'session': 'session',
        'text': 'text'
    }

    def __init__(self, id=None, status=None, items_processed=None, items_total=None, created_at=None, session=None, text=None):  # noqa: E501
        """BulkSession - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._status = None
        self._items_processed = None
        self._items_total = None
        self._created_at = None
        self._session = None
        self._text = None
        self.discriminator = None

        self.id = id
        self.status = status
        self.items_processed = items_processed
        self.items_total = items_total
        self.created_at = created_at
        self.session = session
        self.text = text

    @property
    def id(self):
        """Gets the id of this BulkSession.  # noqa: E501

        Bulk Session ID.  # noqa: E501

        :return: The id of this BulkSession.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BulkSession.

        Bulk Session ID.  # noqa: E501

        :param id: The id of this BulkSession.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this BulkSession.  # noqa: E501

        * **n** – bulk session is just created * **w** - work in progress * **f** - failed * **c** - completed with success * **s** - suspended   # noqa: E501

        :return: The status of this BulkSession.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BulkSession.

        * **n** – bulk session is just created * **w** - work in progress * **f** - failed * **c** - completed with success * **s** - suspended   # noqa: E501

        :param status: The status of this BulkSession.  # noqa: E501
        :type: str
        """
        allowed_values = ["n", "w", "f", "c", "s"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def items_processed(self):
        """Gets the items_processed of this BulkSession.  # noqa: E501

        Amount of messages already processed.  # noqa: E501

        :return: The items_processed of this BulkSession.  # noqa: E501
        :rtype: int
        """
        return self._items_processed

    @items_processed.setter
    def items_processed(self, items_processed):
        """Sets the items_processed of this BulkSession.

        Amount of messages already processed.  # noqa: E501

        :param items_processed: The items_processed of this BulkSession.  # noqa: E501
        :type: int
        """

        self._items_processed = items_processed

    @property
    def items_total(self):
        """Gets the items_total of this BulkSession.  # noqa: E501

        Total amount of messages to be processed.  # noqa: E501

        :return: The items_total of this BulkSession.  # noqa: E501
        :rtype: int
        """
        return self._items_total

    @items_total.setter
    def items_total(self, items_total):
        """Sets the items_total of this BulkSession.

        Total amount of messages to be processed.  # noqa: E501

        :param items_total: The items_total of this BulkSession.  # noqa: E501
        :type: int
        """

        self._items_total = items_total

    @property
    def created_at(self):
        """Gets the created_at of this BulkSession.  # noqa: E501

        Creation date and time of a Bulk Session.  # noqa: E501

        :return: The created_at of this BulkSession.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BulkSession.

        Creation date and time of a Bulk Session.  # noqa: E501

        :param created_at: The created_at of this BulkSession.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def session(self):
        """Gets the session of this BulkSession.  # noqa: E501


        :return: The session of this BulkSession.  # noqa: E501
        :rtype: MessageSession
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this BulkSession.


        :param session: The session of this BulkSession.  # noqa: E501
        :type: MessageSession
        """

        self._session = session

    @property
    def text(self):
        """Gets the text of this BulkSession.  # noqa: E501

        Message text of a Bulk Session.  # noqa: E501

        :return: The text of this BulkSession.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this BulkSession.

        Message text of a Bulk Session.  # noqa: E501

        :param text: The text of this BulkSession.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if issubclass(BulkSession, dict):
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
        if not isinstance(other, BulkSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
