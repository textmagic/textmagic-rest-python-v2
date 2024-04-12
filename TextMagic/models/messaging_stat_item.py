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


class MessagingStatItem(object):
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
        'reply_rate': 'float',
        '_date': 'datetime',
        'delivery_rate': 'float',
        'costs': 'float',
        'messages_received': 'int',
        'messages_sent_delivered': 'int',
        'messages_sent_accepted': 'int',
        'messages_sent_buffered': 'int',
        'messages_sent_failed': 'int',
        'messages_sent_rejected': 'int',
        'messages_sent_parts': 'int'
    }

    attribute_map = {
        'reply_rate': 'replyRate',
        '_date': 'date',
        'delivery_rate': 'deliveryRate',
        'costs': 'costs',
        'messages_received': 'messagesReceived',
        'messages_sent_delivered': 'messagesSentDelivered',
        'messages_sent_accepted': 'messagesSentAccepted',
        'messages_sent_buffered': 'messagesSentBuffered',
        'messages_sent_failed': 'messagesSentFailed',
        'messages_sent_rejected': 'messagesSentRejected',
        'messages_sent_parts': 'messagesSentParts'
    }

    def __init__(self, reply_rate=None, _date=None, delivery_rate=None, costs=None, messages_received=None, messages_sent_delivered=None, messages_sent_accepted=None, messages_sent_buffered=None, messages_sent_failed=None, messages_sent_rejected=None, messages_sent_parts=None):  # noqa: E501
        """MessagingStatItem - a model defined in Swagger"""  # noqa: E501

        self._reply_rate = None
        self.__date = None
        self._delivery_rate = None
        self._costs = None
        self._messages_received = None
        self._messages_sent_delivered = None
        self._messages_sent_accepted = None
        self._messages_sent_buffered = None
        self._messages_sent_failed = None
        self._messages_sent_rejected = None
        self._messages_sent_parts = None
        self.discriminator = None

        self.reply_rate = reply_rate
        self._date = _date
        self.delivery_rate = delivery_rate
        self.costs = costs
        self.messages_received = messages_received
        self.messages_sent_delivered = messages_sent_delivered
        self.messages_sent_accepted = messages_sent_accepted
        self.messages_sent_buffered = messages_sent_buffered
        self.messages_sent_failed = messages_sent_failed
        self.messages_sent_rejected = messages_sent_rejected
        self.messages_sent_parts = messages_sent_parts

    @property
    def reply_rate(self):
        """Gets the reply_rate of this MessagingStatItem.  # noqa: E501

        The number of incoming messages divided by the number of total messages.  # noqa: E501

        :return: The reply_rate of this MessagingStatItem.  # noqa: E501
        :rtype: float
        """
        return self._reply_rate

    @reply_rate.setter
    def reply_rate(self, reply_rate):
        """Sets the reply_rate of this MessagingStatItem.

        The number of incoming messages divided by the number of total messages.  # noqa: E501

        :param reply_rate: The reply_rate of this MessagingStatItem.  # noqa: E501
        :type: float
        """

        self._reply_rate = reply_rate

    @property
    def _date(self):
        """Gets the _date of this MessagingStatItem.  # noqa: E501

        Time interval start: empty if the **by** parameter was set to **off**.   # noqa: E501

        :return: The _date of this MessagingStatItem.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this MessagingStatItem.

        Time interval start: empty if the **by** parameter was set to **off**.   # noqa: E501

        :param _date: The _date of this MessagingStatItem.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def delivery_rate(self):
        """Gets the delivery_rate of this MessagingStatItem.  # noqa: E501

        Message delivery rate:the number of delivered messages divided by the number of total messages.  # noqa: E501

        :return: The delivery_rate of this MessagingStatItem.  # noqa: E501
        :rtype: float
        """
        return self._delivery_rate

    @delivery_rate.setter
    def delivery_rate(self, delivery_rate):
        """Sets the delivery_rate of this MessagingStatItem.

        Message delivery rate:the number of delivered messages divided by the number of total messages.  # noqa: E501

        :param delivery_rate: The delivery_rate of this MessagingStatItem.  # noqa: E501
        :type: float
        """

        self._delivery_rate = delivery_rate

    @property
    def costs(self):
        """Gets the costs of this MessagingStatItem.  # noqa: E501

        Cost for sent messages during this period. The costs are in the [Account](https://docs.textmagic.com/#tag/User) currency.   # noqa: E501

        :return: The costs of this MessagingStatItem.  # noqa: E501
        :rtype: float
        """
        return self._costs

    @costs.setter
    def costs(self, costs):
        """Sets the costs of this MessagingStatItem.

        Cost for sent messages during this period. The costs are in the [Account](https://docs.textmagic.com/#tag/User) currency.   # noqa: E501

        :param costs: The costs of this MessagingStatItem.  # noqa: E501
        :type: float
        """

        self._costs = costs

    @property
    def messages_received(self):
        """Gets the messages_received of this MessagingStatItem.  # noqa: E501

        Total received messages count.  # noqa: E501

        :return: The messages_received of this MessagingStatItem.  # noqa: E501
        :rtype: int
        """
        return self._messages_received

    @messages_received.setter
    def messages_received(self, messages_received):
        """Sets the messages_received of this MessagingStatItem.

        Total received messages count.  # noqa: E501

        :param messages_received: The messages_received of this MessagingStatItem.  # noqa: E501
        :type: int
        """

        self._messages_received = messages_received

    @property
    def messages_sent_delivered(self):
        """Gets the messages_sent_delivered of this MessagingStatItem.  # noqa: E501

        Delivered messages count. As messages are retried for up to 48 hours, this value could change.  # noqa: E501

        :return: The messages_sent_delivered of this MessagingStatItem.  # noqa: E501
        :rtype: int
        """
        return self._messages_sent_delivered

    @messages_sent_delivered.setter
    def messages_sent_delivered(self, messages_sent_delivered):
        """Sets the messages_sent_delivered of this MessagingStatItem.

        Delivered messages count. As messages are retried for up to 48 hours, this value could change.  # noqa: E501

        :param messages_sent_delivered: The messages_sent_delivered of this MessagingStatItem.  # noqa: E501
        :type: int
        """

        self._messages_sent_delivered = messages_sent_delivered

    @property
    def messages_sent_accepted(self):
        """Gets the messages_sent_accepted of this MessagingStatItem.  # noqa: E501

        Messages accepted for delivery (in queue) but not yet delivered.  # noqa: E501

        :return: The messages_sent_accepted of this MessagingStatItem.  # noqa: E501
        :rtype: int
        """
        return self._messages_sent_accepted

    @messages_sent_accepted.setter
    def messages_sent_accepted(self, messages_sent_accepted):
        """Sets the messages_sent_accepted of this MessagingStatItem.

        Messages accepted for delivery (in queue) but not yet delivered.  # noqa: E501

        :param messages_sent_accepted: The messages_sent_accepted of this MessagingStatItem.  # noqa: E501
        :type: int
        """

        self._messages_sent_accepted = messages_sent_accepted

    @property
    def messages_sent_buffered(self):
        """Gets the messages_sent_buffered of this MessagingStatItem.  # noqa: E501

        Messages buffered by endpoint cell phone operators.  # noqa: E501

        :return: The messages_sent_buffered of this MessagingStatItem.  # noqa: E501
        :rtype: int
        """
        return self._messages_sent_buffered

    @messages_sent_buffered.setter
    def messages_sent_buffered(self, messages_sent_buffered):
        """Sets the messages_sent_buffered of this MessagingStatItem.

        Messages buffered by endpoint cell phone operators.  # noqa: E501

        :param messages_sent_buffered: The messages_sent_buffered of this MessagingStatItem.  # noqa: E501
        :type: int
        """

        self._messages_sent_buffered = messages_sent_buffered

    @property
    def messages_sent_failed(self):
        """Gets the messages_sent_failed of this MessagingStatItem.  # noqa: E501

        Messages that have failed for whatever reason, e.g. the destination phone was switched off for 48 hours or the recipient's phone account is out of service.  # noqa: E501

        :return: The messages_sent_failed of this MessagingStatItem.  # noqa: E501
        :rtype: int
        """
        return self._messages_sent_failed

    @messages_sent_failed.setter
    def messages_sent_failed(self, messages_sent_failed):
        """Sets the messages_sent_failed of this MessagingStatItem.

        Messages that have failed for whatever reason, e.g. the destination phone was switched off for 48 hours or the recipient's phone account is out of service.  # noqa: E501

        :param messages_sent_failed: The messages_sent_failed of this MessagingStatItem.  # noqa: E501
        :type: int
        """

        self._messages_sent_failed = messages_sent_failed

    @property
    def messages_sent_rejected(self):
        """Gets the messages_sent_rejected of this MessagingStatItem.  # noqa: E501

        Messages that were rejected: invalid Sender ID used (e.g. you cannot use the Sender ID or your own mobile number when sending to the United States and Canada.)   # noqa: E501

        :return: The messages_sent_rejected of this MessagingStatItem.  # noqa: E501
        :rtype: int
        """
        return self._messages_sent_rejected

    @messages_sent_rejected.setter
    def messages_sent_rejected(self, messages_sent_rejected):
        """Sets the messages_sent_rejected of this MessagingStatItem.

        Messages that were rejected: invalid Sender ID used (e.g. you cannot use the Sender ID or your own mobile number when sending to the United States and Canada.)   # noqa: E501

        :param messages_sent_rejected: The messages_sent_rejected of this MessagingStatItem.  # noqa: E501
        :type: int
        """

        self._messages_sent_rejected = messages_sent_rejected

    @property
    def messages_sent_parts(self):
        """Gets the messages_sent_parts of this MessagingStatItem.  # noqa: E501

        Total sent messages **parts** count. Note that this is not equal to the sent messages count, because one message could consist of 1 to 6 parts and users are charged per part, not per message.  # noqa: E501

        :return: The messages_sent_parts of this MessagingStatItem.  # noqa: E501
        :rtype: int
        """
        return self._messages_sent_parts

    @messages_sent_parts.setter
    def messages_sent_parts(self, messages_sent_parts):
        """Sets the messages_sent_parts of this MessagingStatItem.

        Total sent messages **parts** count. Note that this is not equal to the sent messages count, because one message could consist of 1 to 6 parts and users are charged per part, not per message.  # noqa: E501

        :param messages_sent_parts: The messages_sent_parts of this MessagingStatItem.  # noqa: E501
        :type: int
        """

        self._messages_sent_parts = messages_sent_parts

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
        if issubclass(MessagingStatItem, dict):
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
        if not isinstance(other, MessagingStatItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
