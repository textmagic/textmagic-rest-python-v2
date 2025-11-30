# CreateCustomFieldRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Custom field name. | [optional] 

## Example

```python
from TextMagic.models.create_custom_field_request import CreateCustomFieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomFieldRequest from a JSON string
create_custom_field_request_instance = CreateCustomFieldRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCustomFieldRequest.to_json())

# convert the object into a dict
create_custom_field_request_dict = create_custom_field_request_instance.to_dict()
# create an instance of CreateCustomFieldRequest from a dict
create_custom_field_request_from_dict = CreateCustomFieldRequest.from_dict(create_custom_field_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


