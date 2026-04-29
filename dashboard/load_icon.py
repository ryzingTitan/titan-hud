import pygame


def load_icon(size: int, asset_path: str) -> tuple[pygame.Surface, pygame.Surface]:
    """
    Load and return two scaled TC icon surfaces: (active, inactive).
    Active version is full color; inactive is dimmed.
    """
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
