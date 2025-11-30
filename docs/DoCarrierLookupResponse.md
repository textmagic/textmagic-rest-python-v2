# DoCarrierLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **float** | The cost to check that one number is constant – 0.04 in your account currency. | 
**country** | [**Country**](Country.md) |  | [optional] 
**local** | **str** | Phone number in [National format](https://en.wikipedia.org/wiki/National_conventions_for_writing_telephone_numbers). | 
**type** | **str** | Phone number type. | 
**carrier** | **str** | Carrier name. | 
**number164** | **str** | Phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164). | 
**valid** | **bool** | This field shows whether the entered phone number is valid or not. | 

## Example

```python
from TextMagic.models.do_carrier_lookup_response import DoCarrierLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DoCarrierLookupResponse from a JSON string
do_carrier_lookup_response_instance = DoCarrierLookupResponse.from_json(json)
# print the JSON string representation of the object
print(DoCarrierLookupResponse.to_json())

# convert the object into a dict
do_carrier_lookup_response_dict = do_carrier_lookup_response_instance.to_dict()
# create an instance of DoCarrierLookupResponse from a dict
do_carrier_lookup_response_from_dict = DoCarrierLookupResponse.from_dict(do_carrier_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


