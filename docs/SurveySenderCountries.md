# SurveySenderCountries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**country_name** | **str** |  | 
**from_number** | **str** |  | 
**allow_dedicated** | **bool** | Is allowed to use a dedicated number? | 

## Example

```python
from TextMagic.models.survey_sender_countries import SurveySenderCountries

# TODO update the JSON string below
json = "{}"
# create an instance of SurveySenderCountries from a JSON string
survey_sender_countries_instance = SurveySenderCountries.from_json(json)
# print the JSON string representation of the object
print(SurveySenderCountries.to_json())

# convert the object into a dict
survey_sender_countries_dict = survey_sender_countries_instance.to_dict()
# create an instance of SurveySenderCountries from a dict
survey_sender_countries_from_dict = SurveySenderCountries.from_dict(survey_sender_countries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


