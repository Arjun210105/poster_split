import tkinter as tk
from tkinter import filedialog
from services.image_service import ImageService
from services.poster_service import PosterService
from services.tile_service import TileService
from services.pdf_service import PDFService
from tkinter import messagebox
import os

class MainWindow:

    def __init__(self, root):
        self.root = root
        self.image_path = None
        self.configure_window()
        self.create_widgets()
        self.layout_widgets()

    def configure_window(self):
        self.root.title("Poster Generator")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

    def create_widgets(self):
        self.title_label = tk.Label(self.root,text="Poster Generator",font=("Arial", 18, "bold"))
        self.image_label = tk.Label(self.root,text="Image")
        self.choose_button = tk.Button(self.root,text="Choose Image",command=self.choose_image)
        self.selected_file_label = tk.Label(self.root,text="No image selected")
        self.width_label = tk.Label(self.root,text="Width (cm)")
        self.width_entry = tk.Entry(self.root)
        self.height_label = tk.Label(self.root,text="Height (cm)")
        self.height_entry = tk.Entry(self.root)
        self.generate_button = tk.Button(self.root,text="Generate PDF",command=self.generate_pdf)

    def layout_widgets(self):
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)
        self.image_label.grid(row=1, column=0, sticky="w", padx=10)
        self.choose_button.grid(row=1, column=1, pady=5)
        self.selected_file_label.grid(row=2, column=0, columnspan=2)
        self.width_label.grid(row=3, column=0, sticky="w", padx=10)
        self.width_entry.grid(row=3, column=1, pady=5)
        self.height_label.grid(row=4, column=0, sticky="w", padx=10)
        self.height_entry.grid(row=4, column=1, pady=5)
        self.generate_button.grid(row=5, column=0, columnspan=2, pady=20)

    def choose_image(self):
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[
                ("Image Files", "*.jpg *.jpeg *.png *.bmp")
            ]
        )

        if file_path:
            self.image_path = file_path
            filename = os.path.basename(file_path)
            self.selected_file_label.config(text=filename)  

    def generate_pdf(self):

        if self.image_path is None:
            messagebox.showerror("Error","Please choose an image.")
            return

        width_text = self.width_entry.get()
        height_text = self.height_entry.get()

        if width_text == "" or height_text == "":
            messagebox.showerror("Error","Please enter width and height.")
            return

        try:
            target_width = float(width_text)
            target_height = float(height_text)
        except ValueError:
            messagebox.showerror("Error","Width and Height must be numbers.")
            return

        info = ImageService.get_image_info(self.image_path)
        poster = PosterService.calculate(info["width"],info["height"],target_width,target_height)

        tiles = TileService.calculate_tiles(poster.width_cm,poster.height_cm)
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf",filetypes=[("PDF Files", "*.pdf")],initialfile="poster.pdf")

        if not output_path:
            return
        PDFService.generate(image =info["image"],poster=poster,tile_info=tiles,output_path=output_path)
        


        print("========== IMAGE INFO ==========")
        print(f"Original Width  : {info['width']} px")
        print(f"Original Height : {info['height']} px")
        print(f"Aspect Ratio    : {info['aspect_ratio']:.2f}")

        print("\n========== POSTER ==========")
        print(f"Width (cm)   : {poster.width_cm:.2f}")
        print(f"Height (cm)  : {poster.height_cm:.2f}")
        print(f"Width (px)   : {poster.width_px}")
        print(f"Height (px)  : {poster.height_px}")
        print(f"Scale        : {poster.scale:.4f}")

        print("\n========== TILE INFO ==========")
        print(f"Orientation  : {tiles.orientation}")
        print(f"Rows         : {tiles.rows}")
        print(f"Columns      : {tiles.columns}")
        print(f"Total Pages  : {tiles.total_pages}")
        print(f"Printable W  : {tiles.page_width_cm:.2f} cm")
        print(f"Printable H  : {tiles.page_height_cm:.2f} cm")