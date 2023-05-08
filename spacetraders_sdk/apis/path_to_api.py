import typing_extensions

from spacetraders_sdk.paths import PathValues
from spacetraders_sdk.apis.paths.register import Register
from spacetraders_sdk.apis.paths.systems import Systems
from spacetraders_sdk.apis.paths.systems_system_symbol import SystemsSystemSymbol
from spacetraders_sdk.apis.paths.systems_system_symbol_waypoints import SystemsSystemSymbolWaypoints
from spacetraders_sdk.apis.paths.systems_system_symbol_waypoints_waypoint_symbol import SystemsSystemSymbolWaypointsWaypointSymbol
from spacetraders_sdk.apis.paths.systems_system_symbol_waypoints_waypoint_symbol_market import SystemsSystemSymbolWaypointsWaypointSymbolMarket
from spacetraders_sdk.apis.paths.systems_system_symbol_waypoints_waypoint_symbol_shipyard import SystemsSystemSymbolWaypointsWaypointSymbolShipyard
from spacetraders_sdk.apis.paths.systems_system_symbol_waypoints_waypoint_symbol_jump_gate import SystemsSystemSymbolWaypointsWaypointSymbolJumpGate
from spacetraders_sdk.apis.paths.factions import Factions
from spacetraders_sdk.apis.paths.factions_faction_symbol import FactionsFactionSymbol
from spacetraders_sdk.apis.paths.my_agent import MyAgent
from spacetraders_sdk.apis.paths.my_contracts import MyContracts
from spacetraders_sdk.apis.paths.my_contracts_contract_id import MyContractsContractId
from spacetraders_sdk.apis.paths.my_contracts_contract_id_accept import MyContractsContractIdAccept
from spacetraders_sdk.apis.paths.my_contracts_contract_id_deliver import MyContractsContractIdDeliver
from spacetraders_sdk.apis.paths.my_contracts_contract_id_fulfill import MyContractsContractIdFulfill
from spacetraders_sdk.apis.paths.my_ships import MyShips
from spacetraders_sdk.apis.paths.my_ships_ship_symbol import MyShipsShipSymbol
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_cargo import MyShipsShipSymbolCargo
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_orbit import MyShipsShipSymbolOrbit
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_refine import MyShipsShipSymbolRefine
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_chart import MyShipsShipSymbolChart
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_cooldown import MyShipsShipSymbolCooldown
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_dock import MyShipsShipSymbolDock
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_survey import MyShipsShipSymbolSurvey
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_extract import MyShipsShipSymbolExtract
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_jettison import MyShipsShipSymbolJettison
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_jump import MyShipsShipSymbolJump
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_navigate import MyShipsShipSymbolNavigate
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_nav import MyShipsShipSymbolNav
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_warp import MyShipsShipSymbolWarp
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_sell import MyShipsShipSymbolSell
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_scan_systems import MyShipsShipSymbolScanSystems
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_scan_waypoints import MyShipsShipSymbolScanWaypoints
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_scan_ships import MyShipsShipSymbolScanShips
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_refuel import MyShipsShipSymbolRefuel
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_purchase import MyShipsShipSymbolPurchase
from spacetraders_sdk.apis.paths.my_ships_ship_symbol_transfer import MyShipsShipSymbolTransfer

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.REGISTER: Register,
        PathValues.SYSTEMS: Systems,
        PathValues.SYSTEMS_SYSTEM_SYMBOL: SystemsSystemSymbol,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS: SystemsSystemSymbolWaypoints,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL: SystemsSystemSymbolWaypointsWaypointSymbol,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL_MARKET: SystemsSystemSymbolWaypointsWaypointSymbolMarket,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL_SHIPYARD: SystemsSystemSymbolWaypointsWaypointSymbolShipyard,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL_JUMPGATE: SystemsSystemSymbolWaypointsWaypointSymbolJumpGate,
        PathValues.FACTIONS: Factions,
        PathValues.FACTIONS_FACTION_SYMBOL: FactionsFactionSymbol,
        PathValues.MY_AGENT: MyAgent,
        PathValues.MY_CONTRACTS: MyContracts,
        PathValues.MY_CONTRACTS_CONTRACT_ID: MyContractsContractId,
        PathValues.MY_CONTRACTS_CONTRACT_ID_ACCEPT: MyContractsContractIdAccept,
        PathValues.MY_CONTRACTS_CONTRACT_ID_DELIVER: MyContractsContractIdDeliver,
        PathValues.MY_CONTRACTS_CONTRACT_ID_FULFILL: MyContractsContractIdFulfill,
        PathValues.MY_SHIPS: MyShips,
        PathValues.MY_SHIPS_SHIP_SYMBOL: MyShipsShipSymbol,
        PathValues.MY_SHIPS_SHIP_SYMBOL_CARGO: MyShipsShipSymbolCargo,
        PathValues.MY_SHIPS_SHIP_SYMBOL_ORBIT: MyShipsShipSymbolOrbit,
        PathValues.MY_SHIPS_SHIP_SYMBOL_REFINE: MyShipsShipSymbolRefine,
        PathValues.MY_SHIPS_SHIP_SYMBOL_CHART: MyShipsShipSymbolChart,
        PathValues.MY_SHIPS_SHIP_SYMBOL_COOLDOWN: MyShipsShipSymbolCooldown,
        PathValues.MY_SHIPS_SHIP_SYMBOL_DOCK: MyShipsShipSymbolDock,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SURVEY: MyShipsShipSymbolSurvey,
        PathValues.MY_SHIPS_SHIP_SYMBOL_EXTRACT: MyShipsShipSymbolExtract,
        PathValues.MY_SHIPS_SHIP_SYMBOL_JETTISON: MyShipsShipSymbolJettison,
        PathValues.MY_SHIPS_SHIP_SYMBOL_JUMP: MyShipsShipSymbolJump,
        PathValues.MY_SHIPS_SHIP_SYMBOL_NAVIGATE: MyShipsShipSymbolNavigate,
        PathValues.MY_SHIPS_SHIP_SYMBOL_NAV: MyShipsShipSymbolNav,
        PathValues.MY_SHIPS_SHIP_SYMBOL_WARP: MyShipsShipSymbolWarp,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SELL: MyShipsShipSymbolSell,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SCAN_SYSTEMS: MyShipsShipSymbolScanSystems,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SCAN_WAYPOINTS: MyShipsShipSymbolScanWaypoints,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SCAN_SHIPS: MyShipsShipSymbolScanShips,
        PathValues.MY_SHIPS_SHIP_SYMBOL_REFUEL: MyShipsShipSymbolRefuel,
        PathValues.MY_SHIPS_SHIP_SYMBOL_PURCHASE: MyShipsShipSymbolPurchase,
        PathValues.MY_SHIPS_SHIP_SYMBOL_TRANSFER: MyShipsShipSymbolTransfer,
    }
)

path_to_api = PathToApi(
    {
        PathValues.REGISTER: Register,
        PathValues.SYSTEMS: Systems,
        PathValues.SYSTEMS_SYSTEM_SYMBOL: SystemsSystemSymbol,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS: SystemsSystemSymbolWaypoints,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL: SystemsSystemSymbolWaypointsWaypointSymbol,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL_MARKET: SystemsSystemSymbolWaypointsWaypointSymbolMarket,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL_SHIPYARD: SystemsSystemSymbolWaypointsWaypointSymbolShipyard,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL_JUMPGATE: SystemsSystemSymbolWaypointsWaypointSymbolJumpGate,
        PathValues.FACTIONS: Factions,
        PathValues.FACTIONS_FACTION_SYMBOL: FactionsFactionSymbol,
        PathValues.MY_AGENT: MyAgent,
        PathValues.MY_CONTRACTS: MyContracts,
        PathValues.MY_CONTRACTS_CONTRACT_ID: MyContractsContractId,
        PathValues.MY_CONTRACTS_CONTRACT_ID_ACCEPT: MyContractsContractIdAccept,
        PathValues.MY_CONTRACTS_CONTRACT_ID_DELIVER: MyContractsContractIdDeliver,
        PathValues.MY_CONTRACTS_CONTRACT_ID_FULFILL: MyContractsContractIdFulfill,
        PathValues.MY_SHIPS: MyShips,
        PathValues.MY_SHIPS_SHIP_SYMBOL: MyShipsShipSymbol,
        PathValues.MY_SHIPS_SHIP_SYMBOL_CARGO: MyShipsShipSymbolCargo,
        PathValues.MY_SHIPS_SHIP_SYMBOL_ORBIT: MyShipsShipSymbolOrbit,
        PathValues.MY_SHIPS_SHIP_SYMBOL_REFINE: MyShipsShipSymbolRefine,
        PathValues.MY_SHIPS_SHIP_SYMBOL_CHART: MyShipsShipSymbolChart,
        PathValues.MY_SHIPS_SHIP_SYMBOL_COOLDOWN: MyShipsShipSymbolCooldown,
        PathValues.MY_SHIPS_SHIP_SYMBOL_DOCK: MyShipsShipSymbolDock,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SURVEY: MyShipsShipSymbolSurvey,
        PathValues.MY_SHIPS_SHIP_SYMBOL_EXTRACT: MyShipsShipSymbolExtract,
        PathValues.MY_SHIPS_SHIP_SYMBOL_JETTISON: MyShipsShipSymbolJettison,
        PathValues.MY_SHIPS_SHIP_SYMBOL_JUMP: MyShipsShipSymbolJump,
        PathValues.MY_SHIPS_SHIP_SYMBOL_NAVIGATE: MyShipsShipSymbolNavigate,
        PathValues.MY_SHIPS_SHIP_SYMBOL_NAV: MyShipsShipSymbolNav,
        PathValues.MY_SHIPS_SHIP_SYMBOL_WARP: MyShipsShipSymbolWarp,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SELL: MyShipsShipSymbolSell,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SCAN_SYSTEMS: MyShipsShipSymbolScanSystems,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SCAN_WAYPOINTS: MyShipsShipSymbolScanWaypoints,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SCAN_SHIPS: MyShipsShipSymbolScanShips,
        PathValues.MY_SHIPS_SHIP_SYMBOL_REFUEL: MyShipsShipSymbolRefuel,
        PathValues.MY_SHIPS_SHIP_SYMBOL_PURCHASE: MyShipsShipSymbolPurchase,
        PathValues.MY_SHIPS_SHIP_SYMBOL_TRANSFER: MyShipsShipSymbolTransfer,
    }
)
