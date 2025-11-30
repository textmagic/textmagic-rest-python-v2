# MessagesIcsTextParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **float** | Cost to check that one number is constant – 0.04 in your account currency. | 
**parts** | **int** | Message parts (multiples of 160 characters) count. | 
**chars** | **int** | Characters count. | 
**encoding** | **str** | Message charset. Could be: * **ISO-8859-1** – for plaintext SMS; * **UTF-16BE** – for Unicode SMS.  | 
**countries** | **List[str]** |  | 
**charset_label** | **str** | Human-readable message charset label. Could be: *   **ISO-8859-1** for plaintext SMS; *   **UTF-16BE** for Unicode SMS; *   **Voice** for voice services (Text-to-Speech or Voice Broadcast) messages.  | 

## Example

```python
from TextMagic.models.messages_ics_text_parameters import MessagesIcsTextParameters

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesIcsTextParameters from a JSON string
messages_ics_text_parameters_instance = MessagesIcsTextParameters.from_json(json)
# print the JSON string representation of the object
print(MessagesIcsTextParameters.to_json())

# convert the object into a dict
messages_ics_text_parameters_dict = messages_ics_text_parameters_instance.to_dict()
# create an instance of MessagesIcsTextParameters from a dict
messages_ics_text_parameters_from_dict = MessagesIcsTextParameters.from_dict(messages_ics_text_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


