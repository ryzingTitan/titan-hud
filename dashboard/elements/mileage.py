import pygame

from dashboard.configuration.colors import CYAN, MAGENTA
from dashboard.configuration.screen_settings import (
    COLUMN_WIDTH,
    MILEAGE_HEIGHT,
    MILEAGE_Y,
)

_LABEL = "MILEAGE"
_COLUMN_INDEX = 3


def draw_mileage(
    surface: pygame.Surface,
    font_label: pygame.font.Font,
    font_value: pygame.font.Font,
    mileage: float,
) -> None:
    x = COLUMN_WIDTH * _COLUMN_INDEX
    rect = pygame.Rect(x, MILEAGE_Y, COLUMN_WIDTH, MILEAGE_HEIGHT)

    label_surf = font_label.render(_LABEL, True, pygame.Color(MAGENTA))
    label_x = rect.centerx - label_surf.get_width() // 2
    label_y = rect.top + 8
    surface.blit(label_surf, (label_x, label_y))

    clamped = max(0, min(250000, int(mileage)))
    value_surf = font_value.render(f"{clamped:,}", True, pygame.Color(CYAN))
    value_area_top = label_y + label_surf.get_height() + 4
    value_area_h = rect.bottom - value_area_top
    value_x = rect.centerx - value_surf.get_width() // 2
    value_y = value_area_top + (value_area_h - value_surf.get_height()) // 2
    surface.blit(value_surf, (value_x, value_y))
