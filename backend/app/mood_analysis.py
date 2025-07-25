from textblob import TextBlob

def analyze_text_mood(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.5:
        return "Happy"
    elif polarity > 0.1:
        return "Calm"
    elif polarity < -0.3:
        return "Sad"
    else:
        return "Focus"
