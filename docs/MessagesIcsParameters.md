# MessagesIcsParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Scheduled message text. | 
**recipients** | [**MessagesIcsParametersRecipients**](MessagesIcsParametersRecipients.md) |  | 

## Example

```python
from TextMagic.models.messages_ics_parameters import MessagesIcsParameters

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesIcsParameters from a JSON string
messages_ics_parameters_instance = MessagesIcsParameters.from_json(json)
# print the JSON string representation of the object
print(MessagesIcsParameters.to_json())

# convert the object into a dict
messages_ics_parameters_dict = messages_ics_parameters_instance.to_dict()
# create an instance of MessagesIcsParameters from a dict
messages_ics_parameters_from_dict = MessagesIcsParameters.from_dict(messages_ics_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


