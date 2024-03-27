import streamlit as st
import os
from PIL import Image
import time
from classes import Processor
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
    st.title("Image To Emotion")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    # Sidebar information about the app
    st.sidebar.title("About")
    st.sidebar.info(
        "This is a Streamlit application that allows users to upload an image containing text. " 
        "The application extracts the text from the image using Optical Character Recognition (OCR) and " 
        "then classifies the emotions expressed in the text using a pre-trained transformer model."
    )
    st.sidebar.markdown(
        "**Usage:**\n"
        "1. Upload an image containing text (e.g., screenshot of a chat conversation, book excerpt).\n"
        "2. The application will extract the text and classify the emotions expressed in the text.\n"
        "3. The detected emotion will be displayed."
    )

    if uploaded_image is not None:
        with loading():
            try:
                # Save uploaded image
                saved_file_path = save_uploaded_image(uploaded_image)
                output = image.extract_text(saved_file_path)
                output = result.classify(output)

                # Display the detected emotion
                st.success(f"Detected emotion: {output[0][0]['label']}")
            except Exception as e:
                print(e)
                st.error('Invalid Image')

if __name__ == "__main__":
    result = Processor()
    image = ImageOCR()
    main()