from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()

HUGGING_FACE_API_TOKEN = os.getenv('HUGGING_FACE_API_TOKEN')

classifier = pipeline("text-classification", model="nateraw/bert-base-uncased-emotion")

def query_sentiment(mood):
    return classifier(mood)