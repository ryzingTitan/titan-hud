import pygame

from dashboard.configuration.colors import CYAN, MAGENTA
from dashboard.configuration.screen_settings import (
    COLUMN_WIDTH,
    FUEL_LEVEL_HEIGHT,
    FUEL_LEVEL_Y,
)

_LABEL = "FUEL"
_COLUMN_INDEX = 3


def draw_fuel_level(
    surface: pygame.Surface,
    font_label: pygame.font.Font,
    font_value: pygame.font.Font,
    fuel_level: float,
) -> None:
    x = COLUMN_WIDTH * _COLUMN_INDEX
    rect = pygame.Rect(x, FUEL_LEVEL_Y, COLUMN_WIDTH, FUEL_LEVEL_HEIGHT)

    label_surf = font_label.render(_LABEL, True, pygame.Color(MAGENTA))
    label_x = rect.centerx - label_surf.get_width() // 2
    label_y = rect.top + 8
    surface.blit(label_surf, (label_x, label_y))

    clamped = max(0.0, min(100.0, fuel_level))
    value_surf = font_value.render(f"{clamped:.0f}%", True, pygame.Color(CYAN))
    value_area_top = label_y + label_surf.get_height() + 4
    value_area_h = rect.bottom - value_area_top
    value_x = rect.centerx - value_surf.get_width() // 2
    value_y = value_area_top + (value_area_h - value_surf.get_height()) // 2
    surface.blit(value_surf, (value_x, value_y))
