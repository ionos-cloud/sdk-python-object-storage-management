# AccesskeysApi

All URIs are relative to *https://s3.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**accesskeys_delete**](AccesskeysApi.md#accesskeys_delete) | **DELETE** /accesskeys/{accesskeyId} | Delete AccessKey |
| [**accesskeys_find_by_id**](AccesskeysApi.md#accesskeys_find_by_id) | **GET** /accesskeys/{accesskeyId} | Retrieve AccessKey |
| [**accesskeys_get**](AccesskeysApi.md#accesskeys_get) | **GET** /accesskeys | Retrieve all Accesskeys |
| [**accesskeys_post**](AccesskeysApi.md#accesskeys_post) | **POST** /accesskeys | Create AccessKey |
| [**accesskeys_put**](AccesskeysApi.md#accesskeys_put) | **PUT** /accesskeys/{accesskeyId} | Ensure AccessKey |
| [**accesskeys_renew**](AccesskeysApi.md#accesskeys_renew) | **PUT** /accesskeys/{accesskeyId}/renew | Ensure AccessKey |


# **accesskeys_delete**
> accesskeys_delete(accesskey_id)

Delete AccessKey

Deletes the specified AccessKey.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accesskey_id** | **str**| The ID (UUID) of the AccessKey. |  |

### Return type

void (empty response body)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **accesskeys_find_by_id**
> AccessKeyRead accesskeys_find_by_id(accesskey_id)

Retrieve AccessKey

Returns the AccessKey by ID.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accesskey_id** | **str**| The ID (UUID) of the AccessKey. |  |

### Return type

[**AccessKeyRead**](../models/AccessKeyRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **accesskeys_get**
> AccessKeyReadList accesskeys_get(offset=offset, limit=limit, filter_accesskey_id=filter_accesskey_id)

Retrieve all Accesskeys

This endpoint enables retrieving all Accesskeys using pagination and optional filters. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100] |
| **filter_accesskey_id** | **str**| The accesskey ID to filter by. | [optional]  |

### Return type

[**AccessKeyReadList**](../models/AccessKeyReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **accesskeys_post**
> AccessKeyRead accesskeys_post(access_key_create)

Create AccessKey

Creates a new AccessKey.  The full AccessKey needs to be provided to create the object. Optional data will be filled with defaults or left empty. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **access_key_create** | [**AccessKeyCreate**](../models/AccessKeyCreate.md)| AccessKey to create. |  |

### Return type

[**AccessKeyRead**](../models/AccessKeyRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **accesskeys_put**
> AccessKeyRead accesskeys_put(accesskey_id, access_key_ensure)

Ensure AccessKey

Ensures that the AccessKey with the provided ID is created or modified. The full AccessKey needs to be provided to ensure (either update or create) the AccessKey. Non present data will only be filled with defaults or left empty, but not take previous values into consideration. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accesskey_id** | **str**| The ID (UUID) of the AccessKey. |  |
| **access_key_ensure** | [**AccessKeyEnsure**](../models/AccessKeyEnsure.md)| update AccessKey |  |

### Return type

[**AccessKeyRead**](../models/AccessKeyRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **accesskeys_renew**
> AccessKeyRead accesskeys_renew(accesskey_id)

Ensure AccessKey

Renew will replace the existing secret access key with a new one. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accesskey_id** | **str**| The ID (UUID) of the AccessKey that should be ensured. |  |

### Return type

[**AccessKeyRead**](../models/AccessKeyRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

