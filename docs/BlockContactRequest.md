# BlockContactRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Contact phone number. | [optional] 

## Example

```python
from TextMagic.models.block_contact_request import BlockContactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlockContactRequest from a JSON string
block_contact_request_instance = BlockContactRequest.from_json(json)
# print the JSON string representation of the object
print(BlockContactRequest.to_json())

# convert the object into a dict
block_contact_request_dict = block_contact_request_instance.to_dict()
# create an instance of BlockContactRequest from a dict
block_contact_request_from_dict = BlockContactRequest.from_dict(block_contact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


