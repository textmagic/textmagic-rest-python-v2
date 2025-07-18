# Conversation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**direction** | **str** | Message type: inbound or outbound.  | 
**sender** | **str** | Sender phone number. | 
**message_time** | **datetime** | Time when  the message arrived at Textmagic. | 
**text** | **str** | Message text. | 
**receiver** | **str** | Receiver&#39;s phone number. | 
**status** | **str** | Message status (for chats outbound only). See [message delivery statuses](https://docs.textmagic.com/#section/Delivery-status-codes) for details. | 
**first_name** | **str** | Contact first name. | 
**last_name** | **str** | Contact last name. | 
**session_id** | **int** | Session ID of a message. See [message sessions](https://docs.textmagic.com/#tag/Outbound-Message-Sessions) for details. | 
**initiator_id** | **int** | Initiator ID of a message. See [message sessions](https://docs.textmagic.com/#tag/Outbound-Message-Sessions) for details. | [optional] 
**message_file_id** | **int** | Message file id. | [optional] 
**type** | **str** | Message type. | [optional] 
**chat_type** | **str** | Chat type. | [optional] 
**chat_id** | **int** | Chat id. | [optional] 
**is_edited** | **bool** |  | [optional] 
**error_code** | **str** | Error code. | [optional] 
**files** | [**list[File]**](File.md) |  | [optional] 
**payload** | [**MessagePayload**](MessagePayload.md) |  | [optional] 
**avatar** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


