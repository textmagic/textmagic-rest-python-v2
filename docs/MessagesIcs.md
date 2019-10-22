# MessagesIcs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Schedule ID. | 
**next_send** | **datetime** | Next send date in [ISO 8601](https://en.wikipedia.org/?title&#x3D;ISO_8601) format.  | 
**rrule** | **str** | [iCal RRULE](http://www.kanzaki.com/docs/ical/rrule.html) string.  | 
**session** | [**MessageSession**](MessageSession.md) |  | 
**last_sent** | **datetime** | Date and time when last message has been sent. | 
**contact_name** | **str** | Aggregated contact information. If the message scheduled to be sent to a single contact, a full name will be returned here. Otherwise, a total amount contacts will be returned. | 
**parameters** | [**MessagesIcsParameters**](MessagesIcsParameters.md) |  | 
**type** | **str** |  | 
**summary** | **str** | A human-readable summary of the sending schedule. | 
**text_parameters** | [**MessagesIcsTextParameters**](MessagesIcsTextParameters.md) |  | 
**first_occurrence** | **datetime** | First occurence date. | 
**last_occurrence** | **datetime** | Last occurence date (could be &#x60;null&#x60; if the schedule is endless). | 
**recipients_count** | **int** | Amount of actual recipients. | 
**timezone** | **str** | User-friendly timezone name (with spaces replaced by underscores). | 
**completed** | **bool** | Indicates that schedling has been completed. | 
**avatar** | **str** | A relative link to the contact avatar. | 
**created_at** | **datetime** | Scheduling creation time. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


