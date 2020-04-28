# Chat

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Chat ID. | 
**original_id** | **int** |  | 
**phone** | **str** | Chat partner&#39;s phone number. | 
**contact** | [**Contact**](Contact.md) |  | 
**unsubscribed_contact_id** | **int** | If this field has a value, it means that the chat phone number has been unsubscribed from you and this value is an ID of an Unsubscribed contact entity. See [Get all unsubscribed contacts](https://docs.textmagic.com/#operation/getUnsubscribers). | 
**unread** | **int** | Total unread incoming messages. | 
**updated_at** | **datetime** | Time when the last incoming message arrived at this chat. | 
**status** | **str** | Chat status:   * **a** - Active;   * **c** - Closed;   * **d** - Deleted.  | 
**mute** | **int** | Indicates when the chat is muted. | 
**last_message** | **str** | The last message content of a chat. | 
**direction** | **str** | Last message type: * **ci** - incoming call; * **co** - outgoing call; * **i** - incoming message; * **o** - outgoing message.  | 
**_from** | **str** | If filled, the value will be used as a sender number for all outgoing messages of a chat. | 
**muted_until** | **datetime** | Date and time until the chat will be muted. | 
**time_left_mute** | **int** | Time left untill the chat will be unmuted (seconds). | 
**country** | [**Country**](Country.md) |  | 
**pinned** | **bool** | Indicates when the chat is pinned. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


