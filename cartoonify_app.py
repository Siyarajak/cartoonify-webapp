import streamlit as st
import numpy as np
from PIL import Image
import cv2
from image_processing import cartoonify_image_steps  # Your existing function

st.set_page_config(page_title="Cartoonify Your Image", layout="centered")
st.title("🖼 Cartoonify Your Image")
st.write("Upload an image and see it transformed into a cartoon!")

# Upload Image
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file:
    # Convert uploaded file to numpy array
    image = np.array(Image.open(uploaded_file).convert("RGB"))

    st.subheader("Original Image")
    st.image(image, use_column_width=True)

    # Sliders for adjustments
    blur_ksize = st.slider("Median Blur Kernel (odd numbers only)", 1, 15, 5, step=2)
    bilateral_d = st.slider("Bilateral Filter Diameter", 1, 20, 9)

    if st.button("Cartoonify Image"):
        # Cartoonify steps
        steps = cartoonify_image_steps(image, blur_ksize=blur_ksize, bilateral_d=bilateral_d)

        # Display all 6 steps
        step_titles = ["Original", "Grayscale", "Smooth Gray", "Edges", "Bilateral Filtered Color", "Cartoon Image"]
        st.subheader("Processing Steps")
        for i, step_img in enumerate(steps):
            st.write(f"**Step {i+1}: {step_titles[i]}**")
            st.image(step_img, use_column_width=True)

        # Show final cartoon image separately
        st.subheader("🎨 Final Cartoon Image")
        st.image(steps[-1], use_column_width=True)

        # Download button
        final_image = Image.fromarray(steps[-1])
        final_image.save("cartoon_image.png")
        with open("cartoon_image.png", "rb") as file:
            btn = st.download_button(
                label="Download Cartoon Image",
                data=file,
                file_name="cartoon_image.png",
                mime="image/png"
            )
