# MessagePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Payload type. | 
**media_preview** | **str** | Media preview link. | 

## Example

```python
from TextMagic.models.message_payload import MessagePayload

# TODO update the JSON string below
json = "{}"
# create an instance of MessagePayload from a JSON string
message_payload_instance = MessagePayload.from_json(json)
# print the JSON string representation of the object
print(MessagePayload.to_json())

# convert the object into a dict
message_payload_dict = message_payload_instance.to_dict()
# create an instance of MessagePayload from a dict
message_payload_from_dict = MessagePayload.from_dict(message_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


