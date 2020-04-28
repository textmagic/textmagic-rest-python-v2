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


class SendPhoneVerificationCodeTFAInputObject(object):
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
        'phone': 'str',
        'workflow_id': 'str',
        'brand': 'str',
        'code_length': 'int',
        'language': 'str',
        'sender_id': 'str',
        'country': 'str'
    }

    attribute_map = {
        'phone': 'phone',
        'workflow_id': 'workflowId',
        'brand': 'brand',
        'code_length': 'codeLength',
        'language': 'language',
        'sender_id': 'senderId',
        'country': 'country'
    }

    def __init__(self, phone=None, workflow_id=None, brand=None, code_length=None, language=None, sender_id=None, country=None):  # noqa: E501
        """SendPhoneVerificationCodeTFAInputObject - a model defined in Swagger"""  # noqa: E501

        self._phone = None
        self._workflow_id = None
        self._brand = None
        self._code_length = None
        self._language = None
        self._sender_id = None
        self._country = None
        self.discriminator = None

        if phone is not None:
            self.phone = phone
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if brand is not None:
            self.brand = brand
        if code_length is not None:
            self.code_length = code_length
        if language is not None:
            self.language = language
        if sender_id is not None:
            self.sender_id = sender_id
        if country is not None:
            self.country = country

    @property
    def phone(self):
        """Gets the phone of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501

        Use the phone number in international E.164 format. If you need to pass a phone number in the local format, please use it with the **country** parameter to specify the origin country of the phone number.   # noqa: E501

        :return: The phone of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this SendPhoneVerificationCodeTFAInputObject.

        Use the phone number in international E.164 format. If you need to pass a phone number in the local format, please use it with the **country** parameter to specify the origin country of the phone number.   # noqa: E501

        :param phone: The phone of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def workflow_id(self):
        """Gets the workflow_id of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501

        **Workflows**  The Verify API allows you to select the best workflow for your use case. This might depend on the type of verification taking place, your users' preference, or their geographical location. You can specify which workflow to use for each Verify API request by setting the workflowId field to an integer value 1-7. The details of each of these preset workflows are detailed below.  <br />  **Workflow 1 (Default Workflow): SMS -> TTS -> TTS**  <br />  Send PIN code by text message, follow up with two subsequent voice calls if the request wasn't already verified.  Send SMS to user with PIN code Wait for 60 seconds Call user and give TTS PIN code Wait for 60 seconds Call user and give TTS PIN code  Request expires after 300 seconds  <br />  **Workflow 2: SMS -> SMS -> TTS**  <br />    Send PIN code by text message, follow up with a second text message and finally a voice call if the request has not been verified.  Send SMS to user with PIN code Wait for 60 seconds Send SMS to user with PIN code Wait for 60 seconds Call user and give TTS PIN code  Request expires after 300 seconds  <br />  **Workflow 3: TTS -> TTS**  <br />   Call the user and speak a PIN code, follow up with a second call if the request wasn't already verified.  Call user and give TTS PIN code Wait for 60 seconds Call user and give TTS PIN code  Request expires after 300 seconds  <br />  **Workflow 4: SMS -> SMS**  <br />    Send PIN code by text message, follow up with a second text message if the code hasn't been verified.  Send SMS to user with PIN code Wait for 60 seconds Send SMS to user with PIN code Wait for 60 seconds  Request expires after 300 seconds  <br />  **Workflow 5: SMS -> TTS**  <br />   Send PIN code by text message, follow up with a voice call if the code hasn't been verified.  Send SMS to user with PIN code Wait for 60 seconds Call user and give TTS PIN code Wait for 60 seconds  Request expires after 300 seconds  <br />  **Workflow 6: SMS**  <br />   Send PIN code by text message once only.  Send SMS to user with PIN code Request expires after 300 seconds  <br />  **Workflow 7: TTS**  <br />  Call the user and speak a PIN code once only.  Call user and give TTS PIN code  Request expires after 300 seconds   # noqa: E501

        :return: The workflow_id of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this SendPhoneVerificationCodeTFAInputObject.

        **Workflows**  The Verify API allows you to select the best workflow for your use case. This might depend on the type of verification taking place, your users' preference, or their geographical location. You can specify which workflow to use for each Verify API request by setting the workflowId field to an integer value 1-7. The details of each of these preset workflows are detailed below.  <br />  **Workflow 1 (Default Workflow): SMS -> TTS -> TTS**  <br />  Send PIN code by text message, follow up with two subsequent voice calls if the request wasn't already verified.  Send SMS to user with PIN code Wait for 60 seconds Call user and give TTS PIN code Wait for 60 seconds Call user and give TTS PIN code  Request expires after 300 seconds  <br />  **Workflow 2: SMS -> SMS -> TTS**  <br />    Send PIN code by text message, follow up with a second text message and finally a voice call if the request has not been verified.  Send SMS to user with PIN code Wait for 60 seconds Send SMS to user with PIN code Wait for 60 seconds Call user and give TTS PIN code  Request expires after 300 seconds  <br />  **Workflow 3: TTS -> TTS**  <br />   Call the user and speak a PIN code, follow up with a second call if the request wasn't already verified.  Call user and give TTS PIN code Wait for 60 seconds Call user and give TTS PIN code  Request expires after 300 seconds  <br />  **Workflow 4: SMS -> SMS**  <br />    Send PIN code by text message, follow up with a second text message if the code hasn't been verified.  Send SMS to user with PIN code Wait for 60 seconds Send SMS to user with PIN code Wait for 60 seconds  Request expires after 300 seconds  <br />  **Workflow 5: SMS -> TTS**  <br />   Send PIN code by text message, follow up with a voice call if the code hasn't been verified.  Send SMS to user with PIN code Wait for 60 seconds Call user and give TTS PIN code Wait for 60 seconds  Request expires after 300 seconds  <br />  **Workflow 6: SMS**  <br />   Send PIN code by text message once only.  Send SMS to user with PIN code Request expires after 300 seconds  <br />  **Workflow 7: TTS**  <br />  Call the user and speak a PIN code once only.  Call user and give TTS PIN code  Request expires after 300 seconds   # noqa: E501

        :param workflow_id: The workflow_id of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501
        :type: str
        """

        self._workflow_id = workflow_id

    @property
    def brand(self):
        """Gets the brand of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501

        An alphanumeric string with up to 18 characters you can use to personalize the verification text message body, to help users identify your company or application name. For example: “Your TextMagic PIN is …”   # noqa: E501

        :return: The brand of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this SendPhoneVerificationCodeTFAInputObject.

        An alphanumeric string with up to 18 characters you can use to personalize the verification text message body, to help users identify your company or application name. For example: “Your TextMagic PIN is …”   # noqa: E501

        :param brand: The brand of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def code_length(self):
        """Gets the code_length of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501

        The length of the verification code. The value can be 4 or 6 characters.   # noqa: E501

        :return: The code_length of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501
        :rtype: int
        """
        return self._code_length

    @code_length.setter
    def code_length(self, code_length):
        """Sets the code_length of this SendPhoneVerificationCodeTFAInputObject.

        The length of the verification code. The value can be 4 or 6 characters.   # noqa: E501

        :param code_length: The code_length of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501
        :type: int
        """

        self._code_length = code_length

    @property
    def language(self):
        """Gets the language of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501

        By default, the SMS or text-to-speech (TTS) voice message is generated in the locale that matches the number. For example, the text message or TTS message for a 33\\* number is sent in French. Use this parameter to explicitly control the language, accent, and gender used for the verification request. Choosing one of the following: `de-de`, `en-au`, `en-gb`, `en-us`, `en-in`, `es-es`, `es-mx`, `es-us`, `fr-ca`, `fr-fr`, `is-is`, `it-it`, `ja-jp`, `ko-kr`, `nl-nl`, `pl-pl`, `pt-pt`, `pt-br`, `ro-ro`, `ru-ru`, `sv-se`, `tr-tr`, `zh-cn` or `zh-tw`.   # noqa: E501

        :return: The language of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SendPhoneVerificationCodeTFAInputObject.

        By default, the SMS or text-to-speech (TTS) voice message is generated in the locale that matches the number. For example, the text message or TTS message for a 33\\* number is sent in French. Use this parameter to explicitly control the language, accent, and gender used for the verification request. Choosing one of the following: `de-de`, `en-au`, `en-gb`, `en-us`, `en-in`, `es-es`, `es-mx`, `es-us`, `fr-ca`, `fr-fr`, `is-is`, `it-it`, `ja-jp`, `ko-kr`, `nl-nl`, `pl-pl`, `pt-pt`, `pt-br`, `ro-ro`, `ru-ru`, `sv-se`, `tr-tr`, `zh-cn` or `zh-tw`.   # noqa: E501

        :param language: The language of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def sender_id(self):
        """Gets the sender_id of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501

        One of the available [sender settings](https://my.textmagic.com/online/reply-options/) on your TextMagic account. If the specified sender setting type is not allowed for some destinations, a fallback default sender will be used to ensure message delivery. More info about known restrictions can be found [here](https://support.textmagic.com/article/how-to-understand-sender-setting-restrictions/).   # noqa: E501

        :return: The sender_id of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501
        :rtype: str
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        """Sets the sender_id of this SendPhoneVerificationCodeTFAInputObject.

        One of the available [sender settings](https://my.textmagic.com/online/reply-options/) on your TextMagic account. If the specified sender setting type is not allowed for some destinations, a fallback default sender will be used to ensure message delivery. More info about known restrictions can be found [here](https://support.textmagic.com/article/how-to-understand-sender-setting-restrictions/).   # noqa: E501

        :param sender_id: The sender_id of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501
        :type: str
        """

        self._sender_id = sender_id

    @property
    def country(self):
        """Gets the country of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501

        The 2-letter ISO country code for the local phone number.  # noqa: E501

        :return: The country of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this SendPhoneVerificationCodeTFAInputObject.

        The 2-letter ISO country code for the local phone number.  # noqa: E501

        :param country: The country of this SendPhoneVerificationCodeTFAInputObject.  # noqa: E501
        :type: str
        """

        self._country = country

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
        if issubclass(SendPhoneVerificationCodeTFAInputObject, dict):
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
        if not isinstance(other, SendPhoneVerificationCodeTFAInputObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
