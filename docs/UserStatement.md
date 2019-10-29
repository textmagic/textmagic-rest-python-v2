# UserStatement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User statement ID. | 
**user_id** | **int** | User ID. | 
**_date** | **datetime** | User statement date. | 
**balance** | **float** |  | 
**delta** | **float** | Balance change amount. | 
**type** | **str** | Type of statement (what you have been charged for): *   **sms** - for sending SMS *   **number** - for renewing a dedicated number; *   **schedule** - for scheduling text messages; *   **topup** - for adding credits to your account.  | 
**value** | **str** | Value differs by **type**: *   for **sms**, it is the sent messages amount; *   for **number**, it is a dedicated phone number; *   for **schedule**, it is a scheduled messages amount; *   for **top-up**, it is an invoice ID.  | 
**comment** | **str** | Optional comment. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


