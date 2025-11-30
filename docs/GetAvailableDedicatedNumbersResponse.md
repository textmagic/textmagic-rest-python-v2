# GetAvailableDedicatedNumbersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numbers** | **List[str]** | Array of phone numbers. | 
**price** | **float** | Dedicated number monthly fee for this country. Returned in the current [account](https://docs.textmagic.com/#tag/User) currency. | 
**gift_type** | **str** |  | 

## Example

```python
from TextMagic.models.get_available_dedicated_numbers_response import GetAvailableDedicatedNumbersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAvailableDedicatedNumbersResponse from a JSON string
get_available_dedicated_numbers_response_instance = GetAvailableDedicatedNumbersResponse.from_json(json)
# print the JSON string representation of the object
print(GetAvailableDedicatedNumbersResponse.to_json())

# convert the object into a dict
get_available_dedicated_numbers_response_dict = get_available_dedicated_numbers_response_instance.to_dict()
# create an instance of GetAvailableDedicatedNumbersResponse from a dict
get_available_dedicated_numbers_response_from_dict = GetAvailableDedicatedNumbersResponse.from_dict(get_available_dedicated_numbers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


