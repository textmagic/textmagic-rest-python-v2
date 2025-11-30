# ScheduledEmailCampaignDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique scheduled campaign ID. | 
**status** | **str** | Current scheduled campaign status. | 
**email_sender_id** | **int** | Email sender ID used for this campaign. | [optional] 
**start_at** | **datetime** | Scheduled start timestamp (UTC). | 
**end_at** | **datetime** | End timestamp for recurring campaigns (UTC). | [optional] 
**next_send_at** | **datetime** | Next scheduled send timestamp (UTC). | [optional] 
**created_by** | [**UserPersonalInfo**](UserPersonalInfo.md) |  | 
**created_at** | **datetime** | Campaign creation timestamp. | 
**updated_at** | **datetime** | Last update timestamp. | 
**type** | **str** | Campaign recurrence type. | 
**from_name** | **str** | Sender name displayed in recipient&#39;s inbox. | [optional] 
**from_email** | **str** | Sender email address. | 
**reply_to_email** | **str** | Reply-to email address. | 
**subject** | **str** | Email subject line. | 
**html** | **str** | HTML email content. | 
**recipients_count** | **int** | Number of recipients for this campaign. | 
**sending_timezone** | **str** | Timezone for sending the campaign. | 
**rrule** | **str** | RFC 5545 recurrence rule for recurring campaigns. | [optional] 
**occurrence_summary** | **str** | Human-readable schedule description. | [optional] 

## Example

```python
from TextMagic.models.scheduled_email_campaign_details import ScheduledEmailCampaignDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledEmailCampaignDetails from a JSON string
scheduled_email_campaign_details_instance = ScheduledEmailCampaignDetails.from_json(json)
# print the JSON string representation of the object
print(ScheduledEmailCampaignDetails.to_json())

# convert the object into a dict
scheduled_email_campaign_details_dict = scheduled_email_campaign_details_instance.to_dict()
# create an instance of ScheduledEmailCampaignDetails from a dict
scheduled_email_campaign_details_from_dict = ScheduledEmailCampaignDetails.from_dict(scheduled_email_campaign_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


