# FavoriteContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int** | List or Contact ID. | 
**entity_type** | **str** | Entity type which should be marked as **favorite**. | 
**primary_label** | **str** | Contact first name/last name if entityType is **contact**; List name if entity type is **list**. | 
**secondary_label** | **str** | Phone number if entityType is **contact**; List contacts number if entity type is **list**. | 
**tertiary_label** | **str** | Contact country if entityType is **contact**; else, null. | 
**avatar** | **str** |  | 

## Example

```python
from TextMagic.models.favorite_contact import FavoriteContact

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteContact from a JSON string
favorite_contact_instance = FavoriteContact.from_json(json)
# print the JSON string representation of the object
print(FavoriteContact.to_json())

# convert the object into a dict
favorite_contact_dict = favorite_contact_instance.to_dict()
# create an instance of FavoriteContact from a dict
favorite_contact_from_dict = FavoriteContact.from_dict(favorite_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


