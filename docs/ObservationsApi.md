# mosquito_alert_api.ObservationsApi

All URIs are relative to *https://api.mosquitoalert.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**observations_create**](ObservationsApi.md#observations_create) | **POST** /api/v1/observations/ | 
[**observations_destroy**](ObservationsApi.md#observations_destroy) | **DELETE** /api/v1/observations/{uuid}/ | 
[**observations_list**](ObservationsApi.md#observations_list) | **GET** /api/v1/observations/ | 
[**observations_prediction_create**](ObservationsApi.md#observations_prediction_create) | **POST** /api/v1/observations/{uuid}/prediction/ | 
[**observations_prediction_destroy**](ObservationsApi.md#observations_prediction_destroy) | **DELETE** /api/v1/observations/{uuid}/prediction/ | 
[**observations_prediction_retrieve**](ObservationsApi.md#observations_prediction_retrieve) | **GET** /api/v1/observations/{uuid}/prediction/ | 
[**observations_retrieve**](ObservationsApi.md#observations_retrieve) | **GET** /api/v1/observations/{uuid}/ | 


# **observations_create**
> Observation observations_create(observation_request)



### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert_api
from mosquito_alert_api.models.observation import Observation
from mosquito_alert_api.models.observation_request import ObservationRequest
from mosquito_alert_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mosquitoalert.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mosquito_alert_api.Configuration(
    host = "https://api.mosquitoalert.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = mosquito_alert_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mosquito_alert_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert_api.ObservationsApi(api_client)
    observation_request = mosquito_alert_api.ObservationRequest() # ObservationRequest | 

    try:
        api_response = api_instance.observations_create(observation_request)
        print("The response of ObservationsApi->observations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservationsApi->observations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_request** | [**ObservationRequest**](ObservationRequest.md)|  | 

### Return type

[**Observation**](Observation.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **observations_destroy**
> observations_destroy(uuid)



### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert_api
from mosquito_alert_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mosquitoalert.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mosquito_alert_api.Configuration(
    host = "https://api.mosquitoalert.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = mosquito_alert_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mosquito_alert_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert_api.ObservationsApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_instance.observations_destroy(uuid)
    except Exception as e:
        print("Exception when calling ObservationsApi->observations_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **observations_list**
> PaginatedObservationList observations_list(created_at_after=created_at_after, created_at_before=created_at_before, has_photos=has_photos, has_prediction=has_prediction, has_predictions_all_photos=has_predictions_all_photos, location_country_id=location_country_id, location_nuts_2=location_nuts_2, location_nuts_3=location_nuts_3, order_by=order_by, page=page, page_size=page_size, received_at_after=received_at_after, received_at_before=received_at_before, short_id=short_id, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)



### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert_api
from mosquito_alert_api.models.paginated_observation_list import PaginatedObservationList
from mosquito_alert_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mosquitoalert.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mosquito_alert_api.Configuration(
    host = "https://api.mosquitoalert.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = mosquito_alert_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mosquito_alert_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert_api.ObservationsApi(api_client)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    has_photos = True # bool | Has any photo (optional)
    has_prediction = True # bool | Filter observations that have an associated prediction. An observation is considered to have a prediction if a photo has been selected as reference to use the prediction from. (optional)
    has_predictions_all_photos = True # bool | Filters observations based on whether all associated photos have predictions. Set to True to include observations where every photo has a prediction; set to False to include observations where at least one photo is missing a prediction. (optional)
    location_country_id = 56 # int |  (optional)
    location_nuts_2 = 'location_nuts_2_example' # str |  (optional)
    location_nuts_3 = 'location_nuts_3_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] | Ordenamiento   (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    received_at_after = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    received_at_before = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    short_id = 'short_id_example' # str | Short ID (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    user_uuid = 'user_uuid_example' # str |  (optional)

    try:
        api_response = api_instance.observations_list(created_at_after=created_at_after, created_at_before=created_at_before, has_photos=has_photos, has_prediction=has_prediction, has_predictions_all_photos=has_predictions_all_photos, location_country_id=location_country_id, location_nuts_2=location_nuts_2, location_nuts_3=location_nuts_3, order_by=order_by, page=page, page_size=page_size, received_at_after=received_at_after, received_at_before=received_at_before, short_id=short_id, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)
        print("The response of ObservationsApi->observations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservationsApi->observations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_at_after** | **datetime**| Created at | [optional] 
 **created_at_before** | **datetime**| Created at | [optional] 
 **has_photos** | **bool**| Has any photo | [optional] 
 **has_prediction** | **bool**| Filter observations that have an associated prediction. An observation is considered to have a prediction if a photo has been selected as reference to use the prediction from. | [optional] 
 **has_predictions_all_photos** | **bool**| Filters observations based on whether all associated photos have predictions. Set to True to include observations where every photo has a prediction; set to False to include observations where at least one photo is missing a prediction. | [optional] 
 **location_country_id** | **int**|  | [optional] 
 **location_nuts_2** | **str**|  | [optional] 
 **location_nuts_3** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenamiento   | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **received_at_after** | **datetime**| Received at | [optional] 
 **received_at_before** | **datetime**| Received at | [optional] 
 **short_id** | **str**| Short ID | [optional] 
 **updated_at_after** | **datetime**| Update at | [optional] 
 **updated_at_before** | **datetime**| Update at | [optional] 
 **user_uuid** | **str**|  | [optional] 

### Return type

[**PaginatedObservationList**](PaginatedObservationList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **observations_prediction_create**
> ObservationPrediction observations_prediction_create(uuid, observation_prediction_request)



### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import mosquito_alert_api
from mosquito_alert_api.models.observation_prediction import ObservationPrediction
from mosquito_alert_api.models.observation_prediction_request import ObservationPredictionRequest
from mosquito_alert_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mosquitoalert.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mosquito_alert_api.Configuration(
    host = "https://api.mosquitoalert.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mosquito_alert_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert_api.ObservationsApi(api_client)
    uuid = 'uuid_example' # str | 
    observation_prediction_request = mosquito_alert_api.ObservationPredictionRequest() # ObservationPredictionRequest | 

    try:
        api_response = api_instance.observations_prediction_create(uuid, observation_prediction_request)
        print("The response of ObservationsApi->observations_prediction_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservationsApi->observations_prediction_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **observation_prediction_request** | [**ObservationPredictionRequest**](ObservationPredictionRequest.md)|  | 

### Return type

[**ObservationPrediction**](ObservationPrediction.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **observations_prediction_destroy**
> observations_prediction_destroy(uuid)



### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import mosquito_alert_api
from mosquito_alert_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mosquitoalert.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mosquito_alert_api.Configuration(
    host = "https://api.mosquitoalert.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mosquito_alert_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert_api.ObservationsApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_instance.observations_prediction_destroy(uuid)
    except Exception as e:
        print("Exception when calling ObservationsApi->observations_prediction_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **observations_prediction_retrieve**
> ObservationPrediction observations_prediction_retrieve(uuid)



### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import mosquito_alert_api
from mosquito_alert_api.models.observation_prediction import ObservationPrediction
from mosquito_alert_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mosquitoalert.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mosquito_alert_api.Configuration(
    host = "https://api.mosquitoalert.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mosquito_alert_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert_api.ObservationsApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_response = api_instance.observations_prediction_retrieve(uuid)
        print("The response of ObservationsApi->observations_prediction_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservationsApi->observations_prediction_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ObservationPrediction**](ObservationPrediction.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **observations_retrieve**
> Observation observations_retrieve(uuid)



### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert_api
from mosquito_alert_api.models.observation import Observation
from mosquito_alert_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mosquitoalert.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mosquito_alert_api.Configuration(
    host = "https://api.mosquitoalert.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = mosquito_alert_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mosquito_alert_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert_api.ObservationsApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_response = api_instance.observations_retrieve(uuid)
        print("The response of ObservationsApi->observations_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservationsApi->observations_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**Observation**](Observation.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
