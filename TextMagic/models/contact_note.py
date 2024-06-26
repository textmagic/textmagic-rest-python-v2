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


class ContactNote(object):
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
        'created_at': 'datetime',
        'note': 'str',
        'user': 'User'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'createdAt',
        'note': 'note',
        'user': 'user'
    }

    def __init__(self, id=None, created_at=None, note=None, user=None):  # noqa: E501
        """ContactNote - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_at = None
        self._note = None
        self._user = None
        self.discriminator = None

        self.id = id
        self.created_at = created_at
        self.note = note
        self.user = user

    @property
    def id(self):
        """Gets the id of this ContactNote.  # noqa: E501

        Contact note ID.  # noqa: E501

        :return: The id of this ContactNote.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContactNote.

        Contact note ID.  # noqa: E501

        :param id: The id of this ContactNote.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this ContactNote.  # noqa: E501

        Contact note creation time.  # noqa: E501

        :return: The created_at of this ContactNote.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ContactNote.

        Contact note creation time.  # noqa: E501

        :param created_at: The created_at of this ContactNote.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def note(self):
        """Gets the note of this ContactNote.  # noqa: E501

        Contact note text.  # noqa: E501

        :return: The note of this ContactNote.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this ContactNote.

        Contact note text.  # noqa: E501

        :param note: The note of this ContactNote.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def user(self):
        """Gets the user of this ContactNote.  # noqa: E501


        :return: The user of this ContactNote.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ContactNote.


        :param user: The user of this ContactNote.  # noqa: E501
        :type: User
        """

        self._user = user

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
        if issubclass(ContactNote, dict):
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
        if not isinstance(other, ContactNote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
