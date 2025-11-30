# MessageTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Template ID. | 
**name** | **str** | Template name. | 
**content** | **str** | Template text. May contain dynamic fields inside braces. See the [Custom fields list](https://docs.textmagic.com/#tag/Templates/Custom-fields-list-(Merge-dynamic-fields)). | 
**last_modified** | **datetime** | Time when the template was last modified. | 

## Example

```python
from TextMagic.models.message_template import MessageTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of MessageTemplate from a JSON string
message_template_instance = MessageTemplate.from_json(json)
# print the JSON string representation of the object
print(MessageTemplate.to_json())

# convert the object into a dict
message_template_dict = message_template_instance.to_dict()
# create an instance of MessageTemplate from a dict
message_template_from_dict = MessageTemplate.from_dict(message_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


