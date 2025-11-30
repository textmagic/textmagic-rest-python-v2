# EmailCampaignStatisticTotals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | **int** | Total number of recipients. | 
**delivered** | **int** | Number of emails delivered. | 
**rejected** | **int** | Number of emails rejected. | 
**failed** | **int** | Number of emails failed to send. | 
**opened** | **int** | Number of emails opened. | 
**clicked** | **int** | Number of emails with clicks. | 
**spam_reports** | **int** | Number of spam reports. | 
**unsubscribed** | **int** | Number of unsubscribes. | 

## Example

```python
from TextMagic.models.email_campaign_statistic_totals import EmailCampaignStatisticTotals

# TODO update the JSON string below
json = "{}"
# create an instance of EmailCampaignStatisticTotals from a JSON string
email_campaign_statistic_totals_instance = EmailCampaignStatisticTotals.from_json(json)
# print the JSON string representation of the object
print(EmailCampaignStatisticTotals.to_json())

# convert the object into a dict
email_campaign_statistic_totals_dict = email_campaign_statistic_totals_instance.to_dict()
# create an instance of EmailCampaignStatisticTotals from a dict
email_campaign_statistic_totals_from_dict = EmailCampaignStatisticTotals.from_dict(email_campaign_statistic_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


