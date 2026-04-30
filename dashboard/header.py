import datetime

import pygame

from dashboard.colors import BG, BORDER, GREY
from dashboard.screen_settings import DIVIDER_WIDTH, HEADER_HEIGHT


def slot_center_x(slot: int, slot_w: int) -> int:
    return slot * slot_w + slot_w // 2


def draw_header(
    surface: pygame.Surface,
    font: pygame.font.Font,
    indicators: list[dict],
) -> None:
    w = surface.get_width()

    pygame.draw.rect(surface, BG, pygame.Rect(0, 0, w, HEADER_HEIGHT))

    divider_y = HEADER_HEIGHT - DIVIDER_WIDTH
    pygame.draw.rect(surface, BORDER, pygame.Rect(0, divider_y, w, DIVIDER_WIDTH))

    content_h = HEADER_HEIGHT - DIVIDER_WIDTH
    center_y = content_h // 2

    total_slots = 8
    slot_w = w // total_slots

    for i, ind in enumerate(indicators):
        icon = ind["icon_active"] if ind["active"] else ind["icon_inactive"]
        ix = slot_center_x(i, slot_w) - icon.get_width() // 2
        iy = center_y - icon.get_height() // 2
        surface.blit(icon, (ix, iy))

    time_str = datetime.datetime.now().strftime("%-I:%M")
    time_surf = font.render(time_str, True, GREY)
    surface.blit(
        time_surf,
        (
            slot_center_x(7, slot_w) - time_surf.get_width() // 2,
            center_y - time_surf.get_height() // 2,
        ),
    )
