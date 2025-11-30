# UserCustomField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Custom field ID. | 
**name** | **str** | Custom field name. | 
**created_at** | **datetime** | Custom field creation time. | 

## Example

```python
from TextMagic.models.user_custom_field import UserCustomField

# TODO update the JSON string below
json = "{}"
# create an instance of UserCustomField from a JSON string
user_custom_field_instance = UserCustomField.from_json(json)
# print the JSON string representation of the object
print(UserCustomField.to_json())

# convert the object into a dict
user_custom_field_dict = user_custom_field_instance.to_dict()
# create an instance of UserCustomField from a dict
user_custom_field_from_dict = UserCustomField.from_dict(user_custom_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


