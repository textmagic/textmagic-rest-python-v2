# UpdateSurveyCountryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | The 2-letter ISO country code. | 
**user_inbound_id** | **int** | User inbound phone ID. | 

## Example

```python
from TextMagic.models.update_survey_country_item import UpdateSurveyCountryItem

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSurveyCountryItem from a JSON string
update_survey_country_item_instance = UpdateSurveyCountryItem.from_json(json)
# print the JSON string representation of the object
print(UpdateSurveyCountryItem.to_json())

# convert the object into a dict
update_survey_country_item_dict = update_survey_country_item_instance.to_dict()
# create an instance of UpdateSurveyCountryItem from a dict
update_survey_country_item_from_dict = UpdateSurveyCountryItem.from_dict(update_survey_country_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


