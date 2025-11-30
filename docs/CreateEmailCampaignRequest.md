# CreateEmailCampaignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_sender_id** | **int** | Email sender ID from your configured senders. | [optional] 
**subject** | **str** | Email subject line. | [optional] 
**message** | **str** | HTML email content. | [optional] 
**from_name** | **str** | Optional custom sender name. | [optional] 
**reply_to_email** | **str** | Optional custom reply-to email address. | [optional] 
**recipients** | [**CreateEmailCampaignRequestRecipients**](CreateEmailCampaignRequestRecipients.md) |  | [optional] 

## Example

```python
from TextMagic.models.create_email_campaign_request import CreateEmailCampaignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEmailCampaignRequest from a JSON string
create_email_campaign_request_instance = CreateEmailCampaignRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEmailCampaignRequest.to_json())

# convert the object into a dict
create_email_campaign_request_dict = create_email_campaign_request_instance.to_dict()
# create an instance of CreateEmailCampaignRequest from a dict
create_email_campaign_request_from_dict = CreateEmailCampaignRequest.from_dict(create_email_campaign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


