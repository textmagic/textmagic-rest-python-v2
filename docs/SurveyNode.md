# SurveyNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**label** | **str** |  | 
**body** | **str** |  | 
**node_type** | **str** |  | 
**is_end_node** | **bool** |  | 
**send_delay** | **int** |  | 
**start_nodes** | **List[str]** |  | 
**end_nodes** | **List[str]** |  | 

## Example

```python
from TextMagic.models.survey_node import SurveyNode

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyNode from a JSON string
survey_node_instance = SurveyNode.from_json(json)
# print the JSON string representation of the object
print(SurveyNode.to_json())

# convert the object into a dict
survey_node_dict = survey_node_instance.to_dict()
# create an instance of SurveyNode from a dict
survey_node_from_dict = SurveyNode.from_dict(survey_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


