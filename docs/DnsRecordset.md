# DnsRecordset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | [optional] [readonly] 
**name** | **str** | use &#39;@&#39; to reference the zone origin | [optional]  if omitted the server will use the default value of "@"
**ttl** | **float** |  | [optional]  if omitted the server will use the default value of 3600
**record** | [**DnsRecordArray**](DnsRecordArray.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


