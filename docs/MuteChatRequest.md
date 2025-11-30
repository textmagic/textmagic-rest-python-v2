# MuteChatRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Chat ID. | [optional] 
**mute** | **bool** | Mute notifications sound. | [optional] 
**var_for** | **int** | Mute for N hours. | [optional] 

## Example

```python
from TextMagic.models.mute_chat_request import MuteChatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MuteChatRequest from a JSON string
mute_chat_request_instance = MuteChatRequest.from_json(json)
# print the JSON string representation of the object
print(MuteChatRequest.to_json())

# convert the object into a dict
mute_chat_request_dict = mute_chat_request_instance.to_dict()
# create an instance of MuteChatRequest from a dict
mute_chat_request_from_dict = MuteChatRequest.from_dict(mute_chat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


