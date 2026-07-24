from dataclasses import dataclass

from utils.constants import DPI


@dataclass
class PosterInfo:
    # Final physical poster size
    width_cm: float
    height_cm: float

    # Final image size
    width_px: int
    height_px: int

    # Resize scale
    scale: float


class PosterService:

    @staticmethod
    def calculate(
        original_width_px: int,
        original_height_px: int,
        target_width_cm: float,
        target_height_cm: float,
    ) -> PosterInfo:

        # ----------------------------------------
        # Convert requested size to pixels
        # ----------------------------------------

        target_width_px = (target_width_cm / 2.54) * DPI
        target_height_px = (target_height_cm / 2.54) * DPI

        # ----------------------------------------
        # Preserve aspect ratio
        # ----------------------------------------

        scale_x = target_width_px / original_width_px
        scale_y = target_height_px / original_height_px

        scale = min(scale_x, scale_y)

        # ----------------------------------------
        # Final image size (pixels)
        # ----------------------------------------

        final_width_px = round(original_width_px * scale)
        final_height_px = round(original_height_px * scale)

        # ----------------------------------------
        # Convert back to centimeters
        # (actual printed size)
        # ----------------------------------------

        final_width_cm = final_width_px * 2.54 / DPI
        final_height_cm = final_height_px * 2.54 / DPI

        return PosterInfo(
            width_cm=final_width_cm,
            height_cm=final_height_cm,
            width_px=final_width_px,
            height_px=final_height_px,
            scale=scale
        )