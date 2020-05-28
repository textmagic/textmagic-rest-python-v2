# SendMessageInputObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Message text. Required if the **template_id** is not set. | [optional] 
**template_id** | **int** | Template used instead of message text. Required if the **text** is not set. | [optional] 
**sending_time** | **int** | DEPRECATED, consider using sendingDateTime and sendingTimezone parameters instead: Optional (required with rrule set). Message sending time in unix timestamp format. Default is now. | [optional] 
**sending_date_time** | **str** | Sending time in Y-m-d H:i:s format (e.g. 2016-05-27 13:02:33). This time is relative to **sendingTimezone**. | [optional] 
**sending_timezone** | **str** | ID or ISO-name of timezone used for sending when sendingDateTime parameter is set. E.g. if you specify sendingDateTime &#x3D; \\\&quot;2016-05-27 13:02:33\\\&quot; and sendingTimezone &#x3D; \\\&quot;America/Buenos_Aires\\\&quot;, your message will be sent at May 27, 2016 13:02:33 Buenos Aires time, or 16:02:33 UTC. Default is account timezone. | [optional] 
**contacts** | **str** | Comma separated array of contact resources id message will be sent to. | [optional] 
**lists** | **str** | Comma separated array of list resources id message will be sent to. | [optional] 
**phones** | **str** | Comma separated array of E.164 phone numbers message will be sent to. | [optional] 
**cut_extra** | **bool** | Should sending method cut extra characters which not fit supplied partsCount or return 400 Bad request response instead. | [optional] [default to False]
**parts_count** | **int** | Maximum message parts count (TextMagic allows sending 1 to 6 message parts). | [optional] 
**reference_id** | **int** | Custom message reference id which can be used in your application infrastructure. | [optional] 
**_from** | **str** | One of allowed Sender ID (phone number or alphanumeric sender ID). If specified Sender ID is not allowed for some destinations, a fallback default Sender ID will be used to ensure delivery. See [Get timezones](https://docs.textmagic.com/#tag/Sender-IDs). | [optional] 
**rrule** | **str** | iCal RRULE parameter to create recurrent scheduled messages. When used, sendingTime is mandatory as start point of sending. See https://www.textmagic.com/free-tools/rrule-generator for format details. | [optional] 
**create_chat** | **bool** | Should sending method try to create new Chat (if not exist) with specified recipients? | [optional] [default to False]
**tts** | **bool** | Send a Text-to-Speech message. | [optional] [default to False]
**local** | **bool** | Treat phone numbers passed in the \\&#39;phones\\&#39; field as local. | [optional] [default to False]
**local_country** | **str** | The 2-letter ISO country code for local phone numbers, used when \\&#39;local\\&#39; is set to true. Default is the account country. | [optional] 
**destination** | **str** | Messsage destination type allowed [mms, tts]. | [optional] [default to 'false']
**resources** | **str** | File name from mms attachment response (named as resource) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


