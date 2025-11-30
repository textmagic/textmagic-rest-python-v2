# CreateListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | List name. | [optional] 
**shared** | **bool** | Should the new list be **shared** among all the sub-accounts? | [optional] [default to False]
**favorited** | **bool** | Is the list favorited? Default is false. | [optional] [default to False]
**is_default** | **bool** | Is the list default for new contacts (web only)? | [optional] [default to False]

## Example

```python
from TextMagic.models.create_list_request import CreateListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateListRequest from a JSON string
create_list_request_instance = CreateListRequest.from_json(json)
# print the JSON string representation of the object
print(CreateListRequest.to_json())

# convert the object into a dict
create_list_request_dict = create_list_request_instance.to_dict()
# create an instance of CreateListRequest from a dict
create_list_request_from_dict = CreateListRequest.from_dict(create_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


