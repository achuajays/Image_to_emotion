# Image to Emotion Classifier


Chat Emotion Analyzer is a powerful tool that allows you to analyze the emotions expressed in text, whether it's from screenshots of chat conversations or any other images containing text such as book excerpts, novel pages, news articles, notices, reports, etc. This application utilizes state-of-the-art Natural Language Understanding (NLU) and Optical Character Recognition (OCR) technologies to extract text from images and classify the emotions conveyed in that text.



## Installation

Before running the application, make sure you have the following dependencies installed:

- [transformers](https://huggingface.co/transformers/)
- [torch](https://pytorch.org/)
- [paddleocr](https://github.com/PaddlePaddle/PaddleOCR)
- [streamlit](https://streamlit.io/)

You can install them using pip:

```bash
pip install transformers torch paddleocr streamlit
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/achuajays/Image_to_emotion.git
```

2. **Navigate to the project directory:**

```bash
cd Image_to_emotion
```


3. **Install requirements.txt**

```bash
pip install requiremnets.txt
```

4. **Run the Streamlit app:**

```bash
streamlit run main.py
```

   This will open a new tab in your web browser with the Streamlit app running. You can then use the file uploader to upload an image and see the emotions expressed in the text within the image.

## Dependencies

- [transformers](https://huggingface.co/transformers/) - A library for Natural Language Understanding (NLU)
- [torch](https://pytorch.org/) - An open-source machine learning framework
- [paddleocr](https://github.com/PaddlePaddle/PaddleOCR) - A deep learning based OCR toolkits
- [streamlit](https://streamlit.io/) - An open-source app framework for Machine Learning and Data Science

## Acknowledgments

- The transformer model used for emotion classification is based on [SamLowe/roberta-base-go_emotions](https://huggingface.co/SamLowe/roberta-base-go_emotions).
