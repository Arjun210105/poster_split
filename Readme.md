# 🖼️ Poster Generator

Poster Generator is a desktop application built with **Python** and **Tkinter** that converts a single image into a **multi-page printable PDF**. It allows users to create large posters using standard A4 sheets while automatically preserving the original image's aspect ratio.

---

## ✨ Features

- 📁 Select any image from your computer.
- 📏 Enter the desired poster dimensions (in centimeters).
- 🔄 Automatically preserves the image's aspect ratio.
- 📄 Splits the poster into multiple A4-sized pages.
- 🔀 Automatically selects the optimal page orientation (Portrait/Landscape).
- 🖨️ Generates a high-quality printable PDF.
- 💾 Lets users choose where to save the generated PDF.
- ⚡ Clean and easy-to-use graphical interface.

---

## 🖼️ Workflow

```text
Select Image
      │
      ▼
Enter Poster Dimensions
      │
      ▼
Calculate Poster Size
      │
      ▼
Determine Page Layout
      │
      ▼
Split Image into Tiles
      │
      ▼
Generate Multi-page PDF
      │
      ▼
Save PDF
```

---

## 📂 Project Structure

```text
PosterGenerator/
│
├── main.py
│
├── ui/
│   └── main_window.py
│
├── services/
│   ├── image_service.py
│   ├── poster_service.py
│   ├── tile_service.py
│   └── pdf_service.py
│
├── utils/
│   └── constants.py
│
├── assets/
├── output/
├── requirements.txt
└── README.md
```

---

## 🛠️ Built With

- Python 3
- Tkinter
- Pillow (PIL)
- ReportLab

---

# 📋 Prerequisites

Before running the application, make sure you have:

- Python **3.10 or later**
- pip (Python Package Manager)

You can verify your installation using:

```bash
python --version
pip --version
```

---

# 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-github-username>/PosterGenerator.git
```

### 2. Navigate to the Project

```bash
cd PosterGenerator
```

### 3. (Optional) Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Required Packages

Using the requirements file:

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install pillow reportlab
```

### 5. Run the Application

```bash
python main.py
```

---

# 📖 How to Use

1. Launch the application.
2. Click **Select Image**.
3. Choose the image you want to enlarge.
4. Enter the desired poster width and height in centimeters.
5. Click **Generate PDF**.
6. Select the location where the PDF should be saved.
7. Print the generated PDF on A4 sheets and assemble the pages to create your poster.

---

# ⚙️ How It Works

The application performs the following steps:

1. Loads the selected image.
2. Reads the image dimensions.
3. Preserves the aspect ratio while calculating the new poster dimensions.
4. Determines the optimal page orientation.
5. Calculates the required number of rows and columns.
6. Resizes the image according to the target poster dimensions.
7. Splits the image into printable tiles.
8. Generates a multi-page PDF using ReportLab.

---

# 📦 Dependencies

| Package | Purpose |
|----------|---------|
| Pillow | Image loading and processing |
| ReportLab | PDF generation |
| Tkinter | Desktop graphical interface |

---

# 💡 Future Improvements

- Page overlap for easier poster assembly.
- Crop marks for precise trimming.
- Support for A3, Letter, and custom paper sizes.
- Adjustable DPI settings.
- Page numbering.
- Poster preview before generation.
- Custom margins.
- Batch poster generation.

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---



If you found this project useful, consider giving it a ⭐ on GitHub!