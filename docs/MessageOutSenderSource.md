# MessageOutSenderSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**phone** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**carrier_status** | **str** |  | [optional] 

## Example

```python
from TextMagic.models.message_out_sender_source import MessageOutSenderSource

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOutSenderSource from a JSON string
message_out_sender_source_instance = MessageOutSenderSource.from_json(json)
# print the JSON string representation of the object
print(MessageOutSenderSource.to_json())

# convert the object into a dict
message_out_sender_source_dict = message_out_sender_source_instance.to_dict()
# create an instance of MessageOutSenderSource from a dict
message_out_sender_source_from_dict = MessageOutSenderSource.from_dict(message_out_sender_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


