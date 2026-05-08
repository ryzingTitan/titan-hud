import pygame

from dashboard.configuration.colors import CYAN, MAGENTA
from dashboard.configuration.screen_settings import AFR_HEIGHT, AFR_Y, COLUMN_WIDTH

_LABEL = "AFR"
_COLUMN_INDEX = 3


def draw_afr(
    surface: pygame.Surface,
    font_label: pygame.font.Font,
    font_value: pygame.font.Font,
    afr: float,
) -> None:
    x = COLUMN_WIDTH * _COLUMN_INDEX
    rect = pygame.Rect(x, AFR_Y, COLUMN_WIDTH, AFR_HEIGHT)

    label_surf = font_label.render(_LABEL, True, pygame.Color(MAGENTA))
    label_x = rect.centerx - label_surf.get_width() // 2
    label_y = rect.top + 8
    surface.blit(label_surf, (label_x, label_y))

    value_surf = font_value.render(f"{afr:.1f}", True, pygame.Color(CYAN))
    unit_surf = font_value.render(":1", True, pygame.Color(CYAN))
    value_area_top = label_y + label_surf.get_height() + 4
    value_area_h = rect.bottom - value_area_top
    gap = 6
    combined_w = value_surf.get_width() + gap + unit_surf.get_width()
    value_x = rect.centerx - combined_w // 2
    value_y = value_area_top + (value_area_h - value_surf.get_height()) // 2
    unit_x = value_x + value_surf.get_width() + gap
    unit_y = value_y + (value_surf.get_height() - unit_surf.get_height()) // 2
    surface.blit(value_surf, (value_x, value_y))
    surface.blit(unit_surf, (unit_x, unit_y))
