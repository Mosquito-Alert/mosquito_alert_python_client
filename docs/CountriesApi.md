# mosquito_alert_api.CountriesApi

All URIs are relative to *https://api.mosquitoalert.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countries_retrieve**](CountriesApi.md#countries_retrieve) | **GET** /api/v1/countries/{id}/ | 


# **countries_retrieve**
> Country countries_retrieve(id)



### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert_api
from mosquito_alert_api.models.country import Country
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
    api_instance = mosquito_alert_api.CountriesApi(api_client)
    id = 56 # int | A unique integer value identifying this europe country.

    try:
        api_response = api_instance.countries_retrieve(id)
        print("The response of CountriesApi->countries_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountriesApi->countries_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this europe country. | 

### Return type

[**Country**](Country.md)

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
