# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from spacetraders_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from spacetraders_sdk.model.agent import Agent
from spacetraders_sdk.model.chart import Chart
from spacetraders_sdk.model.connected_system import ConnectedSystem
from spacetraders_sdk.model.contract import Contract
from spacetraders_sdk.model.contract_deliver_good import ContractDeliverGood
from spacetraders_sdk.model.contract_payment import ContractPayment
from spacetraders_sdk.model.contract_terms import ContractTerms
from spacetraders_sdk.model.cooldown import Cooldown
from spacetraders_sdk.model.extraction import Extraction
from spacetraders_sdk.model.extraction_yield import ExtractionYield
from spacetraders_sdk.model.faction import Faction
from spacetraders_sdk.model.faction_trait import FactionTrait
from spacetraders_sdk.model.jump_gate import JumpGate
from spacetraders_sdk.model.market import Market
from spacetraders_sdk.model.market_trade_good import MarketTradeGood
from spacetraders_sdk.model.market_transaction import MarketTransaction
from spacetraders_sdk.model.meta import Meta
from spacetraders_sdk.model.scanned_ship import ScannedShip
from spacetraders_sdk.model.scanned_system import ScannedSystem
from spacetraders_sdk.model.scanned_waypoint import ScannedWaypoint
from spacetraders_sdk.model.ship import Ship
from spacetraders_sdk.model.ship_cargo import ShipCargo
from spacetraders_sdk.model.ship_cargo_item import ShipCargoItem
from spacetraders_sdk.model.ship_condition import ShipCondition
from spacetraders_sdk.model.ship_crew import ShipCrew
from spacetraders_sdk.model.ship_engine import ShipEngine
from spacetraders_sdk.model.ship_frame import ShipFrame
from spacetraders_sdk.model.ship_fuel import ShipFuel
from spacetraders_sdk.model.ship_module import ShipModule
from spacetraders_sdk.model.ship_mount import ShipMount
from spacetraders_sdk.model.ship_nav import ShipNav
from spacetraders_sdk.model.ship_nav_flight_mode import ShipNavFlightMode
from spacetraders_sdk.model.ship_nav_route import ShipNavRoute
from spacetraders_sdk.model.ship_nav_route_waypoint import ShipNavRouteWaypoint
from spacetraders_sdk.model.ship_nav_status import ShipNavStatus
from spacetraders_sdk.model.ship_reactor import ShipReactor
from spacetraders_sdk.model.ship_registration import ShipRegistration
from spacetraders_sdk.model.ship_requirements import ShipRequirements
from spacetraders_sdk.model.ship_role import ShipRole
from spacetraders_sdk.model.ship_type import ShipType
from spacetraders_sdk.model.shipyard import Shipyard
from spacetraders_sdk.model.shipyard_ship import ShipyardShip
from spacetraders_sdk.model.shipyard_transaction import ShipyardTransaction
from spacetraders_sdk.model.survey import Survey
from spacetraders_sdk.model.survey_deposit import SurveyDeposit
from spacetraders_sdk.model.system import System
from spacetraders_sdk.model.system_faction import SystemFaction
from spacetraders_sdk.model.system_type import SystemType
from spacetraders_sdk.model.system_waypoint import SystemWaypoint
from spacetraders_sdk.model.trade_good import TradeGood
from spacetraders_sdk.model.trade_symbol import TradeSymbol
from spacetraders_sdk.model.waypoint import Waypoint
from spacetraders_sdk.model.waypoint_faction import WaypointFaction
from spacetraders_sdk.model.waypoint_orbital import WaypointOrbital
from spacetraders_sdk.model.waypoint_trait import WaypointTrait
from spacetraders_sdk.model.waypoint_type import WaypointType
