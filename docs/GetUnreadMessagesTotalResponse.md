# GetUnreadMessagesTotalResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Amount of unread messages. | 

## Example

```python
from TextMagic.models.get_unread_messages_total_response import GetUnreadMessagesTotalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUnreadMessagesTotalResponse from a JSON string
get_unread_messages_total_response_instance = GetUnreadMessagesTotalResponse.from_json(json)
# print the JSON string representation of the object
print(GetUnreadMessagesTotalResponse.to_json())

# convert the object into a dict
get_unread_messages_total_response_dict = get_unread_messages_total_response_instance.to_dict()
# create an instance of GetUnreadMessagesTotalResponse from a dict
get_unread_messages_total_response_from_dict = GetUnreadMessagesTotalResponse.from_dict(get_unread_messages_total_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


