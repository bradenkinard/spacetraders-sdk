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


class ShipMount(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A mount is installed on the exterier of a ship.
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
                        "MOUNT_GAS_SIPHON_I": "GAS_SIPHON_I",
                        "MOUNT_GAS_SIPHON_II": "GAS_SIPHON_II",
                        "MOUNT_GAS_SIPHON_III": "GAS_SIPHON_III",
                        "MOUNT_SURVEYOR_I": "SURVEYOR_I",
                        "MOUNT_SURVEYOR_II": "SURVEYOR_II",
                        "MOUNT_SURVEYOR_III": "SURVEYOR_III",
                        "MOUNT_SENSOR_ARRAY_I": "SENSOR_ARRAY_I",
                        "MOUNT_SENSOR_ARRAY_II": "SENSOR_ARRAY_II",
                        "MOUNT_SENSOR_ARRAY_III": "SENSOR_ARRAY_III",
                        "MOUNT_MINING_LASER_I": "MINING_LASER_I",
                        "MOUNT_MINING_LASER_II": "MINING_LASER_II",
                        "MOUNT_MINING_LASER_III": "MINING_LASER_III",
                        "MOUNT_LASER_CANNON_I": "LASER_CANNON_I",
                        "MOUNT_MISSILE_LAUNCHER_I": "MISSILE_LAUNCHER_I",
                        "MOUNT_TURRET_I": "TURRET_I",
                    }
                
                @schemas.classproperty
                def GAS_SIPHON_I(cls):
                    return cls("MOUNT_GAS_SIPHON_I")
                
                @schemas.classproperty
                def GAS_SIPHON_II(cls):
                    return cls("MOUNT_GAS_SIPHON_II")
                
                @schemas.classproperty
                def GAS_SIPHON_III(cls):
                    return cls("MOUNT_GAS_SIPHON_III")
                
                @schemas.classproperty
                def SURVEYOR_I(cls):
                    return cls("MOUNT_SURVEYOR_I")
                
                @schemas.classproperty
                def SURVEYOR_II(cls):
                    return cls("MOUNT_SURVEYOR_II")
                
                @schemas.classproperty
                def SURVEYOR_III(cls):
                    return cls("MOUNT_SURVEYOR_III")
                
                @schemas.classproperty
                def SENSOR_ARRAY_I(cls):
                    return cls("MOUNT_SENSOR_ARRAY_I")
                
                @schemas.classproperty
                def SENSOR_ARRAY_II(cls):
                    return cls("MOUNT_SENSOR_ARRAY_II")
                
                @schemas.classproperty
                def SENSOR_ARRAY_III(cls):
                    return cls("MOUNT_SENSOR_ARRAY_III")
                
                @schemas.classproperty
                def MINING_LASER_I(cls):
                    return cls("MOUNT_MINING_LASER_I")
                
                @schemas.classproperty
                def MINING_LASER_II(cls):
                    return cls("MOUNT_MINING_LASER_II")
                
                @schemas.classproperty
                def MINING_LASER_III(cls):
                    return cls("MOUNT_MINING_LASER_III")
                
                @schemas.classproperty
                def LASER_CANNON_I(cls):
                    return cls("MOUNT_LASER_CANNON_I")
                
                @schemas.classproperty
                def MISSILE_LAUNCHER_I(cls):
                    return cls("MOUNT_MISSILE_LAUNCHER_I")
                
                @schemas.classproperty
                def TURRET_I(cls):
                    return cls("MOUNT_TURRET_I")
            name = schemas.StrSchema
        
            @staticmethod
            def requirements() -> typing.Type['ShipRequirements']:
                return ShipRequirements
            description = schemas.StrSchema
            
            
            class strength(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            
            
            class deposits(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "QUARTZ_SAND": "QUARTZ_SAND",
                                "SILICON_CRYSTALS": "SILICON_CRYSTALS",
                                "PRECIOUS_STONES": "PRECIOUS_STONES",
                                "ICE_WATER": "ICE_WATER",
                                "AMMONIA_ICE": "AMMONIA_ICE",
                                "IRON_ORE": "IRON_ORE",
                                "COPPER_ORE": "COPPER_ORE",
                                "SILVER_ORE": "SILVER_ORE",
                                "ALUMINUM_ORE": "ALUMINUM_ORE",
                                "GOLD_ORE": "GOLD_ORE",
                                "PLATINUM_ORE": "PLATINUM_ORE",
                                "DIAMONDS": "DIAMONDS",
                                "URANITE_ORE": "URANITE_ORE",
                                "MERITIUM_ORE": "MERITIUM_ORE",
                            }
                        
                        @schemas.classproperty
                        def QUARTZ_SAND(cls):
                            return cls("QUARTZ_SAND")
                        
                        @schemas.classproperty
                        def SILICON_CRYSTALS(cls):
                            return cls("SILICON_CRYSTALS")
                        
                        @schemas.classproperty
                        def PRECIOUS_STONES(cls):
                            return cls("PRECIOUS_STONES")
                        
                        @schemas.classproperty
                        def ICE_WATER(cls):
                            return cls("ICE_WATER")
                        
                        @schemas.classproperty
                        def AMMONIA_ICE(cls):
                            return cls("AMMONIA_ICE")
                        
                        @schemas.classproperty
                        def IRON_ORE(cls):
                            return cls("IRON_ORE")
                        
                        @schemas.classproperty
                        def COPPER_ORE(cls):
                            return cls("COPPER_ORE")
                        
                        @schemas.classproperty
                        def SILVER_ORE(cls):
                            return cls("SILVER_ORE")
                        
                        @schemas.classproperty
                        def ALUMINUM_ORE(cls):
                            return cls("ALUMINUM_ORE")
                        
                        @schemas.classproperty
                        def GOLD_ORE(cls):
                            return cls("GOLD_ORE")
                        
                        @schemas.classproperty
                        def PLATINUM_ORE(cls):
                            return cls("PLATINUM_ORE")
                        
                        @schemas.classproperty
                        def DIAMONDS(cls):
                            return cls("DIAMONDS")
                        
                        @schemas.classproperty
                        def URANITE_ORE(cls):
                            return cls("URANITE_ORE")
                        
                        @schemas.classproperty
                        def MERITIUM_ORE(cls):
                            return cls("MERITIUM_ORE")
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'deposits':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "symbol": symbol,
                "name": name,
                "requirements": requirements,
                "description": description,
                "strength": strength,
                "deposits": deposits,
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
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["strength"]) -> MetaOapg.properties.strength: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deposits"]) -> MetaOapg.properties.deposits: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["symbol", "name", "requirements", "description", "strength", "deposits", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requirements"]) -> 'ShipRequirements': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["strength"]) -> typing.Union[MetaOapg.properties.strength, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deposits"]) -> typing.Union[MetaOapg.properties.deposits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["symbol", "name", "requirements", "description", "strength", "deposits", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        requirements: 'ShipRequirements',
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        strength: typing.Union[MetaOapg.properties.strength, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        deposits: typing.Union[MetaOapg.properties.deposits, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ShipMount':
        return super().__new__(
            cls,
            *_args,
            symbol=symbol,
            requirements=requirements,
            name=name,
            description=description,
            strength=strength,
            deposits=deposits,
            _configuration=_configuration,
            **kwargs,
        )

from spacetraders_sdk.model.ship_requirements import ShipRequirements
