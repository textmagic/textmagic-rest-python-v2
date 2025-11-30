# Timezone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal timezone ID. | 
**area** | **str** | Timezone area. | 
**dst** | **int** | Is daylight saving time used in this timezone? | 
**offset** | **int** | Offset from UTC time in seconds. In this example, it is 21600/60/60&#x3D;6 hours. | 
**timezone** | **str** | User-friendly timezone name (with spaces replaced by underscores). | 

## Example

```python
from TextMagic.models.timezone import Timezone

# TODO update the JSON string below
json = "{}"
# create an instance of Timezone from a JSON string
timezone_instance = Timezone.from_json(json)
# print the JSON string representation of the object
print(Timezone.to_json())

# convert the object into a dict
timezone_dict = timezone_instance.to_dict()
# create an instance of Timezone from a dict
timezone_from_dict = Timezone.from_dict(timezone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


