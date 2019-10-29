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


class MessageOut(object):
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
        'sender': 'str',
        'receiver': 'str',
        'text': 'str',
        'status': 'str',
        'contact_id': 'int',
        'session_id': 'int',
        'message_time': 'datetime',
        'avatar': 'str',
        'deleted': 'bool',
        'charset': 'str',
        'charset_label': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'country': 'str',
        'phone': 'str',
        'price': 'float',
        'parts_count': 'int',
        'from_email': 'str',
        'from_number': 'str'
    }

    attribute_map = {
        'id': 'id',
        'sender': 'sender',
        'receiver': 'receiver',
        'text': 'text',
        'status': 'status',
        'contact_id': 'contactId',
        'session_id': 'sessionId',
        'message_time': 'messageTime',
        'avatar': 'avatar',
        'deleted': 'deleted',
        'charset': 'charset',
        'charset_label': 'charsetLabel',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'country': 'country',
        'phone': 'phone',
        'price': 'price',
        'parts_count': 'partsCount',
        'from_email': 'fromEmail',
        'from_number': 'fromNumber'
    }

    def __init__(self, id=None, sender=None, receiver=None, text=None, status=None, contact_id=None, session_id=None, message_time=None, avatar=None, deleted=None, charset=None, charset_label=None, first_name=None, last_name=None, country=None, phone=None, price=None, parts_count=None, from_email=None, from_number=None):  # noqa: E501
        """MessageOut - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._sender = None
        self._receiver = None
        self._text = None
        self._status = None
        self._contact_id = None
        self._session_id = None
        self._message_time = None
        self._avatar = None
        self._deleted = None
        self._charset = None
        self._charset_label = None
        self._first_name = None
        self._last_name = None
        self._country = None
        self._phone = None
        self._price = None
        self._parts_count = None
        self._from_email = None
        self._from_number = None
        self.discriminator = None

        self.id = id
        if sender is not None:
            self.sender = sender
        if receiver is not None:
            self.receiver = receiver
        self.text = text
        self.status = status
        self.contact_id = contact_id
        self.session_id = session_id
        self.message_time = message_time
        self.avatar = avatar
        if deleted is not None:
            self.deleted = deleted
        self.charset = charset
        self.charset_label = charset_label
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        if phone is not None:
            self.phone = phone
        if price is not None:
            self.price = price
        self.parts_count = parts_count
        if from_email is not None:
            self.from_email = from_email
        if from_number is not None:
            self.from_number = from_number

    @property
    def id(self):
        """Gets the id of this MessageOut.  # noqa: E501

        Message ID.  # noqa: E501

        :return: The id of this MessageOut.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MessageOut.

        Message ID.  # noqa: E501

        :param id: The id of this MessageOut.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def sender(self):
        """Gets the sender of this MessageOut.  # noqa: E501

        Message sender (phone number or alphanumeric Sender ID).  # noqa: E501

        :return: The sender of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this MessageOut.

        Message sender (phone number or alphanumeric Sender ID).  # noqa: E501

        :param sender: The sender of this MessageOut.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def receiver(self):
        """Gets the receiver of this MessageOut.  # noqa: E501

        Recipient phone number.  # noqa: E501

        :return: The receiver of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this MessageOut.

        Recipient phone number.  # noqa: E501

        :param receiver: The receiver of this MessageOut.  # noqa: E501
        :type: str
        """

        self._receiver = receiver

    @property
    def text(self):
        """Gets the text of this MessageOut.  # noqa: E501


        :return: The text of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this MessageOut.


        :param text: The text of this MessageOut.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def status(self):
        """Gets the status of this MessageOut.  # noqa: E501

        Delivery status of the message. See [message delivery statuses](http://docs.textmagictesting.com/#section/Delivery-status-codes) for details.   # noqa: E501

        :return: The status of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MessageOut.

        Delivery status of the message. See [message delivery statuses](http://docs.textmagictesting.com/#section/Delivery-status-codes) for details.   # noqa: E501

        :param status: The status of this MessageOut.  # noqa: E501
        :type: str
        """
        allowed_values = ["q", "s", "e", "r", "a", "d", "b", "f", "u", "j", "i", "p", "h"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def contact_id(self):
        """Gets the contact_id of this MessageOut.  # noqa: E501

        Recipient contact ID.  # noqa: E501

        :return: The contact_id of this MessageOut.  # noqa: E501
        :rtype: int
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this MessageOut.

        Recipient contact ID.  # noqa: E501

        :param contact_id: The contact_id of this MessageOut.  # noqa: E501
        :type: int
        """

        self._contact_id = contact_id

    @property
    def session_id(self):
        """Gets the session_id of this MessageOut.  # noqa: E501

        Message Session ID of a Message.  # noqa: E501

        :return: The session_id of this MessageOut.  # noqa: E501
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this MessageOut.

        Message Session ID of a Message.  # noqa: E501

        :param session_id: The session_id of this MessageOut.  # noqa: E501
        :type: int
        """

        self._session_id = session_id

    @property
    def message_time(self):
        """Gets the message_time of this MessageOut.  # noqa: E501

        Sending time.  # noqa: E501

        :return: The message_time of this MessageOut.  # noqa: E501
        :rtype: datetime
        """
        return self._message_time

    @message_time.setter
    def message_time(self, message_time):
        """Sets the message_time of this MessageOut.

        Sending time.  # noqa: E501

        :param message_time: The message_time of this MessageOut.  # noqa: E501
        :type: datetime
        """

        self._message_time = message_time

    @property
    def avatar(self):
        """Gets the avatar of this MessageOut.  # noqa: E501


        :return: The avatar of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this MessageOut.


        :param avatar: The avatar of this MessageOut.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def deleted(self):
        """Gets the deleted of this MessageOut.  # noqa: E501

        Indicates that the message has been deleted.  # noqa: E501

        :return: The deleted of this MessageOut.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this MessageOut.

        Indicates that the message has been deleted.  # noqa: E501

        :param deleted: The deleted of this MessageOut.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def charset(self):
        """Gets the charset of this MessageOut.  # noqa: E501

        Message charset. Could be: *   **ISO-8859-1** for plaintext SMS; *   **UTF-16BE** for Unicode SMS.   # noqa: E501

        :return: The charset of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._charset

    @charset.setter
    def charset(self, charset):
        """Sets the charset of this MessageOut.

        Message charset. Could be: *   **ISO-8859-1** for plaintext SMS; *   **UTF-16BE** for Unicode SMS.   # noqa: E501

        :param charset: The charset of this MessageOut.  # noqa: E501
        :type: str
        """

        self._charset = charset

    @property
    def charset_label(self):
        """Gets the charset_label of this MessageOut.  # noqa: E501

        Human-readable message charset label. Could be: *   **ISO-8859-1** for plaintext SMS; *   **UTF-16BE** for Unicode SMS; *   **Voice** for voice services (Text-to-Speech or Voice Broadcast) messages.   # noqa: E501

        :return: The charset_label of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._charset_label

    @charset_label.setter
    def charset_label(self, charset_label):
        """Sets the charset_label of this MessageOut.

        Human-readable message charset label. Could be: *   **ISO-8859-1** for plaintext SMS; *   **UTF-16BE** for Unicode SMS; *   **Voice** for voice services (Text-to-Speech or Voice Broadcast) messages.   # noqa: E501

        :param charset_label: The charset_label of this MessageOut.  # noqa: E501
        :type: str
        """

        self._charset_label = charset_label

    @property
    def first_name(self):
        """Gets the first_name of this MessageOut.  # noqa: E501

        Contact first name. Could be substituted from your [Contacts](http://docs.textmagictesting.com/#tag/Contacts) (even if you submitted the phone number instead of the contact ID).   # noqa: E501

        :return: The first_name of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this MessageOut.

        Contact first name. Could be substituted from your [Contacts](http://docs.textmagictesting.com/#tag/Contacts) (even if you submitted the phone number instead of the contact ID).   # noqa: E501

        :param first_name: The first_name of this MessageOut.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this MessageOut.  # noqa: E501

        Contact last name.  # noqa: E501

        :return: The last_name of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this MessageOut.

        Contact last name.  # noqa: E501

        :param last_name: The last_name of this MessageOut.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def country(self):
        """Gets the country of this MessageOut.  # noqa: E501

        The 2-letter ISO country code of the recipient's phone number.   # noqa: E501

        :return: The country of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this MessageOut.

        The 2-letter ISO country code of the recipient's phone number.   # noqa: E501

        :param country: The country of this MessageOut.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def phone(self):
        """Gets the phone of this MessageOut.  # noqa: E501

        Receipent phone number.  # noqa: E501

        :return: The phone of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this MessageOut.

        Receipent phone number.  # noqa: E501

        :param phone: The phone of this MessageOut.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def price(self):
        """Gets the price of this MessageOut.  # noqa: E501

        Message price.  # noqa: E501

        :return: The price of this MessageOut.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this MessageOut.

        Message price.  # noqa: E501

        :param price: The price of this MessageOut.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def parts_count(self):
        """Gets the parts_count of this MessageOut.  # noqa: E501

        Message parts (multiples of 160 characters) count.  # noqa: E501

        :return: The parts_count of this MessageOut.  # noqa: E501
        :rtype: int
        """
        return self._parts_count

    @parts_count.setter
    def parts_count(self, parts_count):
        """Sets the parts_count of this MessageOut.

        Message parts (multiples of 160 characters) count.  # noqa: E501

        :param parts_count: The parts_count of this MessageOut.  # noqa: E501
        :type: int
        """

        self._parts_count = parts_count

    @property
    def from_email(self):
        """Gets the from_email of this MessageOut.  # noqa: E501

        The user email which this message came from. For Email2SMS and Distribution Lists the message will come from an original email address; in other cases, it will come from an account email address.  # noqa: E501

        :return: The from_email of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._from_email

    @from_email.setter
    def from_email(self, from_email):
        """Sets the from_email of this MessageOut.

        The user email which this message came from. For Email2SMS and Distribution Lists the message will come from an original email address; in other cases, it will come from an account email address.  # noqa: E501

        :param from_email: The from_email of this MessageOut.  # noqa: E501
        :type: str
        """

        self._from_email = from_email

    @property
    def from_number(self):
        """Gets the from_number of this MessageOut.  # noqa: E501

        Phone number used to send the SMS.  # noqa: E501

        :return: The from_number of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._from_number

    @from_number.setter
    def from_number(self, from_number):
        """Sets the from_number of this MessageOut.

        Phone number used to send the SMS.  # noqa: E501

        :param from_number: The from_number of this MessageOut.  # noqa: E501
        :type: str
        """

        self._from_number = from_number

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
        if issubclass(MessageOut, dict):
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
        if not isinstance(other, MessageOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
