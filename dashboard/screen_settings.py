def pct_to_px(percent: float, dimension: int) -> int:
    """Convert a percentage (0–100) to pixels based on a screen dimension."""
    return round((percent / 100) * dimension)


W, H = 1280, 720
FPS = 60
HEADER_HEIGHT = pct_to_px(6, H)
DIVIDER_WIDTH = 2
SPACING = 4
