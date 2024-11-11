# UserNotificationCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receiver_type** | **str** |  | 
**title_en** | **str** |  | 
**body_en** | **str** |  | 
**user_uuid** | **str** |  | 

## Example

```python
from mosquito_alert_api.models.user_notification_create_request import UserNotificationCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserNotificationCreateRequest from a JSON string
user_notification_create_request_instance = UserNotificationCreateRequest.from_json(json)
# print the JSON string representation of the object
print(UserNotificationCreateRequest.to_json())

# convert the object into a dict
user_notification_create_request_dict = user_notification_create_request_instance.to_dict()
# create an instance of UserNotificationCreateRequest from a dict
user_notification_create_request_from_dict = UserNotificationCreateRequest.from_dict(user_notification_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

