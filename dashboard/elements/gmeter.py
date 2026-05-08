import math

import pygame

from dashboard.configuration.colors import CYAN, MAGENTA
from dashboard.configuration.screen_settings import (
    COLUMN_WIDTH,
    GMETER_HEIGHT,
    GMETER_Y,
)

_COLUMN_INDEX = 0
_MAX_G = 1.5
_RINGS = (0.5, 1.0, 1.5)
_DIM_MAGENTA = (140, 0, 140)


def _dashed_circle(surface: pygame.Surface, color, center, radius: int) -> None:
    cx, cy = center
    step = 10
    arc_deg = 7
    rect = pygame.Rect(cx - radius, cy - radius, radius * 2, radius * 2)
    for start in range(0, 360, step):
        pygame.draw.arc(
            surface,
            color,
            rect,
            math.radians(start),
            math.radians(start + arc_deg),
            1,
        )


def draw_gmeter(
    surface: pygame.Surface,
    font_label: pygame.font.Font,
    lat_g: float,
    lon_g: float,
) -> None:
    x = COLUMN_WIDTH * _COLUMN_INDEX
    rect = pygame.Rect(x, GMETER_Y, COLUMN_WIDTH, GMETER_HEIGHT)
    cx = rect.centerx
    cy = rect.centery

    outer_radius = min(COLUMN_WIDTH, GMETER_HEIGHT) // 2 - 20

    # crosshairs — extend only to the outer ring
    pygame.draw.line(surface, _DIM_MAGENTA, (cx, cy - outer_radius), (cx, cy + outer_radius), 1)
    pygame.draw.line(surface, _DIM_MAGENTA, (cx - outer_radius, cy), (cx + outer_radius, cy), 1)

    # dashed rings and labels
    for g_val in _RINGS:
        r = int(outer_radius * g_val / _MAX_G)
        _dashed_circle(surface, _DIM_MAGENTA, (cx, cy), r)
        label_surf = font_label.render(str(g_val), True, pygame.Color(*_DIM_MAGENTA))
        label_surf = pygame.transform.smoothscale(
            label_surf, (label_surf.get_width() // 2, label_surf.get_height() // 2)
        )
        surface.blit(label_surf, (cx + r + 2, cy - label_surf.get_height() // 2))

    # direction labels
    for text, pos in (
        ("ACCEL", (cx, rect.top + 10)),
        ("BRAKE", (cx, rect.bottom - 20)),
        ("L", (rect.left + 8, cy)),
        ("R", (rect.right - 16, cy)),
    ):
        surf = font_label.render(text, True, pygame.Color(MAGENTA))
        surf = pygame.transform.smoothscale(surf, (surf.get_width() // 2, surf.get_height() // 2))
        surface.blit(surf, (pos[0] - surf.get_width() // 2, pos[1] - surf.get_height() // 2))

    # G dot — clamped to outer ring
    magnitude = math.hypot(lat_g, lon_g)
    if magnitude > _MAX_G:
        scale = _MAX_G / magnitude
        lat_g *= scale
        lon_g *= scale
    dot_x = cx + int(lat_g / _MAX_G * outer_radius)
    dot_y = cy - int(lon_g / _MAX_G * outer_radius)
    pygame.draw.circle(surface, pygame.Color(CYAN), (dot_x, dot_y), 8)
