from reportlab.lib.units import cm

# -----------------------
# Image Quality
# -----------------------

DPI = 150

# -----------------------
# A4 Page
# -----------------------

A4_WIDTH_CM = 21
A4_HEIGHT_CM = 29.7

# ReportLab works in points
A4_WIDTH = 21 * cm
A4_HEIGHT = 29.7 * cm

# -----------------------
# Printable Area
# -----------------------

MARGIN_CM = 0.5

PRINTABLE_WIDTH_CM = A4_WIDTH_CM - (2 * MARGIN_CM)
PRINTABLE_HEIGHT_CM = A4_HEIGHT_CM - (2 * MARGIN_CM)

# -----------------------
# Output Folder
# -----------------------

OUTPUT_FOLDER = "output"