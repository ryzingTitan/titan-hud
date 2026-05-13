import pygame

from dashboard.configuration.colors import CYAN, MAGENTA
from dashboard.configuration.screen_settings import (
    COLUMN_WIDTH,
    TRACK_MAP_HEIGHT,
    TRACK_MAP_Y,
)

_COLUMN_INDEX = 0
_PADDING = 16
_DIM_MAGENTA = (140, 0, 140)

_TRACK_POINTS = [
    (0.15, 0.85),
    (0.85, 0.85),
    (0.90, 0.78),
    (0.92, 0.68),
    (0.88, 0.58),
    (0.80, 0.50),
    (0.75, 0.42),
    (0.82, 0.36),
    (0.75, 0.30),
    (0.60, 0.22),
    (0.45, 0.18),
    (0.30, 0.22),
    (0.18, 0.32),
    (0.12, 0.42),
    (0.18, 0.52),
    (0.20, 0.62),
    (0.15, 0.70),
    (0.20, 0.78),
]


def _compute_transform(rect: pygame.Rect):
    xs = [p[0] for p in _TRACK_POINTS]
    ys = [p[1] for p in _TRACK_POINTS]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    draw_w = rect.width - _PADDING * 2
    draw_h = rect.height - _PADDING * 2
    scale = min(draw_w / (max_x - min_x), draw_h / (max_y - min_y))
    offset_x = rect.left + _PADDING + (draw_w - (max_x - min_x) * scale) / 2
    offset_y = rect.top + _PADDING + (draw_h - (max_y - min_y) * scale) / 2
    return min_x, min_y, scale, offset_x, offset_y


def _to_px(norm_x, norm_y, min_x, min_y, scale, offset_x, offset_y):
    return (
        round(offset_x + (norm_x - min_x) * scale),
        round(offset_y + (norm_y - min_y) * scale),
    )


def draw_track_map(
    surface: pygame.Surface,
    font_label: pygame.font.Font,
    track_position: float,
) -> None:
    rect = pygame.Rect(COLUMN_WIDTH * _COLUMN_INDEX, TRACK_MAP_Y, COLUMN_WIDTH, TRACK_MAP_HEIGHT)
    transform = _compute_transform(rect)

    pixel_points = [_to_px(p[0], p[1], *transform) for p in _TRACK_POINTS]
    pygame.draw.lines(surface, pygame.Color(*_DIM_MAGENTA), False, pixel_points + [pixel_points[0]], 2)

    n = len(_TRACK_POINTS)
    t_scaled = track_position * n
    idx = int(t_scaled) % n
    t = t_scaled - int(t_scaled)
    a, b = _TRACK_POINTS[idx], _TRACK_POINTS[(idx + 1) % n]
    norm_x = a[0] + (b[0] - a[0]) * t
    norm_y = a[1] + (b[1] - a[1]) * t
    dot_px = _to_px(norm_x, norm_y, *transform)
    pygame.draw.circle(surface, pygame.Color(CYAN), dot_px, 6)

    label_surf = font_label.render("TRACK", True, pygame.Color(MAGENTA))
    label_surf = pygame.transform.smoothscale(label_surf, (label_surf.get_width() // 2, label_surf.get_height() // 2))
    surface.blit(label_surf, (rect.centerx - label_surf.get_width() // 2, rect.top + 6))
