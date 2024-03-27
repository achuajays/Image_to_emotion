from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import os

class ImageOCR:
    """
    A class for extracting text from images using PaddleOCR.

    Attributes:
        ocr (PaddleOCR): An instance of PaddleOCR for optical character recognition.
    """

    def __init__(self):
        """
        Initializes the ImageOCR object by creating an instance of PaddleOCR.
        """
        self.ocr = PaddleOCR()

    def extract_text(self, image_path):
        """
        Extracts text from the provided image using PaddleOCR.

        Args:
            image_path (str): The file path to the image.

        Returns:
            str: The extracted text from the image.
                Returns None if an error occurs during the OCR process.
        """
        try:
            result = self.ocr.ocr(image_path)
            extracted_text = ' '.join([word[1][0] for line in result for word in line])
            os.remove(image_path)
            return extracted_text
        except Exception as e:
            print("Error:", e)
            return None