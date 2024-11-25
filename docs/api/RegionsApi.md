# RegionsApi

All URIs are relative to *https://s3.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**regions_find_by_region**](RegionsApi.md#regions_find_by_region) | **GET** /regions/{region} | Retrieve Region |
| [**regions_get**](RegionsApi.md#regions_get) | **GET** /regions | Retrieve all Regions |


# **regions_find_by_region**
> RegionRead regions_find_by_region(region)

Retrieve Region

Returns the Region by Region.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **region** | **str**| The Region of the Region. |  |

### Return type

[**RegionRead**](../models/RegionRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **regions_get**
> RegionReadList regions_get(offset=offset, limit=limit)

Retrieve all Regions

This endpoint enables retrieving all Regions using pagination and optional filters. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100] |

### Return type

[**RegionReadList**](../models/RegionReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

