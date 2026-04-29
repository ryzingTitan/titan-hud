import pygame

from dashboard.colors import BG, BORDER
from dashboard.screen_settings import DIVIDER_WIDTH, HEADER_HEIGHT, SPACING

PANEL = (16, 20, 30)


def draw_header(
    surface: pygame.Surface,
    font: pygame.font.Font,
    tc_active: bool,
    tc_icon_active: pygame.Surface,
    tc_icon_inactive: pygame.Surface,
) -> None:
    w = surface.get_width()

    pygame.draw.rect(surface, BG, pygame.Rect(0, 0, w, HEADER_HEIGHT))

    divider_y = HEADER_HEIGHT - DIVIDER_WIDTH
    pygame.draw.rect(surface, BORDER, pygame.Rect(0, divider_y, w, DIVIDER_WIDTH))

    content_h = HEADER_HEIGHT - DIVIDER_WIDTH
    center_y = content_h // 2

    icon = tc_icon_active if tc_active else tc_icon_inactive
    icon_margin = SPACING * 2
    icon_x = icon_margin
    icon_y = center_y - icon.get_height() // 2
    surface.blit(icon, (icon_x, icon_y))
