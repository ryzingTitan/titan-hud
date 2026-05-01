import sys

import pygame
import yaml

from dashboard.configuration.colors import BACKGROUND
from dashboard.configuration.screen_settings import (
    DIVIDER_WIDTH,
    FOOTER_HEIGHT,
    FPS,
    HEIGHT,
    SPACING,
    WIDTH,
)
from dashboard.elements.footer import draw_footer
from dashboard.elements.tachometer import draw_tachometer
from dashboard.helpers.load_icons import load_icons


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    footer_text_height = FOOTER_HEIGHT - DIVIDER_WIDTH - (SPACING * 2)
    icons = load_icons(footer_text_height)
    footer_font = pygame.font.Font("assets/fonts/InterVariable.ttf", footer_text_height)
    rpm_font = pygame.font.Font("assets/fonts/InterVariable.ttf", 18)

    with open("config.yaml") as f:
        config = yaml.safe_load(f)
    rpm_max = config["rpm_max"]
    rpm_redline = config["rpm_redline"]

    fake_rpm = 4500
    tc_active = True

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

        screen.fill(BACKGROUND)
        draw_tachometer(screen, rpm_font, fake_rpm, rpm_max, rpm_redline)

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
