import datetime

import pygame

from dashboard.configuration.colors import CYAN, MAGENTA
from dashboard.configuration.screen_settings import DIVIDER_WIDTH, HEADER_HEIGHT, WIDTH


def __slot_center_x(slot: int, slot_w: int) -> int:
    return slot * slot_w + slot_w // 2


def draw_header(
    surface: pygame.Surface,
    font: pygame.font.Font,
    indicators: list[dict],
) -> None:
    divider_y = HEADER_HEIGHT - DIVIDER_WIDTH
    pygame.draw.line(surface, MAGENTA, (0, divider_y), (WIDTH, divider_y), DIVIDER_WIDTH)

    content_h = HEADER_HEIGHT - DIVIDER_WIDTH
    center_y = content_h // 2

    total_slots = 8
    slot_w = WIDTH // total_slots

    for i, ind in enumerate(indicators):
        icon = ind["icon_active"] if ind["active"] else ind["icon_inactive"]
        ix = __slot_center_x(i, slot_w) - icon.get_width() // 2
        iy = center_y - icon.get_height() // 2
        surface.blit(icon, (ix, iy))

    time_str = datetime.datetime.now().strftime("%-I:%M")
    time_surf = font.render(time_str, True, CYAN)
    surface.blit(
        time_surf,
        (
            __slot_center_x(7, slot_w) - time_surf.get_width() // 2,
            center_y - time_surf.get_height() // 2,
        ),
    )
