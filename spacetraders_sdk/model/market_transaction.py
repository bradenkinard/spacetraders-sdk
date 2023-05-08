# coding: utf-8

"""
    SpaceTraders API

    SpaceTraders is an open-universe game and learning platform that offers a set of HTTP endpoints to control a fleet of ships and explore a multiplayer universe.  The API is documented using [OpenAPI](https://github.com/SpaceTradersAPI/api-docs). You can send your first request right here in your browser to check the status of the game server.  ```json http {   \"method\": \"GET\",   \"url\": \"https://api.spacetraders.io/v2\", } ```  Unlike a traditional game, SpaceTraders does not have a first-party client or app to play the game. Instead, you can use the API to build your own client, write a script to automate your ships, or try an app built by the community.  We have a [Discord channel](https://discord.com/invite/jh6zurdWk5) where you can share your projects, ask questions, and get help from other players.     # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: joel@spacetraders.io
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from spacetraders_sdk import schemas  # noqa: F401


class MarketTransaction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "tradeSymbol",
            "totalPrice",
            "waypointSymbol",
            "shipSymbol",
            "units",
            "type",
            "pricePerUnit",
            "timestamp",
        }
        
        class properties:
            waypointSymbol = schemas.StrSchema
            shipSymbol = schemas.StrSchema
            tradeSymbol = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PURCHASE": "PURCHASE",
                        "SELL": "SELL",
                    }
                
                @schemas.classproperty
                def PURCHASE(cls):
                    return cls("PURCHASE")
                
                @schemas.classproperty
                def SELL(cls):
                    return cls("SELL")
            
            
            class units(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 1
            
            
            class pricePerUnit(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 1
            
            
            class totalPrice(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 1
            timestamp = schemas.DateTimeSchema
            __annotations__ = {
                "waypointSymbol": waypointSymbol,
                "shipSymbol": shipSymbol,
                "tradeSymbol": tradeSymbol,
                "type": type,
                "units": units,
                "pricePerUnit": pricePerUnit,
                "totalPrice": totalPrice,
                "timestamp": timestamp,
            }
    
    tradeSymbol: MetaOapg.properties.tradeSymbol
    totalPrice: MetaOapg.properties.totalPrice
    waypointSymbol: MetaOapg.properties.waypointSymbol
    shipSymbol: MetaOapg.properties.shipSymbol
    units: MetaOapg.properties.units
    type: MetaOapg.properties.type
    pricePerUnit: MetaOapg.properties.pricePerUnit
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["waypointSymbol"]) -> MetaOapg.properties.waypointSymbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipSymbol"]) -> MetaOapg.properties.shipSymbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tradeSymbol"]) -> MetaOapg.properties.tradeSymbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["units"]) -> MetaOapg.properties.units: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pricePerUnit"]) -> MetaOapg.properties.pricePerUnit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalPrice"]) -> MetaOapg.properties.totalPrice: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["waypointSymbol", "shipSymbol", "tradeSymbol", "type", "units", "pricePerUnit", "totalPrice", "timestamp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["waypointSymbol"]) -> MetaOapg.properties.waypointSymbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipSymbol"]) -> MetaOapg.properties.shipSymbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tradeSymbol"]) -> MetaOapg.properties.tradeSymbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["units"]) -> MetaOapg.properties.units: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pricePerUnit"]) -> MetaOapg.properties.pricePerUnit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalPrice"]) -> MetaOapg.properties.totalPrice: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["waypointSymbol", "shipSymbol", "tradeSymbol", "type", "units", "pricePerUnit", "totalPrice", "timestamp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        tradeSymbol: typing.Union[MetaOapg.properties.tradeSymbol, str, ],
        totalPrice: typing.Union[MetaOapg.properties.totalPrice, decimal.Decimal, int, ],
        waypointSymbol: typing.Union[MetaOapg.properties.waypointSymbol, str, ],
        shipSymbol: typing.Union[MetaOapg.properties.shipSymbol, str, ],
        units: typing.Union[MetaOapg.properties.units, decimal.Decimal, int, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        pricePerUnit: typing.Union[MetaOapg.properties.pricePerUnit, decimal.Decimal, int, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MarketTransaction':
        return super().__new__(
            cls,
            *_args,
            tradeSymbol=tradeSymbol,
            totalPrice=totalPrice,
            waypointSymbol=waypointSymbol,
            shipSymbol=shipSymbol,
            units=units,
            type=type,
            pricePerUnit=pricePerUnit,
            timestamp=timestamp,
            _configuration=_configuration,
            **kwargs,
        )
