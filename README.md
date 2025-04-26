# Color Palette Generator

## Overview

The Color Palette Generator is a Flask-based web application that allows users to upload images and extract a color palette consisting of the dominant colors present in the image. The application uses the KMeans clustering algorithm from scikit-learn to identify these colors and presents them in an interactive, user-friendly interface.

## Features

* **Image Upload:** Supports drag-and-drop or file selection for PNG, JPG, and JPEG images.
* **Dominant Color Extraction:** Extracts up to 5 dominant colors from the uploaded image using KMeans clustering.
* **Interactive UI:** Displays the color palette with hex codes, which can be copied to the clipboard with a click.
* **Responsive Design:** Optimized for desktop and mobile devices with a clean, modern interface.
* **Preview:** Shows a preview of the uploaded image before generating the palette.

## Technologies Used

* **Backend:** Python, Flask, PIL (Pillow), NumPy, scikit-learn
* **Frontend:** HTML, CSS, JavaScript
* **Styling:** Custom CSS with Font Awesome icons
* **External Libraries:** Hosted via CDNs (Font Awesome)

## Installation

1.  **Clone the Repository:**

    ```bash
    git clone <repository-url>
    cd color-palette-generator
    ```

2.  **Set Up a Virtual Environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Directory Structure

Ensure the following structure is in place:

color-palette-generator/  
├── static/   
│   └── style.css  
├── templates/  
│   └── index.html  
├── uploads/  
├── app.py  
└── README.md  

## Run the Application

```bash
python app.py
```

The app will run on http://127.0.0.1:5000 by default.

## Usage
* Open the application in a web browser.
* Drag and drop an image (PNG, JPG, or JPEG) into the upload area or click to browse.
* Once an image is selected, the "Generate Palette" button becomes activated. 
* Click "Generate Palette" to process the image and display the dominant colors.
* Click on any color circle to copy its hex code to the clipboard.
