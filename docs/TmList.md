# TmList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | List ID. | 
**name** | **str** | List name. | 
**description** | **str** | Description of the list. | 
**favorited** | **bool** | Is the List favorited? See [Favorites list](https://docs.textmagic.com/#operation/getFavourites). | 
**members_count** | **int** | List members count. | 
**user** | [**User**](User.md) |  | 
**service** | **bool** | Internal service field. | 
**shared** | **bool** | Is the list **shared** among all sub-accounts? | 
**avatar** | [**ListImage**](ListImage.md) |  | 
**is_default** | **bool** | Indicates that List is used as a default. All new contacts added via the Web-app will be added in this List by default. | 

## Example

```python
from TextMagic.models.tm_list import TmList

# TODO update the JSON string below
json = "{}"
# create an instance of TmList from a JSON string
tm_list_instance = TmList.from_json(json)
# print the JSON string representation of the object
print(TmList.to_json())

# convert the object into a dict
tm_list_dict = tm_list_instance.to_dict()
# create an instance of TmList from a dict
tm_list_from_dict = TmList.from_dict(tm_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


