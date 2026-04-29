import sys

import pygame

from dashboard.colors import BG
from dashboard.header import draw_header
from dashboard.load_icon import load_icon
from dashboard.screen_settings import DIVIDER_WIDTH, HEADER_HEIGHT, SPACING, H, W


def main():
    pygame.init()
    screen = pygame.display.set_mode((W, H))

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

        screen.fill(BG)

        available_text_height = HEADER_HEIGHT - DIVIDER_WIDTH - (SPACING * 2)
        icon_size = available_text_height
        tc_icon_active, tc_icon_inactive = load_icon(
            icon_size, "assets/traction-control-light.png"
        )
        fuel_icon_active, fuel_icon_inactive = load_icon(
            icon_size, "assets/low-fuel-light.png"
        )
        coolant_icon_active, coolant_icon_inactive = load_icon(
            icon_size, "assets/coolant-temperature-light.png"
        )
        oil_icon_active, oil_icon_inactive = load_icon(
            icon_size, "assets/oil-pressure-light.png"
        )
        engine_icon_active, engine_icon_inactive = load_icon(
            icon_size, "assets/check-engine-light.png"
        )
        abs_icon_active, abs_icon_inactive = load_icon(
            icon_size, "assets/abs-warning-light.png"
        )
        battery_icon_active, battery_icon_inactive = load_icon(
            icon_size, "assets/battery-light.png"
        )
        font = pygame.font.SysFont("DejaVu Sans", available_text_height)

        indicators = [
            {
                "icon_active": tc_icon_active,
                "icon_inactive": tc_icon_inactive,
                "active": tc_active,
            },
            {
                "icon_active": fuel_icon_active,
                "icon_inactive": fuel_icon_inactive,
                "active": True,
            },
            {
                "icon_active": coolant_icon_active,
                "icon_inactive": coolant_icon_inactive,
                "active": True,
            },
            {
                "icon_active": oil_icon_active,
                "icon_inactive": oil_icon_inactive,
                "active": True,
            },
            {
                "icon_active": engine_icon_active,
                "icon_inactive": engine_icon_inactive,
                "active": True,
            },
            {
                "icon_active": abs_icon_active,
                "icon_inactive": abs_icon_inactive,
                "active": True,
            },
            {
                "icon_active": battery_icon_active,
                "icon_inactive": battery_icon_inactive,
                "active": True,
            },
        ]
        draw_header(screen, font, indicators)

        pygame.display.flip()


if __name__ == "__main__":
    main()
