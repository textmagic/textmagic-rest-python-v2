# MessageOutSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**start_time** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**numbers_count** | **int** |  | [optional] 
**destination** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**initiator_id** | **int** |  | [optional] 

## Example

```python
from TextMagic.models.message_out_session import MessageOutSession

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOutSession from a JSON string
message_out_session_instance = MessageOutSession.from_json(json)
# print the JSON string representation of the object
print(MessageOutSession.to_json())

# convert the object into a dict
message_out_session_dict = message_out_session_instance.to_dict()
# create an instance of MessageOutSession from a dict
message_out_session_from_dict = MessageOutSession.from_dict(message_out_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


