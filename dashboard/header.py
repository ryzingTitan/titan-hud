import pygame

from dashboard.colors import BG, BORDER
from dashboard.screen_settings import DIVIDER_WIDTH, HEADER_HEIGHT

PANEL = (16, 20, 30)


def draw_header(
    surface: pygame.Surface, font: pygame.font.Font, indicators: list[dict]
) -> None:
    w = surface.get_width()

    pygame.draw.rect(surface, BG, pygame.Rect(0, 0, w, HEADER_HEIGHT))

    divider_y = HEADER_HEIGHT - DIVIDER_WIDTH
    pygame.draw.rect(surface, BORDER, pygame.Rect(0, divider_y, w, DIVIDER_WIDTH))

    content_h = HEADER_HEIGHT - DIVIDER_WIDTH
    center_y = content_h // 2

    total_slots = len(indicators)
    slot_w = w // total_slots

    for i, ind in enumerate(indicators):
        icon = ind["icon_active"] if ind["active"] else ind["icon_inactive"]
        slot_center_x = slot_w * i + slot_w // 2
        icon_x = slot_center_x - icon.get_width() // 2
        icon_y = center_y - icon.get_height() // 2
        surface.blit(icon, (icon_x, icon_y))
