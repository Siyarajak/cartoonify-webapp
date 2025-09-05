# 🎨 Cartoonify Web App

Turn your photos into fun cartoon-style images instantly!


This web app lets users upload an image, apply cartoon effects using OpenCV, and download the result. 
It’s powered by Streamlit for an interactive and user-friendly experience.

## 🌟 Features

Upload any image (JPG, PNG, BMP).

Apply cartoon effect with adjustable settings:
   Median Blur Kernel.
   Bilateral Filter Diameter.
   
Preview the original and cartoonified image side by side.

Download the cartoonified image.

Clean and responsive web interface.


## ⚡ Demo
Check out the live web app: https://cartoonify-webapp-bayjm5a4sf8f53x7xfbekm.streamlit.app/

  
## 🛠 Technology Stack
Python 3.x
Streamlit – Web app framework
OpenCV – Image processing
Pillow – Image handling
NumPy – Nume

## 📦 Installation (for local use)

1.Clone the repository:

    git clone https://github.com/Siyarajak/cartoonify-webapp.git
    cd cartoonify-webapp

2.Create a virtual environment (recommended):

    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows


3.Install dependencies:

    pip install -r requirements.txt


4.Run the app:

    streamlit run cartoonify_app.py


5.Open the URL provided in the terminal (usually http://localhost:8501)rical computing


## 🖼 Usage

1.Click Upload Image to select an image from your computer.

2.Adjust Median Blur Kernel and Bilateral Filter Diameter sliders to tweak the cartoon effect.

3.Click Cartoonify to generate the cartoon image.

4.Click Save Image to download it.


## ⚠️ Notes

Make sure to upload proper image formats (JPG, PNG, BMP).

The app works best with clear, high-resolution images.

For Streamlit deployment, use compatible versions of NumPy (<2.0) and OpenCV to avoid runtime errors.


## 📂 Project Structure
      cartoonify-webapp/
      │
      ├─ cartoonify_app.py      # Main Streamlit app
      ├─ image_processing.py    # Cartoonify logic
      ├─ requirements.txt       # Python dependencies
      ├─ README.md              # Project documentation
      ├─ .gitignore             # Ignore unnecessary files
      └─ images/                # Optional folder for sample images  

## 🔗 Live Demo
https://cartoonify-webapp-bayjm5a4sf8f53x7xfbekm.streamlit.app/

## 💡 Future Improvements

Add more cartoon effects and filters
Support drag-and-drop image upload
Mobile-friendly layout
Real-time camera input

## 📄 License
 Feel free to use and modify this project.

  
