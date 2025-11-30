# CustomFieldListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Custom Field ID. | 
**user_custom_field_id** | **int** | Old property custom Field ID. | 
**name** | **str** | Custom Field name. | 
**value** | **str** | Custom Field value. | 
**created_at** | **datetime** | Custom field creation time. | 

## Example

```python
from TextMagic.models.custom_field_list_item import CustomFieldListItem

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldListItem from a JSON string
custom_field_list_item_instance = CustomFieldListItem.from_json(json)
# print the JSON string representation of the object
print(CustomFieldListItem.to_json())

# convert the object into a dict
custom_field_list_item_dict = custom_field_list_item_instance.to_dict()
# create an instance of CustomFieldListItem from a dict
custom_field_list_item_from_dict = CustomFieldListItem.from_dict(custom_field_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


