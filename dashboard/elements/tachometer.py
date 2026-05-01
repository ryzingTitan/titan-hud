import pygame

from dashboard.configuration.colors import BACKGROUND, CYAN, MAGENTA, RED
from dashboard.configuration.screen_settings import TACHOMETER_HEIGHT, WIDTH

_TOP_PAD = 10
_TICK_HEIGHT = 80
_HORIZONTAL_PAD = 20


def draw_tachometer(
    surface: pygame.Surface,
    font: pygame.font.Font,
    rpm: float,
    rpm_max: int,
    rpm_redline: int,
) -> None:
    rpm = max(0.0, min(float(rpm), float(rpm_max)))
    at_redline = rpm >= rpm_redline

    def rpm_to_x(r: float) -> int:
        bar_width = WIDTH - 2 * _HORIZONTAL_PAD
        return round(_HORIZONTAL_PAD + (r / rpm_max) * bar_width)

    bg_color = pygame.Color(RED) if at_redline else pygame.Color(BACKGROUND)
    pygame.draw.rect(surface, bg_color, (0, 0, WIDTH, TACHOMETER_HEIGHT))

    label_y = _TOP_PAD
    font_h = font.get_height()
    tick_top = label_y + font_h
    tick_bot = tick_top + _TICK_HEIGHT

    fill_end_x = rpm_to_x(rpm)
    if fill_end_x > _HORIZONTAL_PAD:
        pygame.draw.rect(
            surface, pygame.Color(MAGENTA), (_HORIZONTAL_PAD, tick_top, fill_end_x - _HORIZONTAL_PAD, _TICK_HEIGHT)
        )

    intervals = rpm_max // 1000
    for i in range(intervals + 1):
        tick_x = rpm_to_x(i * 1000)
        pygame.draw.line(surface, pygame.Color(CYAN), (tick_x, tick_top), (tick_x, tick_bot), 2)
        label_surf = font.render(str(i), True, pygame.Color(CYAN))
        half_w = label_surf.get_width() // 2
        lx = max(half_w, min(tick_x, WIDTH - half_w))
        label_rect = label_surf.get_rect(midtop=(lx, label_y))
        surface.blit(label_surf, label_rect)
