from utils.sentiment_classif_utils import query_sentiment

def analyze_text_mood(text):
    return query_sentiment(text)[0]['label']
