# 🎨 Intelligent Color Palette Generator

An ML-enhanced web application that extracts dominant color palettes from images and videos using:

- **CLIP-based scene classification**  
- **LAB colorspace clustering**  
- **Scene-aware palette refinement rules**  
- **Smart video frame selection**  
- **Fast KMeans clustering**  

This transforms simple palette extraction into a **context-aware intelligent system** that adapts its output based on the visual scene.

---

## Key Features

### 1. CLIP Scene Classification (AI Component)
Uses OpenAI CLIP to classify the uploaded image/video into high-level scene categories such as:

- Indoor / Outdoor  
- Natural / Urban  
- Portrait / Landscape  

These scene labels influence how the palette is generated.

---

### 2. LAB-Based Color Extraction (Professional-Grade)
Instead of basic RGB clustering, the system converts pixel data into **CIELAB**, a perceptually uniform color space used in professional design tools.

This dramatically improves color accuracy and realism.

---

### 3. Scene-Aware Palette Engine
The palette extraction logic adapts based on the scene:

- **Nature scenes:** emphasize greens & blues  
- **Urban scenes:** highlight neutral/metallic tones  
- **Portraits:** preserve skin-tone clusters  
- **Indoor scenes:** avoid oversaturated noise  

This makes the app feel like a truly intelligent color engine.

---

### 🎥 4. Smart Video Frame Selection
Instead of extracting random frames, the system:

1. Reads video frames  
2. Computes histogram differences  
3. Detects scene changes  
4. Selects 5–7 meaningful frames  
5. Extracts the palette from those frames  

This improves both accuracy and performance.

---

### 🖥 5. Modern Frontend UI
- Drag-and-drop upload  
- Video/image preview  
- Color swatches with hex codes  
- Click-to-copy functionality  
- Displays scene labels used for extraction  

---

## 🛠 Tech Stack

### Backend
- Python  
- Flask  
- Pillow (PIL)  
- NumPy  
- OpenCV (cv2)  
- scikit-learn  
- PyTorch  

### Machine Learning
- **OpenAI CLIP (ViT-B/32)**  
- CIELAB color conversion  
- Rule-based scene-aware logic  

### Frontend
- HTML  
- CSS  
- JavaScript  

--- 

## Run the Application

```bash
python app.py
```

The app will run on http://127.0.0.1:5000 by default.

## 📌 Usage

1. Open the application in your browser at **http://127.0.0.1:5000**
2. Drag and drop an **image** (PNG/JPG/JPEG) or **video** (MP4/MOV/AVI/MKV) into the upload area  
   — or click the box to browse files from your system.
3. The application will:
   - Classify the scene using CLIP  
   - For videos: intelligently select key frames using histogram difference  
   - Convert the image/video frames into LAB color space  
   - Cluster colors using KMeans  
   - Apply scene-aware palette refinement rules
4. The final dominant color palette will appear as **colored swatches**.
5. Click any swatch to **copy its HEX code** to your clipboard.
6. The detected **scene labels** will also be displayed alongside the palette.
