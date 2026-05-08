import pygame

from dashboard.configuration.colors import CYAN, MAGENTA
from dashboard.configuration.screen_settings import (
    COLUMN_WIDTH,
    LAP_TIMER_HEIGHT,
    LAP_TIMER_Y,
)

_LABEL = "LAP"
_COLUMN_INDEX = 0


def _format_lap_time(seconds: float) -> str:
    minutes = int(seconds) // 60
    secs = seconds % 60
    return f"{minutes}:{secs:05.2f}"


def draw_lap_timer(
    surface: pygame.Surface,
    font_label: pygame.font.Font,
    font_value: pygame.font.Font,
    lap_number: int,
    lap_time_seconds: float,
) -> None:
    x = COLUMN_WIDTH * _COLUMN_INDEX
    rect = pygame.Rect(x, LAP_TIMER_Y, COLUMN_WIDTH, LAP_TIMER_HEIGHT)

    num_surf = font_value.render(str(lap_number), True, pygame.Color(CYAN))
    num_surf = pygame.transform.smoothscale(num_surf, (num_surf.get_width() // 2, num_surf.get_height() // 2))
    label_surf = font_label.render(_LABEL, True, pygame.Color(MAGENTA))
    time_surf = font_value.render(_format_lap_time(lap_time_seconds), True, pygame.Color(CYAN))

    gap_inline = 6
    gap_rows = 4
    row1_h = max(num_surf.get_height(), label_surf.get_height())
    combined_h = row1_h + gap_rows + time_surf.get_height()
    start_y = rect.top + (rect.height - combined_h) // 2

    row1_w = num_surf.get_width() + gap_inline + label_surf.get_width()
    row1_x = rect.centerx - row1_w // 2
    num_y = start_y + (row1_h - num_surf.get_height()) // 2
    label_y = start_y + (row1_h - label_surf.get_height()) // 2
    time_y = start_y + row1_h + gap_rows

    surface.blit(num_surf, (row1_x, num_y))
    surface.blit(label_surf, (row1_x + num_surf.get_width() + gap_inline, label_y))
    surface.blit(time_surf, (rect.centerx - time_surf.get_width() // 2, time_y))
