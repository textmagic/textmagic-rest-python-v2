# GetEmailSendersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EmailSenderItem]**](EmailSenderItem.md) | Array of email sender objects. | 

## Example

```python
from TextMagic.models.get_email_senders_response import GetEmailSendersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmailSendersResponse from a JSON string
get_email_senders_response_instance = GetEmailSendersResponse.from_json(json)
# print the JSON string representation of the object
print(GetEmailSendersResponse.to_json())

# convert the object into a dict
get_email_senders_response_dict = get_email_senders_response_instance.to_dict()
# create an instance of GetEmailSendersResponse from a dict
get_email_senders_response_from_dict = GetEmailSendersResponse.from_dict(get_email_senders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


