# BulkSession

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Bulk Session ID. | 
**status** | **str** | * **n** - bulk session is just created * **w** - work in progress * **f** - failed * **c** - completed with success * **s** - suspended  | 
**items_processed** | **int** | Amount of messages which is already processed. | 
**items_total** | **int** | Total amount of messages to be processed. | 
**created_at** | **datetime** | Creation date and time of a Bulk Session. | 
**session** | [**MessageSession**](MessageSession.md) |  | 
**text** | **str** | Message text of a Bulk Session. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


