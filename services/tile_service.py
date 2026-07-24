from dataclasses import dataclass
import math

from utils.constants import (
    A4_WIDTH_CM,
    A4_HEIGHT_CM,
    MARGIN_CM
)


@dataclass
class TileInfo:
    rows: int
    columns: int
    total_pages: int

    page_width_cm: float
    page_height_cm: float
    
    orientation: str


class TileService:

    @staticmethod
    def _calculate(poster_width_cm, poster_height_cm,
                   page_width_cm, page_height_cm):

        printable_width = page_width_cm - (2 * MARGIN_CM)
        printable_height = page_height_cm - (2 * MARGIN_CM)

        columns = math.ceil(poster_width_cm / printable_width)
        rows = math.ceil(poster_height_cm / printable_height)

        return {
            "rows": rows,
            "columns": columns,
            "total_pages": rows * columns,
            "page_width_cm": printable_width,
            "page_height_cm": printable_height
        }

    @staticmethod
    def calculate_tiles(
            poster_width_cm,
            poster_height_cm):

        # Portrait calculation
        portrait = TileService._calculate(
            poster_width_cm,
            poster_height_cm,
            A4_WIDTH_CM,
            A4_HEIGHT_CM
        )

        # Landscape calculation
        landscape = TileService._calculate(
            poster_width_cm,
            poster_height_cm,
            A4_HEIGHT_CM,
            A4_WIDTH_CM
        )

        # Choose the orientation requiring fewer pages
        if portrait["total_pages"] <= landscape["total_pages"]:
            chosen = portrait
            orientation = "portrait"
        else:
            chosen = landscape
            orientation = "landscape"

        return TileInfo(
            rows=chosen["rows"],
            columns=chosen["columns"],
            total_pages=chosen["total_pages"],
            page_width_cm=chosen["page_width_cm"],
            page_height_cm=chosen["page_height_cm"],
            orientation=orientation
        )