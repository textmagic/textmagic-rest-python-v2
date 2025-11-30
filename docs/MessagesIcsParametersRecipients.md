# MessagesIcsParametersRecipients


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | **List[int]** |  | 
**groups** | **List[int]** |  | 
**numbers** | **List[str]** |  | 
**filtered_views** | **List[int]** |  | 

## Example

```python
from TextMagic.models.messages_ics_parameters_recipients import MessagesIcsParametersRecipients

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesIcsParametersRecipients from a JSON string
messages_ics_parameters_recipients_instance = MessagesIcsParametersRecipients.from_json(json)
# print the JSON string representation of the object
print(MessagesIcsParametersRecipients.to_json())

# convert the object into a dict
messages_ics_parameters_recipients_dict = messages_ics_parameters_recipients_instance.to_dict()
# create an instance of MessagesIcsParametersRecipients from a dict
messages_ics_parameters_recipients_from_dict = MessagesIcsParametersRecipients.from_dict(messages_ics_parameters_recipients_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


