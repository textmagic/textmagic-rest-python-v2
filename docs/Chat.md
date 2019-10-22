# Chat

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Chat ID. | 
**original_id** | **int** |  | 
**phone** | **str** | Chat partner phone number. | 
**contact** | [**Contact**](Contact.md) |  | 
**unsubscribed_contact_id** | **int** | If this field has a value then it means that chat phone number has been unsubscribed from you and this value is a ID of a Unsubscribed contact entity. See [Get all unsubscribed contacts](http://docs.textmagictesting.com/#operation/getUnsubscribers). | 
**unread** | **int** | Total unread incoming messages. | 
**updated_at** | **datetime** | Time when last incoming message arrived at this chat. | 
**status** | **str** | Chat status:   * **a** - Active   * **c** - Closed   * **d** - Deleted  | 
**mute** | **int** | Indicates when chat is muted. | 
**last_message** | **str** | The last message content of a chat. | 
**direction** | **str** | Last message type: * **ci** - incoming call * **co** - outgoing call * **i** - incoming message * **o** - outgoing message  | 
**_from** | **str** | If filled then value will be used as a sender number for all outgoing messages of a chat. | 
**muted_until** | **datetime** | Date and time until chat will be mutted. | 
**time_left_mute** | **int** | Time left till chat will be unmutted (seconds). | 
**country** | [**Country**](Country.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


