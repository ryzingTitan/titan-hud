import pygame

from dashboard.data.icons import Icons


def __load_icon(size: int, asset_path: str) -> tuple[pygame.Surface, pygame.Surface]:
    original = pygame.image.load(asset_path).convert_alpha()

    # Scale to fit within the icon size (preserve aspect ratio)
    orig_w, orig_h = original.get_size()
    scale = size / max(orig_w, orig_h)
    scaled_w = round(orig_w * scale)
    scaled_h = round(orig_h * scale)
    active_icon = pygame.transform.smoothscale(original, (scaled_w, scaled_h))

    # Inactive: same image but pixels dimmed via per-surface alpha
    inactive_icon = active_icon.copy()
    inactive_icon.set_alpha(60)  # 0=invisible, 255=full — tweak to taste

    return active_icon, inactive_icon


def load_icons(icon_size: int) -> Icons:
    tc_icon_active, tc_icon_inactive = __load_icon(icon_size, "assets/images/traction-control-light.png")
    fuel_icon_active, fuel_icon_inactive = __load_icon(icon_size, "assets/images/low-fuel-light.png")
    coolant_icon_active, coolant_icon_inactive = __load_icon(icon_size, "assets/images/coolant-temperature-light.png")
    oil_icon_active, oil_icon_inactive = __load_icon(icon_size, "assets/images/oil-pressure-light.png")
    engine_icon_active, engine_icon_inactive = __load_icon(icon_size, "assets/images/check-engine-light.png")
    abs_icon_active, abs_icon_inactive = __load_icon(icon_size, "assets/images/abs-warning-light.png")
    battery_icon_active, battery_icon_inactive = __load_icon(icon_size, "assets/images/battery-light.png")

    return Icons(
        tc_icon_active,
        tc_icon_inactive,
        fuel_icon_active,
        fuel_icon_inactive,
        coolant_icon_active,
        coolant_icon_inactive,
        oil_icon_active,
        oil_icon_inactive,
        engine_icon_active,
        engine_icon_inactive,
        abs_icon_active,
        abs_icon_inactive,
        battery_icon_active,
        battery_icon_inactive,
    )
