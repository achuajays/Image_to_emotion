import streamlit as st
import os
from PIL import Image
import time
from classes import  Processor
from classes import ImageOCR



# Function to save uploaded image to uploads folder
def save_uploaded_image(uploaded_image):
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    file_path = os.path.join("uploads", uploaded_image.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_image.getbuffer())
    return file_path

# Function to display loader
def loading(message="Processing..."):
    loader = st.empty()
    loader.write(message)
    return loader

def main():
    st.title("Image Uploader and Saver")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        with loading():
            # Save uploaded image
            saved_file_path = save_uploaded_image(uploaded_image)
            output = image.extract_text(saved_file_path)
            output = result.classify(output)

            # time.sleep(2)  # Simulate some processing time
            
            # Display the file path of the saved image
            st.success(f"{output[0][0]['label']}")

            # Display the saved image
            # st.image(saved_file_path, use_column_width=True)

if __name__ == "__main__":
    result = Processor()
    image = ImageOCR()
    main()