# FileMetadataPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** |  | 
**width** | **int** |  | 

## Example

```python
from TextMagic.models.file_metadata_preview import FileMetadataPreview

# TODO update the JSON string below
json = "{}"
# create an instance of FileMetadataPreview from a JSON string
file_metadata_preview_instance = FileMetadataPreview.from_json(json)
# print the JSON string representation of the object
print(FileMetadataPreview.to_json())

# convert the object into a dict
file_metadata_preview_dict = file_metadata_preview_instance.to_dict()
# create an instance of FileMetadataPreview from a dict
file_metadata_preview_from_dict = FileMetadataPreview.from_dict(file_metadata_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


