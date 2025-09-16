# OutboundEmailResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Outbound email ID. | 
**send_time** | **datetime** | Email send timestamp. | 
**from_name** | **str** | Sender name. | [optional] 
**from_email** | **str** | Sender email address. | 
**reply_to_email** | **str** | Reply-to email address. | 
**recipient_full_name** | **str** | Recipient&#39;s full name. | [optional] 
**recipient_email** | **str** | Recipient&#39;s email address. | [optional] 
**email_subject** | **str** | Email subject line. | 
**email_content** | **str** | HTML email content. | 
**source** | **str** | Source of the outbound email. | 
**status** | **str** | Current email status. | 
**cost** | **float** | Cost of sending this email. | 
**status_reason** | **str** | Detailed status reason. | [optional] 
**contact_id** | **int** | Associated contact ID. | [optional] 
**initiator_id** | **int** | ID of user who initiated the email. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


