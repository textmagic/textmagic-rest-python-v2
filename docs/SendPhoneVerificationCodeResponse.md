# SendPhoneVerificationCodeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verify_id** | **str** | The ID of a verification request. This is required to finish the verification request in the next step. | 
**price** | **float** | An amount of credit which will be deducted from your account balance when this verification is successfully completed. | 

## Example

```python
from TextMagic.models.send_phone_verification_code_response import SendPhoneVerificationCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendPhoneVerificationCodeResponse from a JSON string
send_phone_verification_code_response_instance = SendPhoneVerificationCodeResponse.from_json(json)
# print the JSON string representation of the object
print(SendPhoneVerificationCodeResponse.to_json())

# convert the object into a dict
send_phone_verification_code_response_dict = send_phone_verification_code_response_instance.to_dict()
# create an instance of SendPhoneVerificationCodeResponse from a dict
send_phone_verification_code_response_from_dict = SendPhoneVerificationCodeResponse.from_dict(send_phone_verification_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


