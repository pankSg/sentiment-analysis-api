from textblob import TextBlob

def analyze_sentiment(text: str) -> str: 
    """
    Analyze the sentiment of the given text using TextBlob.
    
    Args:
        text (str): The input text to analyze.

    Returns:
        str: The sentiment of the text ('positive', 'negative', 'neutral').
    """
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'