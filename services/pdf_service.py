from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import cm
#from tkinter import messagebox
import os


class PDFService:

    @staticmethod
    def generate(image, poster, tile_info, output_path):

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Resize image to poster size
        resized_image = image.resize((poster.width_px, poster.height_px))

        # Select PDF page orientation
        if tile_info.orientation == "landscape":
            page_size = landscape(A4)
        else:
            page_size = A4

        pdf = canvas.Canvas(output_path, pagesize=page_size)

        margin = 0.5 * cm

        draw_width = tile_info.page_width_cm * cm
        draw_height = tile_info.page_height_cm * cm

        for row in range(tile_info.rows):
            for col in range(tile_info.columns):

                # Calculate crop boundaries
                left = round(col * poster.width_px / tile_info.columns)
                right = round((col + 1) * poster.width_px / tile_info.columns)

                top = round(row * poster.height_px / tile_info.rows)
                bottom = round((row + 1) * poster.height_px / tile_info.rows)

                tile = resized_image.crop((left, top, right, bottom))

                pdf.drawImage(
                    ImageReader(tile),
                    margin,
                    margin,
                    width=draw_width,
                    height=draw_height
                )

                # Don't create a blank page after the last tile
                if not (
                    row == tile_info.rows - 1 and
                    col == tile_info.columns - 1
                ):
                    pdf.showPage()

        pdf.save()

        print("PDF Created Successfully!")
        print(output_path)
        print(os.path.exists(output_path))
        os.startfile(output_path)