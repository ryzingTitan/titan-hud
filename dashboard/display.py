import sys

import pygame
import yaml

from dashboard.configuration.colors import BACKGROUND, CYAN
from dashboard.configuration.screen_settings import (
    COLUMN_WIDTH,
    DIVIDER_WIDTH,
    FOOTER_HEIGHT,
    FPS,
    HEIGHT,
    SPACING,
    WIDTH,
)
from dashboard.elements.afr import draw_afr
from dashboard.elements.boost import draw_boost
from dashboard.elements.coolant_temp import draw_coolant_temp
from dashboard.elements.footer import draw_footer
from dashboard.elements.fuel_level import draw_fuel_level
from dashboard.elements.gmeter import draw_gmeter
from dashboard.elements.intake_air_temp import draw_intake_air_temp
from dashboard.elements.lap_timer import draw_lap_timer
from dashboard.elements.mileage import draw_mileage
from dashboard.elements.oil_pressure import draw_oil_pressure
from dashboard.elements.oil_temp import draw_oil_temp
from dashboard.elements.shift_indicator import draw_shift_indicator
from dashboard.elements.speedometer import draw_speedometer
from dashboard.elements.tachometer import draw_tachometer
from dashboard.elements.track_map import draw_track_map
from dashboard.helpers.load_icons import load_icons

_DIM_MAGENTA = (140, 0, 140)
_COL0_PAGE_COUNT = 3


def _draw_page_dots(surface: pygame.Surface, current_page: int) -> None:
    dot_r = 4
    gap = 10
    total_w = _COL0_PAGE_COUNT * (dot_r * 2) + (_COL0_PAGE_COUNT - 1) * gap
    start_x = (COLUMN_WIDTH - total_w) // 2 + dot_r
    y = HEIGHT - FOOTER_HEIGHT - dot_r - 6
    for i in range(_COL0_PAGE_COUNT):
        color = pygame.Color(CYAN) if i == current_page else pygame.Color(*_DIM_MAGENTA)
        cx = start_x + i * (dot_r * 2 + gap)
        pygame.draw.circle(surface, color, (cx, y), dot_r)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    footer_text_height = FOOTER_HEIGHT - DIVIDER_WIDTH - (SPACING * 2)
    icons = load_icons(footer_text_height)
    footer_font = pygame.font.Font("assets/fonts/InterVariable.ttf", footer_text_height)
    rpm_font = pygame.font.Font("assets/fonts/InterVariable.ttf", 18)
    speed_label_font = pygame.font.Font("assets/fonts/InterVariable.ttf", 20)
    speed_value_font = pygame.font.Font("assets/fonts/InterVariable.ttf", 60)

    with open("config.yaml") as f:
        config = yaml.safe_load(f)
    rpm_max = config["rpm_max"]
    rpm_redline = config["rpm_redline"]
    shift_lights = config["shift_lights"]

    fake_rpm = 4500
    fake_speed = 120.0
    fake_boost = 14.7
    fake_oil_pressure = 45.0
    fake_intake_air_temp = 95.0
    fake_coolant_temp = 190.0
    fake_oil_temp = 200.0
    fake_afr = 14.7
    fake_fuel_level = 75.0
    fake_mileage = 123456
    fake_lap_number = 15
    fake_lap_time_seconds = 83.456
    fake_lap_delta = 0.342
    fake_lateral_g = 0.3
    fake_longitudinal_g = 0.5
    fake_track_position = 0.0
    tc_active = True
    column_0_page = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                tc_active = not tc_active
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                fake_rpm = (fake_rpm + 1000) % (rpm_max + 1000)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                column_0_page = (column_0_page + 1) % _COL0_PAGE_COUNT
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                column_0_page = (column_0_page - 1) % _COL0_PAGE_COUNT

        screen.fill(BACKGROUND)
        fake_track_position = (fake_track_position + 1.0 / (FPS * 10)) % 1.0
        draw_tachometer(screen, rpm_font, fake_rpm, rpm_max, rpm_redline)
        draw_shift_indicator(screen, fake_rpm, shift_lights, pygame.time.get_ticks())

        if column_0_page == 0:
            draw_lap_timer(
                screen, speed_label_font, speed_value_font, fake_lap_number, fake_lap_time_seconds, fake_lap_delta
            )
        elif column_0_page == 1:
            draw_gmeter(screen, speed_label_font, fake_lateral_g, fake_longitudinal_g)
        else:
            draw_track_map(screen, speed_label_font, fake_track_position)
        _draw_page_dots(screen, column_0_page)

        draw_afr(screen, speed_label_font, speed_value_font, fake_afr)
        draw_fuel_level(screen, speed_label_font, speed_value_font, fake_fuel_level)
        draw_mileage(screen, speed_label_font, speed_value_font, fake_mileage)
        draw_speedometer(screen, speed_label_font, speed_value_font, fake_speed)
        draw_boost(screen, speed_label_font, speed_value_font, fake_boost)
        draw_oil_pressure(screen, speed_label_font, speed_value_font, fake_oil_pressure)
        draw_intake_air_temp(screen, speed_label_font, speed_value_font, fake_intake_air_temp)
        draw_coolant_temp(screen, speed_label_font, speed_value_font, fake_coolant_temp)
        draw_oil_temp(screen, speed_label_font, speed_value_font, fake_oil_temp)

        indicators = [
            {
                "icon_active": icons.tc_icon_active,
                "icon_inactive": icons.tc_icon_inactive,
                "active": tc_active,
            },
            {
                "icon_active": icons.fuel_icon_active,
                "icon_inactive": icons.fuel_icon_inactive,
                "active": True,
            },
            {
                "icon_active": icons.coolant_icon_active,
                "icon_inactive": icons.coolant_icon_inactive,
                "active": True,
            },
            {
                "icon_active": icons.oil_icon_active,
                "icon_inactive": icons.oil_icon_inactive,
                "active": True,
            },
            {
                "icon_active": icons.engine_icon_active,
                "icon_inactive": icons.engine_icon_inactive,
                "active": True,
            },
            {
                "icon_active": icons.abs_icon_active,
                "icon_inactive": icons.abs_icon_inactive,
                "active": True,
            },
            {
                "icon_active": icons.battery_icon_active,
                "icon_inactive": icons.battery_icon_inactive,
                "active": True,
            },
        ]
        draw_footer(screen, footer_font, indicators)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
