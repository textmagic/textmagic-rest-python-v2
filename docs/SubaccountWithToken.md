# SubaccountWithToken

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Sub-account ID. | 
**username** | **str** | Username. | 
**first_name** | **str** | Account first name. | 
**last_name** | **str** | Account last name. | 
**email** | **str** | Account Email address. | 
**status** | **str** | Current account status: * **A** for Active * **T** for Trial.  | 
**balance** | **float** | Account balance (in account currency). | 
**phone** | **str** | Contact phone number. | 
**company** | **str** | Account company name. | 
**currency** | [**Currency**](Currency.md) |  | 
**country** | [**Country**](Country.md) |  | 
**timezone** | [**Timezone**](Timezone.md) |  | 
**subaccount_type** | **str** | Type of account: *   **A** for Administrator sub-account *   **U** for Regular User  | 
**email_accepted** | **bool** | Does the account have a confirmed Email?. | 
**phone_accepted** | **bool** | Does the account have a confirmed Phone Number?. | 
**avatar** | [**UserImage**](UserImage.md) |  | 
**token** | **str** | Access token of account. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


