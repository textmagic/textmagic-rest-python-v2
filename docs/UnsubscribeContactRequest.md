# UnsubscribeContactRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Contact phone number. | [optional] 
**block_incoming** | **int** | If set to 1, incoming messages from this number will be blocked. | [optional] 

## Example

```python
from TextMagic.models.unsubscribe_contact_request import UnsubscribeContactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnsubscribeContactRequest from a JSON string
unsubscribe_contact_request_instance = UnsubscribeContactRequest.from_json(json)
# print the JSON string representation of the object
print(UnsubscribeContactRequest.to_json())

# convert the object into a dict
unsubscribe_contact_request_dict = unsubscribe_contact_request_instance.to_dict()
# create an instance of UnsubscribeContactRequest from a dict
unsubscribe_contact_request_from_dict = UnsubscribeContactRequest.from_dict(unsubscribe_contact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


