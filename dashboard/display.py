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
        font = pygame.font.SysFont("DejaVu Sans", available_text_height)
        draw_header(screen, font, tc_active, tc_icon_active, tc_icon_inactive)

        pygame.display.flip()


if __name__ == "__main__":
    main()
