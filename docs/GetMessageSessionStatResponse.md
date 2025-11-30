# GetMessageSessionStatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed** | **int** | Amount of failed messages. | 
**delivered** | **int** | Amount of delivered messages. | 
**accepted** | **int** | Amount of accepted messages. | 
**rejected** | **int** | Amount of rejected messages. | 
**scheduled** | **int** | Amount of scheduled messages. | 
**all** | **int** | Total amount of messages. | 
**sent** | **int** | Amount of sent but not yet delivered messages. | 

## Example

```python
from TextMagic.models.get_message_session_stat_response import GetMessageSessionStatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessageSessionStatResponse from a JSON string
get_message_session_stat_response_instance = GetMessageSessionStatResponse.from_json(json)
# print the JSON string representation of the object
print(GetMessageSessionStatResponse.to_json())

# convert the object into a dict
get_message_session_stat_response_dict = get_message_session_stat_response_instance.to_dict()
# create an instance of GetMessageSessionStatResponse from a dict
get_message_session_stat_response_from_dict = GetMessageSessionStatResponse.from_dict(get_message_session_stat_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


