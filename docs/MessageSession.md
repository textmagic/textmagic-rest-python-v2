# MessageSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Session ID. | 
**start_time** | **str** | Session creation time. | 
**text** | **str** | Session text. If a template was used for the session text (see [Messages: Send](https://docs.textmagic.com/#tag/Outbound-Messages) for details), it may contain template tags.  | 
**source** | **str** | *   **O** – for Textmagic Online; *   **A** – for API; *   **M** – for Textmagic Messenger; *   **E** – for [Email to SMS](https://docs.textmagic.com/#tag/Send-Email-to-SMS); *   **X** – for [Distribution Lists](https://docs.textmagic.com/#tag/Distribution-Lists).  | 
**reference_id** | **str** | Custom reference ID (see [Messages: Send](https://docs.textmagic.com/#tag/Send-Email-to-SMS) for details).  | 
**price** | **float** | Session cost (in account currency). | 
**numbers_count** | **int** | Session recipient count. | 
**destination** | **str** | Destination type of a Message Session: * **t** – text SMS; * **s** – text-to-speech; * **v** – voice broadcast.  | 
**initiator_id** | **int** | Initiator ID. | 
**title** | **str** |  | 

## Example

```python
from TextMagic.models.message_session import MessageSession

# TODO update the JSON string below
json = "{}"
# create an instance of MessageSession from a JSON string
message_session_instance = MessageSession.from_json(json)
# print the JSON string representation of the object
print(MessageSession.to_json())

# convert the object into a dict
message_session_dict = message_session_instance.to_dict()
# create an instance of MessageSession from a dict
message_session_from_dict = MessageSession.from_dict(message_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


