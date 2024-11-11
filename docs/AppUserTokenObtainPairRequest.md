# AppUserTokenObtainPairRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from mosquito_alert_api.models.app_user_token_obtain_pair_request import AppUserTokenObtainPairRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserTokenObtainPairRequest from a JSON string
app_user_token_obtain_pair_request_instance = AppUserTokenObtainPairRequest.from_json(json)
# print the JSON string representation of the object
print(AppUserTokenObtainPairRequest.to_json())

# convert the object into a dict
app_user_token_obtain_pair_request_dict = app_user_token_obtain_pair_request_instance.to_dict()
# create an instance of AppUserTokenObtainPairRequest from a dict
app_user_token_obtain_pair_request_from_dict = AppUserTokenObtainPairRequest.from_dict(app_user_token_obtain_pair_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

