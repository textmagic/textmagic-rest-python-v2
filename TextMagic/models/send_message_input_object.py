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


class SendMessageInputObject(object):
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
        'text': 'str',
        'template_id': 'int',
        'sending_time': 'int',
        'sending_date_time': 'str',
        'sending_timezone': 'str',
        'contacts': 'str',
        'lists': 'str',
        'phones': 'str',
        'cut_extra': 'bool',
        'parts_count': 'int',
        'reference_id': 'int',
        '_from': 'str',
        'rrule': 'str',
        'create_chat': 'bool',
        'tts': 'bool',
        'local': 'bool',
        'local_country': 'str',
        'destination': 'str',
        'resources': 'str'
    }

    attribute_map = {
        'text': 'text',
        'template_id': 'templateId',
        'sending_time': 'sendingTime',
        'sending_date_time': 'sendingDateTime',
        'sending_timezone': 'sendingTimezone',
        'contacts': 'contacts',
        'lists': 'lists',
        'phones': 'phones',
        'cut_extra': 'cutExtra',
        'parts_count': 'partsCount',
        'reference_id': 'referenceId',
        '_from': 'from',
        'rrule': 'rrule',
        'create_chat': 'createChat',
        'tts': 'tts',
        'local': 'local',
        'local_country': 'localCountry',
        'destination': 'destination',
        'resources': 'resources'
    }

    def __init__(self, text=None, template_id=None, sending_time=None, sending_date_time=None, sending_timezone=None, contacts=None, lists=None, phones=None, cut_extra=False, parts_count=None, reference_id=None, _from=None, rrule=None, create_chat=False, tts=False, local=False, local_country=None, destination=None, resources=None):  # noqa: E501
        """SendMessageInputObject - a model defined in Swagger"""  # noqa: E501

        self._text = None
        self._template_id = None
        self._sending_time = None
        self._sending_date_time = None
        self._sending_timezone = None
        self._contacts = None
        self._lists = None
        self._phones = None
        self._cut_extra = None
        self._parts_count = None
        self._reference_id = None
        self.__from = None
        self._rrule = None
        self._create_chat = None
        self._tts = None
        self._local = None
        self._local_country = None
        self._destination = None
        self._resources = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if template_id is not None:
            self.template_id = template_id
        if sending_time is not None:
            self.sending_time = sending_time
        if sending_date_time is not None:
            self.sending_date_time = sending_date_time
        if sending_timezone is not None:
            self.sending_timezone = sending_timezone
        if contacts is not None:
            self.contacts = contacts
        if lists is not None:
            self.lists = lists
        if phones is not None:
            self.phones = phones
        if cut_extra is not None:
            self.cut_extra = cut_extra
        if parts_count is not None:
            self.parts_count = parts_count
        if reference_id is not None:
            self.reference_id = reference_id
        if _from is not None:
            self._from = _from
        if rrule is not None:
            self.rrule = rrule
        if create_chat is not None:
            self.create_chat = create_chat
        if tts is not None:
            self.tts = tts
        if local is not None:
            self.local = local
        if local_country is not None:
            self.local_country = local_country
        if destination is not None:
            self.destination = destination
        if resources is not None:
            self.resources = resources

    @property
    def text(self):
        """Gets the text of this SendMessageInputObject.  # noqa: E501

        Message text. Required if the **template_id** is not set.  # noqa: E501

        :return: The text of this SendMessageInputObject.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SendMessageInputObject.

        Message text. Required if the **template_id** is not set.  # noqa: E501

        :param text: The text of this SendMessageInputObject.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def template_id(self):
        """Gets the template_id of this SendMessageInputObject.  # noqa: E501

        Template used instead of message text. Required if the **text** is not set.  # noqa: E501

        :return: The template_id of this SendMessageInputObject.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this SendMessageInputObject.

        Template used instead of message text. Required if the **text** is not set.  # noqa: E501

        :param template_id: The template_id of this SendMessageInputObject.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

    @property
    def sending_time(self):
        """Gets the sending_time of this SendMessageInputObject.  # noqa: E501

        DEPRECATED, consider using sendingDateTime and sendingTimezone parameters instead: Optional (required with rrule set). Message sending time in unix timestamp format. Default is now.  # noqa: E501

        :return: The sending_time of this SendMessageInputObject.  # noqa: E501
        :rtype: int
        """
        return self._sending_time

    @sending_time.setter
    def sending_time(self, sending_time):
        """Sets the sending_time of this SendMessageInputObject.

        DEPRECATED, consider using sendingDateTime and sendingTimezone parameters instead: Optional (required with rrule set). Message sending time in unix timestamp format. Default is now.  # noqa: E501

        :param sending_time: The sending_time of this SendMessageInputObject.  # noqa: E501
        :type: int
        """

        self._sending_time = sending_time

    @property
    def sending_date_time(self):
        """Gets the sending_date_time of this SendMessageInputObject.  # noqa: E501

        Sending time in Y-m-d H:i:s format (e.g. 2022-05-27 13:05:10). This time is relative to **sendingTimezone**. Note: for correct operation, the value of seconds must not be less than 10.  # noqa: E501

        :return: The sending_date_time of this SendMessageInputObject.  # noqa: E501
        :rtype: str
        """
        return self._sending_date_time

    @sending_date_time.setter
    def sending_date_time(self, sending_date_time):
        """Sets the sending_date_time of this SendMessageInputObject.

        Sending time in Y-m-d H:i:s format (e.g. 2022-05-27 13:05:10). This time is relative to **sendingTimezone**. Note: for correct operation, the value of seconds must not be less than 10.  # noqa: E501

        :param sending_date_time: The sending_date_time of this SendMessageInputObject.  # noqa: E501
        :type: str
        """

        self._sending_date_time = sending_date_time

    @property
    def sending_timezone(self):
        """Gets the sending_timezone of this SendMessageInputObject.  # noqa: E501

        ID or ISO-name of timezone used for sending when sendingDateTime parameter is set. E.g. if you specify sendingDateTime = \\\"2016-05-27 13:02:33\\\" and sendingTimezone = \\\"America/Buenos_Aires\\\", your message will be sent at May 27, 2016 13:02:33 Buenos Aires time, or 16:02:33 UTC. Default is account timezone.  # noqa: E501

        :return: The sending_timezone of this SendMessageInputObject.  # noqa: E501
        :rtype: str
        """
        return self._sending_timezone

    @sending_timezone.setter
    def sending_timezone(self, sending_timezone):
        """Sets the sending_timezone of this SendMessageInputObject.

        ID or ISO-name of timezone used for sending when sendingDateTime parameter is set. E.g. if you specify sendingDateTime = \\\"2016-05-27 13:02:33\\\" and sendingTimezone = \\\"America/Buenos_Aires\\\", your message will be sent at May 27, 2016 13:02:33 Buenos Aires time, or 16:02:33 UTC. Default is account timezone.  # noqa: E501

        :param sending_timezone: The sending_timezone of this SendMessageInputObject.  # noqa: E501
        :type: str
        """

        self._sending_timezone = sending_timezone

    @property
    def contacts(self):
        """Gets the contacts of this SendMessageInputObject.  # noqa: E501

        Comma separated array of contact resources id message will be sent to.  # noqa: E501

        :return: The contacts of this SendMessageInputObject.  # noqa: E501
        :rtype: str
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this SendMessageInputObject.

        Comma separated array of contact resources id message will be sent to.  # noqa: E501

        :param contacts: The contacts of this SendMessageInputObject.  # noqa: E501
        :type: str
        """

        self._contacts = contacts

    @property
    def lists(self):
        """Gets the lists of this SendMessageInputObject.  # noqa: E501

        Comma separated array of list resources id message will be sent to.  # noqa: E501

        :return: The lists of this SendMessageInputObject.  # noqa: E501
        :rtype: str
        """
        return self._lists

    @lists.setter
    def lists(self, lists):
        """Sets the lists of this SendMessageInputObject.

        Comma separated array of list resources id message will be sent to.  # noqa: E501

        :param lists: The lists of this SendMessageInputObject.  # noqa: E501
        :type: str
        """

        self._lists = lists

    @property
    def phones(self):
        """Gets the phones of this SendMessageInputObject.  # noqa: E501

        Comma separated array of E.164 phone numbers message will be sent to.  # noqa: E501

        :return: The phones of this SendMessageInputObject.  # noqa: E501
        :rtype: str
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        """Sets the phones of this SendMessageInputObject.

        Comma separated array of E.164 phone numbers message will be sent to.  # noqa: E501

        :param phones: The phones of this SendMessageInputObject.  # noqa: E501
        :type: str
        """

        self._phones = phones

    @property
    def cut_extra(self):
        """Gets the cut_extra of this SendMessageInputObject.  # noqa: E501

        Should sending method cut extra characters which not fit supplied partsCount or return 400 Bad request response instead.  # noqa: E501

        :return: The cut_extra of this SendMessageInputObject.  # noqa: E501
        :rtype: bool
        """
        return self._cut_extra

    @cut_extra.setter
    def cut_extra(self, cut_extra):
        """Sets the cut_extra of this SendMessageInputObject.

        Should sending method cut extra characters which not fit supplied partsCount or return 400 Bad request response instead.  # noqa: E501

        :param cut_extra: The cut_extra of this SendMessageInputObject.  # noqa: E501
        :type: bool
        """

        self._cut_extra = cut_extra

    @property
    def parts_count(self):
        """Gets the parts_count of this SendMessageInputObject.  # noqa: E501

        Maximum message parts count (Textmagic allows sending 1 to 6 message parts).  # noqa: E501

        :return: The parts_count of this SendMessageInputObject.  # noqa: E501
        :rtype: int
        """
        return self._parts_count

    @parts_count.setter
    def parts_count(self, parts_count):
        """Sets the parts_count of this SendMessageInputObject.

        Maximum message parts count (Textmagic allows sending 1 to 6 message parts).  # noqa: E501

        :param parts_count: The parts_count of this SendMessageInputObject.  # noqa: E501
        :type: int
        """

        self._parts_count = parts_count

    @property
    def reference_id(self):
        """Gets the reference_id of this SendMessageInputObject.  # noqa: E501

        Custom message reference id which can be used in your application infrastructure.  # noqa: E501

        :return: The reference_id of this SendMessageInputObject.  # noqa: E501
        :rtype: int
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this SendMessageInputObject.

        Custom message reference id which can be used in your application infrastructure.  # noqa: E501

        :param reference_id: The reference_id of this SendMessageInputObject.  # noqa: E501
        :type: int
        """

        self._reference_id = reference_id

    @property
    def _from(self):
        """Gets the _from of this SendMessageInputObject.  # noqa: E501

        One of allowed Sender ID (phone number or alphanumeric sender ID). If specified Sender ID is not allowed for some destinations, a fallback default Sender ID will be used to ensure delivery. See [Get timezones](https://docs.textmagic.com/#tag/Sender-IDs).  # noqa: E501

        :return: The _from of this SendMessageInputObject.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this SendMessageInputObject.

        One of allowed Sender ID (phone number or alphanumeric sender ID). If specified Sender ID is not allowed for some destinations, a fallback default Sender ID will be used to ensure delivery. See [Get timezones](https://docs.textmagic.com/#tag/Sender-IDs).  # noqa: E501

        :param _from: The _from of this SendMessageInputObject.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def rrule(self):
        """Gets the rrule of this SendMessageInputObject.  # noqa: E501

        iCal RRULE parameter to create recurrent scheduled messages. When used, sendingTime is mandatory as start point of sending. See https://www.textmagic.com/free-tools/rrule-generator for format details.  # noqa: E501

        :return: The rrule of this SendMessageInputObject.  # noqa: E501
        :rtype: str
        """
        return self._rrule

    @rrule.setter
    def rrule(self, rrule):
        """Sets the rrule of this SendMessageInputObject.

        iCal RRULE parameter to create recurrent scheduled messages. When used, sendingTime is mandatory as start point of sending. See https://www.textmagic.com/free-tools/rrule-generator for format details.  # noqa: E501

        :param rrule: The rrule of this SendMessageInputObject.  # noqa: E501
        :type: str
        """

        self._rrule = rrule

    @property
    def create_chat(self):
        """Gets the create_chat of this SendMessageInputObject.  # noqa: E501

        Should sending method try to create new Chat (if not exist) with specified recipients?  # noqa: E501

        :return: The create_chat of this SendMessageInputObject.  # noqa: E501
        :rtype: bool
        """
        return self._create_chat

    @create_chat.setter
    def create_chat(self, create_chat):
        """Sets the create_chat of this SendMessageInputObject.

        Should sending method try to create new Chat (if not exist) with specified recipients?  # noqa: E501

        :param create_chat: The create_chat of this SendMessageInputObject.  # noqa: E501
        :type: bool
        """

        self._create_chat = create_chat

    @property
    def tts(self):
        """Gets the tts of this SendMessageInputObject.  # noqa: E501

        Send a Text-to-Speech message.  # noqa: E501

        :return: The tts of this SendMessageInputObject.  # noqa: E501
        :rtype: bool
        """
        return self._tts

    @tts.setter
    def tts(self, tts):
        """Sets the tts of this SendMessageInputObject.

        Send a Text-to-Speech message.  # noqa: E501

        :param tts: The tts of this SendMessageInputObject.  # noqa: E501
        :type: bool
        """

        self._tts = tts

    @property
    def local(self):
        """Gets the local of this SendMessageInputObject.  # noqa: E501

        Treat phone numbers passed in the \\'phones\\' field as local.  # noqa: E501

        :return: The local of this SendMessageInputObject.  # noqa: E501
        :rtype: bool
        """
        return self._local

    @local.setter
    def local(self, local):
        """Sets the local of this SendMessageInputObject.

        Treat phone numbers passed in the \\'phones\\' field as local.  # noqa: E501

        :param local: The local of this SendMessageInputObject.  # noqa: E501
        :type: bool
        """

        self._local = local

    @property
    def local_country(self):
        """Gets the local_country of this SendMessageInputObject.  # noqa: E501

        The 2-letter ISO country code for local phone numbers, used when \\'local\\' is set to true. Default is the account country.  # noqa: E501

        :return: The local_country of this SendMessageInputObject.  # noqa: E501
        :rtype: str
        """
        return self._local_country

    @local_country.setter
    def local_country(self, local_country):
        """Sets the local_country of this SendMessageInputObject.

        The 2-letter ISO country code for local phone numbers, used when \\'local\\' is set to true. Default is the account country.  # noqa: E501

        :param local_country: The local_country of this SendMessageInputObject.  # noqa: E501
        :type: str
        """

        self._local_country = local_country

    @property
    def destination(self):
        """Gets the destination of this SendMessageInputObject.  # noqa: E501

        Messsage destination type allowed [mms, tts].  # noqa: E501

        :return: The destination of this SendMessageInputObject.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this SendMessageInputObject.

        Messsage destination type allowed [mms, tts].  # noqa: E501

        :param destination: The destination of this SendMessageInputObject.  # noqa: E501
        :type: str
        """

        self._destination = destination

    @property
    def resources(self):
        """Gets the resources of this SendMessageInputObject.  # noqa: E501

        File name from mms attachment response (named as resource)  # noqa: E501

        :return: The resources of this SendMessageInputObject.  # noqa: E501
        :rtype: str
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this SendMessageInputObject.

        File name from mms attachment response (named as resource)  # noqa: E501

        :param resources: The resources of this SendMessageInputObject.  # noqa: E501
        :type: str
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
        if issubclass(SendMessageInputObject, dict):
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
        if not isinstance(other, SendMessageInputObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
