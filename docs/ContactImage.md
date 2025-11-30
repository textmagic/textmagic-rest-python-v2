# ContactImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The URI of a contact avatar. | 

## Example

```python
from TextMagic.models.contact_image import ContactImage

# TODO update the JSON string below
json = "{}"
# create an instance of ContactImage from a JSON string
contact_image_instance = ContactImage.from_json(json)
# print the JSON string representation of the object
print(ContactImage.to_json())

# convert the object into a dict
contact_image_dict = contact_image_instance.to_dict()
# create an instance of ContactImage from a dict
contact_image_from_dict = ContactImage.from_dict(contact_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


