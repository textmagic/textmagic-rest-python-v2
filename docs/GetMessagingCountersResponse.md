# GetMessagingCountersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | **int** | Total contacts amount. | 
**sent** | **int** | Total sent messages amount. | 
**received** | **int** | Total received messages amount. | 

## Example

```python
from TextMagic.models.get_messaging_counters_response import GetMessagingCountersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessagingCountersResponse from a JSON string
get_messaging_counters_response_instance = GetMessagingCountersResponse.from_json(json)
# print the JSON string representation of the object
print(GetMessagingCountersResponse.to_json())

# convert the object into a dict
get_messaging_counters_response_dict = get_messaging_counters_response_instance.to_dict()
# create an instance of GetMessagingCountersResponse from a dict
get_messaging_counters_response_from_dict = GetMessagingCountersResponse.from_dict(get_messaging_counters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


