import pygame

from dashboard.configuration.colors import CYAN, GREEN, RED, YELLOW
from dashboard.configuration.screen_settings import (
    SHIFT_INDICATOR_HEIGHT,
    TACHOMETER_HEIGHT,
    WIDTH,
)

_NUM_LIGHTS = 8
_HORIZONTAL_PCT = 0.8
_FLASH_INTERVAL_MS = 100

_PAIR_COLORS = [
    pygame.Color(CYAN),
    pygame.Color(GREEN),
    pygame.Color(YELLOW),
    pygame.Color(RED),
]


def _dim(color: pygame.Color) -> pygame.Color:
    return pygame.Color(
        round(color.r * 0.15),
        round(color.g * 0.15),
        round(color.b * 0.15),
    )


def draw_shift_indicator(
    surface: pygame.Surface,
    rpm: float,
    thresholds: list[int],
    time_ms: int,
) -> None:
    pair_active = [rpm >= t for t in thresholds]
    flashing = pair_active[3]
    flash_visible = flashing and (time_ms // _FLASH_INTERVAL_MS) % 2 == 0

    area_w = round(WIDTH * _HORIZONTAL_PCT)
    area_x = (WIDTH - area_w) // 2
    area_y = TACHOMETER_HEIGHT
    slot_w = area_w // _NUM_LIGHTS
    diameter = min(SHIFT_INDICATOR_HEIGHT - 8, slot_w - 16)
    radius = diameter // 2
    center_y = area_y + SHIFT_INDICATOR_HEIGHT // 2

    for i in range(_NUM_LIGHTS):
        pair_idx = min(i, _NUM_LIGHTS - 1 - i)
        active = pair_active[pair_idx]
        cx = area_x + slot_w * i + slot_w // 2

        if flashing:
            color = pygame.Color(RED) if flash_visible else _dim(pygame.Color(RED))
        elif active:
            color = _PAIR_COLORS[pair_idx]
        else:
            color = _dim(_PAIR_COLORS[pair_idx])

        pygame.draw.circle(surface, color, (cx, center_y), radius)
