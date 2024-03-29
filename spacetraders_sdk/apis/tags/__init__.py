# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from spacetraders_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    FACTIONS = "factions"
    FLEET = "fleet"
    CONTRACTS = "contracts"
    SYSTEMS = "systems"
    AGENTS = "agents"
    DEFAULT = "default"
