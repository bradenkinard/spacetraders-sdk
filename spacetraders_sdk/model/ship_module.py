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


class ShipModule(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A module can be installed in a ship and provides a set of capabilities such as storage space or quarters for crew. Module installations are permanent.
    """


    class MetaOapg:
        required = {
            "symbol",
            "requirements",
            "name",
        }
        
        class properties:
            
            
            class symbol(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "MODULE_MINERAL_PROCESSOR_I": "MINERAL_PROCESSOR_I",
                        "MODULE_CARGO_HOLD_I": "CARGO_HOLD_I",
                        "MODULE_CREW_QUARTERS_I": "CREW_QUARTERS_I",
                        "MODULE_ENVOY_QUARTERS_I": "ENVOY_QUARTERS_I",
                        "MODULE_PASSENGER_CABIN_I": "PASSENGER_CABIN_I",
                        "MODULE_MICRO_REFINERY_I": "MICRO_REFINERY_I",
                        "MODULE_ORE_REFINERY_I": "ORE_REFINERY_I",
                        "MODULE_FUEL_REFINERY_I": "FUEL_REFINERY_I",
                        "MODULE_SCIENCE_LAB_I": "SCIENCE_LAB_I",
                        "MODULE_JUMP_DRIVE_I": "JUMP_DRIVE_I",
                        "MODULE_JUMP_DRIVE_II": "JUMP_DRIVE_II",
                        "MODULE_JUMP_DRIVE_III": "JUMP_DRIVE_III",
                        "MODULE_WARP_DRIVE_I": "WARP_DRIVE_I",
                        "MODULE_WARP_DRIVE_II": "WARP_DRIVE_II",
                        "MODULE_WARP_DRIVE_III": "WARP_DRIVE_III",
                        "MODULE_SHIELD_GENERATOR_I": "SHIELD_GENERATOR_I",
                        "MODULE_SHIELD_GENERATOR_II": "SHIELD_GENERATOR_II",
                    }
                
                @schemas.classproperty
                def MINERAL_PROCESSOR_I(cls):
                    return cls("MODULE_MINERAL_PROCESSOR_I")
                
                @schemas.classproperty
                def CARGO_HOLD_I(cls):
                    return cls("MODULE_CARGO_HOLD_I")
                
                @schemas.classproperty
                def CREW_QUARTERS_I(cls):
                    return cls("MODULE_CREW_QUARTERS_I")
                
                @schemas.classproperty
                def ENVOY_QUARTERS_I(cls):
                    return cls("MODULE_ENVOY_QUARTERS_I")
                
                @schemas.classproperty
                def PASSENGER_CABIN_I(cls):
                    return cls("MODULE_PASSENGER_CABIN_I")
                
                @schemas.classproperty
                def MICRO_REFINERY_I(cls):
                    return cls("MODULE_MICRO_REFINERY_I")
                
                @schemas.classproperty
                def ORE_REFINERY_I(cls):
                    return cls("MODULE_ORE_REFINERY_I")
                
                @schemas.classproperty
                def FUEL_REFINERY_I(cls):
                    return cls("MODULE_FUEL_REFINERY_I")
                
                @schemas.classproperty
                def SCIENCE_LAB_I(cls):
                    return cls("MODULE_SCIENCE_LAB_I")
                
                @schemas.classproperty
                def JUMP_DRIVE_I(cls):
                    return cls("MODULE_JUMP_DRIVE_I")
                
                @schemas.classproperty
                def JUMP_DRIVE_II(cls):
                    return cls("MODULE_JUMP_DRIVE_II")
                
                @schemas.classproperty
                def JUMP_DRIVE_III(cls):
                    return cls("MODULE_JUMP_DRIVE_III")
                
                @schemas.classproperty
                def WARP_DRIVE_I(cls):
                    return cls("MODULE_WARP_DRIVE_I")
                
                @schemas.classproperty
                def WARP_DRIVE_II(cls):
                    return cls("MODULE_WARP_DRIVE_II")
                
                @schemas.classproperty
                def WARP_DRIVE_III(cls):
                    return cls("MODULE_WARP_DRIVE_III")
                
                @schemas.classproperty
                def SHIELD_GENERATOR_I(cls):
                    return cls("MODULE_SHIELD_GENERATOR_I")
                
                @schemas.classproperty
                def SHIELD_GENERATOR_II(cls):
                    return cls("MODULE_SHIELD_GENERATOR_II")
            name = schemas.StrSchema
        
            @staticmethod
            def requirements() -> typing.Type['ShipRequirements']:
                return ShipRequirements
            
            
            class capacity(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            
            
            class range(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            description = schemas.StrSchema
            __annotations__ = {
                "symbol": symbol,
                "name": name,
                "requirements": requirements,
                "capacity": capacity,
                "range": range,
                "description": description,
            }
    
    symbol: MetaOapg.properties.symbol
    requirements: 'ShipRequirements'
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requirements"]) -> 'ShipRequirements': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["capacity"]) -> MetaOapg.properties.capacity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["range"]) -> MetaOapg.properties.range: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["symbol", "name", "requirements", "capacity", "range", "description", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requirements"]) -> 'ShipRequirements': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["capacity"]) -> typing.Union[MetaOapg.properties.capacity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["range"]) -> typing.Union[MetaOapg.properties.range, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["symbol", "name", "requirements", "capacity", "range", "description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        requirements: 'ShipRequirements',
        name: typing.Union[MetaOapg.properties.name, str, ],
        capacity: typing.Union[MetaOapg.properties.capacity, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        range: typing.Union[MetaOapg.properties.range, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ShipModule':
        return super().__new__(
            cls,
            *_args,
            symbol=symbol,
            requirements=requirements,
            name=name,
            capacity=capacity,
            range=range,
            description=description,
            _configuration=_configuration,
            **kwargs,
        )

from spacetraders_sdk.model.ship_requirements import ShipRequirements