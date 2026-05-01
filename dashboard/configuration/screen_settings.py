def __pct_to_px(percent: float, dimension: int) -> int:
    """Convert a percentage (0–100) to pixels based on a screen dimension."""
    return round((percent / 100) * dimension)


WIDTH = 1280
HEIGHT = 720
FPS = 60
FOOTER_HEIGHT = __pct_to_px(10, HEIGHT)
DIVIDER_WIDTH = 2
SPACING = 4
