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


class ShipyardShip(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "engine",
            "reactor",
            "name",
            "description",
            "mounts",
            "purchasePrice",
            "modules",
            "frame",
        }
        
        class properties:
            name = schemas.StrSchema
            description = schemas.StrSchema
            purchasePrice = schemas.IntSchema
        
            @staticmethod
            def frame() -> typing.Type['ShipFrame']:
                return ShipFrame
        
            @staticmethod
            def reactor() -> typing.Type['ShipReactor']:
                return ShipReactor
        
            @staticmethod
            def engine() -> typing.Type['ShipEngine']:
                return ShipEngine
            
            
            class modules(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ShipModule']:
                        return ShipModule
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ShipModule'], typing.List['ShipModule']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'modules':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ShipModule':
                    return super().__getitem__(i)
            
            
            class mounts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ShipMount']:
                        return ShipMount
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ShipMount'], typing.List['ShipMount']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mounts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ShipMount':
                    return super().__getitem__(i)
        
            @staticmethod
            def type() -> typing.Type['ShipType']:
                return ShipType
            __annotations__ = {
                "name": name,
                "description": description,
                "purchasePrice": purchasePrice,
                "frame": frame,
                "reactor": reactor,
                "engine": engine,
                "modules": modules,
                "mounts": mounts,
                "type": type,
            }
    
    engine: 'ShipEngine'
    reactor: 'ShipReactor'
    name: MetaOapg.properties.name
    description: MetaOapg.properties.description
    mounts: MetaOapg.properties.mounts
    purchasePrice: MetaOapg.properties.purchasePrice
    modules: MetaOapg.properties.modules
    frame: 'ShipFrame'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purchasePrice"]) -> MetaOapg.properties.purchasePrice: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frame"]) -> 'ShipFrame': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reactor"]) -> 'ShipReactor': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["engine"]) -> 'ShipEngine': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modules"]) -> MetaOapg.properties.modules: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mounts"]) -> MetaOapg.properties.mounts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'ShipType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "description", "purchasePrice", "frame", "reactor", "engine", "modules", "mounts", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purchasePrice"]) -> MetaOapg.properties.purchasePrice: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frame"]) -> 'ShipFrame': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reactor"]) -> 'ShipReactor': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["engine"]) -> 'ShipEngine': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modules"]) -> MetaOapg.properties.modules: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mounts"]) -> MetaOapg.properties.mounts: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union['ShipType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "description", "purchasePrice", "frame", "reactor", "engine", "modules", "mounts", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        engine: 'ShipEngine',
        reactor: 'ShipReactor',
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        mounts: typing.Union[MetaOapg.properties.mounts, list, tuple, ],
        purchasePrice: typing.Union[MetaOapg.properties.purchasePrice, decimal.Decimal, int, ],
        modules: typing.Union[MetaOapg.properties.modules, list, tuple, ],
        frame: 'ShipFrame',
        type: typing.Union['ShipType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ShipyardShip':
        return super().__new__(
            cls,
            *_args,
            engine=engine,
            reactor=reactor,
            name=name,
            description=description,
            mounts=mounts,
            purchasePrice=purchasePrice,
            modules=modules,
            frame=frame,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from spacetraders_sdk.model.ship_engine import ShipEngine
from spacetraders_sdk.model.ship_frame import ShipFrame
from spacetraders_sdk.model.ship_module import ShipModule
from spacetraders_sdk.model.ship_mount import ShipMount
from spacetraders_sdk.model.ship_reactor import ShipReactor
from spacetraders_sdk.model.ship_type import ShipType
