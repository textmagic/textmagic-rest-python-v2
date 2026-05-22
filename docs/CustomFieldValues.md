# CustomFieldValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **int** |  | [optional] 
**field_title** | **str** |  | [optional] 
**field_type** | **str** |  | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from TextMagic.models.custom_field_values import CustomFieldValues

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldValues from a JSON string
custom_field_values_instance = CustomFieldValues.from_json(json)
# print the JSON string representation of the object
print(CustomFieldValues.to_json())

# convert the object into a dict
custom_field_values_dict = custom_field_values_instance.to_dict()
# create an instance of CustomFieldValues from a dict
custom_field_values_from_dict = CustomFieldValues.from_dict(custom_field_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


