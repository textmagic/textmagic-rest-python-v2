# MessageOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Message ID. | 
**sender** | **str** | Message sender (phone number or alphanumeric Sender ID). | [optional] 
**receiver** | **str** | Recipient phone number. | [optional] 
**text** | **str** |  | 
**status** | **str** | Delivery status of the message. See [message delivery statuses](http://docs.textmagictesting.com/#section/Delivery-status-codes) for details.  | 
**contact_id** | **int** | Recipient contact ID. | 
**session_id** | **int** | Message Session ID of a Message. | 
**message_time** | **datetime** | Sending time. | 
**avatar** | **str** |  | 
**deleted** | **bool** | Indicates that the message has been deleted. | [optional] 
**charset** | **str** | Message charset. Could be: *   **ISO-8859-1** for plaintext SMS; *   **UTF-16BE** for Unicode SMS.  | 
**charset_label** | **str** | Human-readable message charset label. Could be: *   **ISO-8859-1** for plaintext SMS; *   **UTF-16BE** for Unicode SMS; *   **Voice** for voice services (Text-to-Speech or Voice Broadcast) messages.  | 
**first_name** | **str** | Contact first name. Could be substituted from your [Contacts](http://docs.textmagictesting.com/#tag/Contacts) (even if you submitted the phone number instead of the contact ID).  | 
**last_name** | **str** | Contact last name. | 
**country** | **str** | The 2-letter ISO country code of the recipient&#39;s phone number.  | 
**phone** | **str** | Receipent phone number. | [optional] 
**price** | **float** | Message price. | [optional] 
**parts_count** | **int** | Message parts (multiples of 160 characters) count. | 
**from_email** | **str** | The user email which this message came from. For Email2SMS and Distribution Lists the message will come from an original email address; in other cases, it will come from an account email address. | [optional] 
**from_number** | **str** | The Phone number used to send the SMS. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


