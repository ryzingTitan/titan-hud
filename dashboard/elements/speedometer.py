import pygame

from dashboard.configuration.colors import CYAN, MAGENTA
from dashboard.configuration.screen_settings import (
    COLUMN_WIDTH,
    CONTENT_Y,
    SPEED_HEIGHT,
)

_BORDER_WIDTH = 2
_LABEL = "Speed"
_COLUMN_INDEX = 1


def draw_speedometer(
    surface: pygame.Surface,
    font_label: pygame.font.Font,
    font_value: pygame.font.Font,
    speed_mph: float,
) -> None:
    x = COLUMN_WIDTH * _COLUMN_INDEX
    rect = pygame.Rect(x, CONTENT_Y, COLUMN_WIDTH, SPEED_HEIGHT)

    pygame.draw.rect(surface, pygame.Color(MAGENTA), rect, _BORDER_WIDTH)

    label_surf = font_label.render(_LABEL, True, pygame.Color(MAGENTA))
    label_x = rect.centerx - label_surf.get_width() // 2
    label_y = rect.top + _BORDER_WIDTH + 4
    surface.blit(label_surf, (label_x, label_y))

    value_surf = font_value.render(str(round(speed_mph)), True, pygame.Color(CYAN))
    unit_surf = font_label.render("MPH", True, pygame.Color(CYAN))
    value_area_top = label_y + label_surf.get_height() + 4
    value_area_h = rect.bottom - _BORDER_WIDTH - value_area_top
    gap = 6
    combined_w = value_surf.get_width() + gap + unit_surf.get_width()
    value_x = rect.centerx - combined_w // 2
    value_y = value_area_top + (value_area_h - value_surf.get_height()) // 2
    unit_x = value_x + value_surf.get_width() + gap
    unit_y = value_y + (value_surf.get_height() - unit_surf.get_height()) // 2
    surface.blit(value_surf, (value_x, value_y))
    surface.blit(unit_surf, (unit_x, unit_y))
