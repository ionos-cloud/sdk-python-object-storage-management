# MetadataWithStatus

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **created_date** | **datetime** | The ISO 8601 creation timestamp. | [optional] [readonly]  |
| **created_by** | **str** | Unique name of the identity that created the resource. | [optional] [readonly]  |
| **created_by_user_id** | **str** | Unique id of the identity that created the resource. | [optional] [readonly]  |
| **last_modified_date** | **datetime** | The ISO 8601 modified timestamp. | [optional] [readonly]  |
| **last_modified_by** | **str** | Unique name of the identity that last modified the resource. | [optional] [readonly]  |
| **last_modified_by_user_id** | **str** | Unique id of the identity that last modified the resource. | [optional] [readonly]  |
| **resource_urn** | **str** | Unique name of the resource. | [optional] [readonly]  |
| **status** | **str** | The status of the object. The status can be: * &#x60;AVAILABLE&#x60; - resource exists and is healthy. * &#x60;PROVISIONING&#x60; - resource is being created or updated. * &#x60;DESTROYING&#x60; - delete command was issued, the resource is being deleted. * &#x60;FAILED&#x60; - resource failed, details in &#x60;failureMessage&#x60;.  | [readonly]  |
| **status_message** | **str** | The message of the failure if the status is &#x60;FAILED&#x60;.  | [optional] [readonly]  |
| **administrative** | **bool** | Indicates if the key is an administrative key. Administrative keys can create buckets and set bucket policies.  | [optional] [readonly]  |


