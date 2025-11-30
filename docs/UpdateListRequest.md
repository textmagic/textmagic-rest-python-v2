# UpdateListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | List name. | [optional] 
**shared** | **bool** | Make this list shared or not? | [optional] [default to False]
**favorited** | **bool** | Is list favorited. | [optional] [default to False]
**is_default** | **bool** | Is list default for new contacts (web only). | [optional] [default to False]

## Example

```python
from TextMagic.models.update_list_request import UpdateListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateListRequest from a JSON string
update_list_request_instance = UpdateListRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateListRequest.to_json())

# convert the object into a dict
update_list_request_dict = update_list_request_instance.to_dict()
# create an instance of UpdateListRequest from a dict
update_list_request_from_dict = UpdateListRequest.from_dict(update_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


