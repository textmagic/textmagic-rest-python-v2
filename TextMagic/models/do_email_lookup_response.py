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


class DoEmailLookupResponse(object):
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
        'address': 'str',
        'status': 'str',
        'deliverability': 'str',
        'reason': 'str',
        'risk': 'str',
        'address_type': 'str',
        'is_disposable_address': 'bool',
        'suggestion': 'str',
        'email_role': 'str',
        'local_part': 'str',
        'domain_part': 'str',
        'exchange': 'str',
        'preference': 'int',
        'is_in_white_list': 'bool',
        'is_in_black_list': 'bool',
        'has_mx': 'bool',
        'has_aa': 'bool',
        'has_aaaa': 'bool'
    }

    attribute_map = {
        'address': 'address',
        'status': 'status',
        'deliverability': 'deliverability',
        'reason': 'reason',
        'risk': 'risk',
        'address_type': 'addressType',
        'is_disposable_address': 'isDisposableAddress',
        'suggestion': 'suggestion',
        'email_role': 'emailRole',
        'local_part': 'localPart',
        'domain_part': 'domainPart',
        'exchange': 'exchange',
        'preference': 'preference',
        'is_in_white_list': 'isInWhiteList',
        'is_in_black_list': 'isInBlackList',
        'has_mx': 'hasMx',
        'has_aa': 'hasAa',
        'has_aaaa': 'hasAaaa'
    }

    def __init__(self, address=None, status=None, deliverability=None, reason=None, risk=None, address_type=None, is_disposable_address=None, suggestion=None, email_role=None, local_part=None, domain_part=None, exchange=None, preference=None, is_in_white_list=None, is_in_black_list=None, has_mx=None, has_aa=None, has_aaaa=None):  # noqa: E501
        """DoEmailLookupResponse - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._status = None
        self._deliverability = None
        self._reason = None
        self._risk = None
        self._address_type = None
        self._is_disposable_address = None
        self._suggestion = None
        self._email_role = None
        self._local_part = None
        self._domain_part = None
        self._exchange = None
        self._preference = None
        self._is_in_white_list = None
        self._is_in_black_list = None
        self._has_mx = None
        self._has_aa = None
        self._has_aaaa = None
        self.discriminator = None

        self.address = address
        self.status = status
        self.deliverability = deliverability
        self.reason = reason
        self.risk = risk
        self.address_type = address_type
        self.is_disposable_address = is_disposable_address
        self.suggestion = suggestion
        self.email_role = email_role
        self.local_part = local_part
        self.domain_part = domain_part
        self.exchange = exchange
        self.preference = preference
        self.is_in_white_list = is_in_white_list
        self.is_in_black_list = is_in_black_list
        self.has_mx = has_mx
        self.has_aa = has_aa
        self.has_aaaa = has_aaaa

    @property
    def address(self):
        """Gets the address of this DoEmailLookupResponse.  # noqa: E501

        The email address passed to the call.  # noqa: E501

        :return: The address of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this DoEmailLookupResponse.

        The email address passed to the call.  # noqa: E501

        :param address: The address of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def status(self):
        """Gets the status of this DoEmailLookupResponse.  # noqa: E501

        The email is `valid` or `invalid`.  # noqa: E501

        :return: The status of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DoEmailLookupResponse.

        The email is `valid` or `invalid`.  # noqa: E501

        :param status: The status of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["valid", "invalid"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def deliverability(self):
        """Gets the deliverability of this DoEmailLookupResponse.  # noqa: E501

        The delivery status of the email address is`deliverable`, `undeliverable`  or `unknown`.  # noqa: E501

        :return: The deliverability of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._deliverability

    @deliverability.setter
    def deliverability(self, deliverability):
        """Sets the deliverability of this DoEmailLookupResponse.

        The delivery status of the email address is`deliverable`, `undeliverable`  or `unknown`.  # noqa: E501

        :param deliverability: The deliverability of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._deliverability = deliverability

    @property
    def reason(self):
        """Gets the reason of this DoEmailLookupResponse.  # noqa: E501

        The reason why the checked email is invalid/undeliverable.  # noqa: E501

        :return: The reason of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this DoEmailLookupResponse.

        The reason why the checked email is invalid/undeliverable.  # noqa: E501

        :param reason: The reason of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def risk(self):
        """Gets the risk of this DoEmailLookupResponse.  # noqa: E501

        The risk score of the email is`high`, `medium`, `low` or `null`.  # noqa: E501

        :return: The risk of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        """Sets the risk of this DoEmailLookupResponse.

        The risk score of the email is`high`, `medium`, `low` or `null`.  # noqa: E501

        :param risk: The risk of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["high", "medium", "low", "unknown"]  # noqa: E501
        if risk not in allowed_values:
            raise ValueError(
                "Invalid value for `risk` ({0}), must be one of {1}"  # noqa: E501
                .format(risk, allowed_values)
            )

        self._risk = risk

    @property
    def address_type(self):
        """Gets the address_type of this DoEmailLookupResponse.  # noqa: E501

        The email address type (domain) is `free` or `corporate`.  # noqa: E501

        :return: The address_type of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this DoEmailLookupResponse.

        The email address type (domain) is `free` or `corporate`.  # noqa: E501

        :param address_type: The address_type of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["corporate", "free"]  # noqa: E501
        if address_type not in allowed_values:
            raise ValueError(
                "Invalid value for `address_type` ({0}), must be one of {1}"  # noqa: E501
                .format(address_type, allowed_values)
            )

        self._address_type = address_type

    @property
    def is_disposable_address(self):
        """Gets the is_disposable_address of this DoEmailLookupResponse.  # noqa: E501

        This is `true` if the domain is in the list of disposable email addresses; otherwise, it returns as `false`.  # noqa: E501

        :return: The is_disposable_address of this DoEmailLookupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_disposable_address

    @is_disposable_address.setter
    def is_disposable_address(self, is_disposable_address):
        """Sets the is_disposable_address of this DoEmailLookupResponse.

        This is `true` if the domain is in the list of disposable email addresses; otherwise, it returns as `false`.  # noqa: E501

        :param is_disposable_address: The is_disposable_address of this DoEmailLookupResponse.  # noqa: E501
        :type: bool
        """

        self._is_disposable_address = is_disposable_address

    @property
    def suggestion(self):
        """Gets the suggestion of this DoEmailLookupResponse.  # noqa: E501

        Null if nothing is suggested; however, if there is a potential typo in the email address, the closest suggestion is provided.  # noqa: E501

        :return: The suggestion of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this DoEmailLookupResponse.

        Null if nothing is suggested; however, if there is a potential typo in the email address, the closest suggestion is provided.  # noqa: E501

        :param suggestion: The suggestion of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._suggestion = suggestion

    @property
    def email_role(self):
        """Gets the email_role of this DoEmailLookupResponse.  # noqa: E501

        Checks the mailbox part of the email to see whether it matches a specific role type (‘admin’, ‘sales’, ‘webmaster’)  # noqa: E501

        :return: The email_role of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._email_role

    @email_role.setter
    def email_role(self, email_role):
        """Sets the email_role of this DoEmailLookupResponse.

        Checks the mailbox part of the email to see whether it matches a specific role type (‘admin’, ‘sales’, ‘webmaster’)  # noqa: E501

        :param email_role: The email_role of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._email_role = email_role

    @property
    def local_part(self):
        """Gets the local_part of this DoEmailLookupResponse.  # noqa: E501

        The local part of the email address.  # noqa: E501

        :return: The local_part of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._local_part

    @local_part.setter
    def local_part(self, local_part):
        """Sets the local_part of this DoEmailLookupResponse.

        The local part of the email address.  # noqa: E501

        :param local_part: The local_part of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._local_part = local_part

    @property
    def domain_part(self):
        """Gets the domain_part of this DoEmailLookupResponse.  # noqa: E501

        The domain part of the email address.  # noqa: E501

        :return: The domain_part of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._domain_part

    @domain_part.setter
    def domain_part(self, domain_part):
        """Sets the domain_part of this DoEmailLookupResponse.

        The domain part of the email address.  # noqa: E501

        :param domain_part: The domain_part of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._domain_part = domain_part

    @property
    def exchange(self):
        """Gets the exchange of this DoEmailLookupResponse.  # noqa: E501

        Email exchange server domain name (MX record value).  # noqa: E501

        :return: The exchange of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this DoEmailLookupResponse.

        Email exchange server domain name (MX record value).  # noqa: E501

        :param exchange: The exchange of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

    @property
    def preference(self):
        """Gets the preference of this DoEmailLookupResponse.  # noqa: E501

        MX record preference.  # noqa: E501

        :return: The preference of this DoEmailLookupResponse.  # noqa: E501
        :rtype: int
        """
        return self._preference

    @preference.setter
    def preference(self, preference):
        """Sets the preference of this DoEmailLookupResponse.

        MX record preference.  # noqa: E501

        :param preference: The preference of this DoEmailLookupResponse.  # noqa: E501
        :type: int
        """

        self._preference = preference

    @property
    def is_in_white_list(self):
        """Gets the is_in_white_list of this DoEmailLookupResponse.  # noqa: E501

        `true` if the email address exists in the TextMagic whitelist.   # noqa: E501

        :return: The is_in_white_list of this DoEmailLookupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_white_list

    @is_in_white_list.setter
    def is_in_white_list(self, is_in_white_list):
        """Sets the is_in_white_list of this DoEmailLookupResponse.

        `true` if the email address exists in the TextMagic whitelist.   # noqa: E501

        :param is_in_white_list: The is_in_white_list of this DoEmailLookupResponse.  # noqa: E501
        :type: bool
        """

        self._is_in_white_list = is_in_white_list

    @property
    def is_in_black_list(self):
        """Gets the is_in_black_list of this DoEmailLookupResponse.  # noqa: E501

        `true` if the email address exists in the TextMagic blacklist.   # noqa: E501

        :return: The is_in_black_list of this DoEmailLookupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_black_list

    @is_in_black_list.setter
    def is_in_black_list(self, is_in_black_list):
        """Sets the is_in_black_list of this DoEmailLookupResponse.

        `true` if the email address exists in the TextMagic blacklist.   # noqa: E501

        :param is_in_black_list: The is_in_black_list of this DoEmailLookupResponse.  # noqa: E501
        :type: bool
        """

        self._is_in_black_list = is_in_black_list

    @property
    def has_mx(self):
        """Gets the has_mx of this DoEmailLookupResponse.  # noqa: E501

        `true` if the email address domain has an MX record.   # noqa: E501

        :return: The has_mx of this DoEmailLookupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_mx

    @has_mx.setter
    def has_mx(self, has_mx):
        """Sets the has_mx of this DoEmailLookupResponse.

        `true` if the email address domain has an MX record.   # noqa: E501

        :param has_mx: The has_mx of this DoEmailLookupResponse.  # noqa: E501
        :type: bool
        """

        self._has_mx = has_mx

    @property
    def has_aa(self):
        """Gets the has_aa of this DoEmailLookupResponse.  # noqa: E501

        `true` if the email address domain has an A record (IPv4).   # noqa: E501

        :return: The has_aa of this DoEmailLookupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_aa

    @has_aa.setter
    def has_aa(self, has_aa):
        """Sets the has_aa of this DoEmailLookupResponse.

        `true` if the email address domain has an A record (IPv4).   # noqa: E501

        :param has_aa: The has_aa of this DoEmailLookupResponse.  # noqa: E501
        :type: bool
        """

        self._has_aa = has_aa

    @property
    def has_aaaa(self):
        """Gets the has_aaaa of this DoEmailLookupResponse.  # noqa: E501

        `true` if the email address domain has an AAAA record (IPv6).   # noqa: E501

        :return: The has_aaaa of this DoEmailLookupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_aaaa

    @has_aaaa.setter
    def has_aaaa(self, has_aaaa):
        """Sets the has_aaaa of this DoEmailLookupResponse.

        `true` if the email address domain has an AAAA record (IPv6).   # noqa: E501

        :param has_aaaa: The has_aaaa of this DoEmailLookupResponse.  # noqa: E501
        :type: bool
        """

        self._has_aaaa = has_aaaa

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
        if issubclass(DoEmailLookupResponse, dict):
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
        if not isinstance(other, DoEmailLookupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
