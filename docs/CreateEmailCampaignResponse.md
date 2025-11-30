# CreateEmailCampaignResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique campaign ID. | 
**status** | **str** | Current campaign status. | 
**email_sender_id** | **int** | Email sender ID used for this campaign. | [optional] 
**start_at** | **datetime** | Campaign start timestamp. | 
**created_by** | [**UserPersonalInfo**](UserPersonalInfo.md) |  | 
**from_name** | **str** | Sender name displayed in recipient&#39;s inbox. | [optional] 
**from_email** | **str** | Sender email address. | 
**reply_to_email** | **str** | Reply-to email address. | 
**subject** | **str** | Email subject line. | 
**html** | **str** | HTML email content. | 
**cost** | **float** | Total campaign cost. | 
**totals** | [**EmailCampaignStatisticTotals**](EmailCampaignStatisticTotals.md) |  | 
**outbound_email** | [**OutboundEmailResponse**](OutboundEmailResponse.md) |  | [optional] 
**failed_reason** | **str** | Reason for campaign failure if applicable. | [optional] 

## Example

```python
from TextMagic.models.create_email_campaign_response import CreateEmailCampaignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEmailCampaignResponse from a JSON string
create_email_campaign_response_instance = CreateEmailCampaignResponse.from_json(json)
# print the JSON string representation of the object
print(CreateEmailCampaignResponse.to_json())

# convert the object into a dict
create_email_campaign_response_dict = create_email_campaign_response_instance.to_dict()
# create an instance of CreateEmailCampaignResponse from a dict
create_email_campaign_response_from_dict = CreateEmailCampaignResponse.from_dict(create_email_campaign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


