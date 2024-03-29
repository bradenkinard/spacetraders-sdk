# spacetraders_sdk.model.contract_deliver_good.ContractDeliverGood

The details of a delivery contract. Includes the type of good, units needed, and the destination.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The details of a delivery contract. Includes the type of good, units needed, and the destination. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**tradeSymbol** | str,  | str,  | The symbol of the trade good to deliver. | 
**unitsRequired** | decimal.Decimal, int,  | decimal.Decimal,  | The number of units that need to be delivered on this contract. | 
**destinationSymbol** | str,  | str,  | The destination where goods need to be delivered. | 
**unitsFulfilled** | decimal.Decimal, int,  | decimal.Decimal,  | The number of units fulfilled on this contract. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

