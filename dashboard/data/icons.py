from dataclasses import dataclass

from pygame import Surface


@dataclass
class Icons:
    tc_icon_active: Surface
    tc_icon_inactive: Surface
    fuel_icon_active: Surface
    fuel_icon_inactive: Surface
    coolant_icon_active: Surface
    coolant_icon_inactive: Surface
    oil_icon_active: Surface
    oil_icon_inactive: Surface
    engine_icon_active: Surface
    engine_icon_inactive: Surface
    abs_icon_active: Surface
    abs_icon_inactive: Surface
    battery_icon_active: Surface
    battery_icon_inactive: Surface
