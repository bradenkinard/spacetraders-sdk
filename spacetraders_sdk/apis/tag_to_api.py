import typing_extensions

from spacetraders_sdk.apis.tags import TagValues
from spacetraders_sdk.apis.tags.factions_api import FactionsApi
from spacetraders_sdk.apis.tags.fleet_api import FleetApi
from spacetraders_sdk.apis.tags.contracts_api import ContractsApi
from spacetraders_sdk.apis.tags.systems_api import SystemsApi
from spacetraders_sdk.apis.tags.agents_api import AgentsApi
from spacetraders_sdk.apis.tags.default_api import DefaultApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.FACTIONS: FactionsApi,
        TagValues.FLEET: FleetApi,
        TagValues.CONTRACTS: ContractsApi,
        TagValues.SYSTEMS: SystemsApi,
        TagValues.AGENTS: AgentsApi,
        TagValues.DEFAULT: DefaultApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.FACTIONS: FactionsApi,
        TagValues.FLEET: FleetApi,
        TagValues.CONTRACTS: ContractsApi,
        TagValues.SYSTEMS: SystemsApi,
        TagValues.AGENTS: AgentsApi,
        TagValues.DEFAULT: DefaultApi,
    }
)
