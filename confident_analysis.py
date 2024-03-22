from textblob import TextBlob

def analyze_text_confidence(text):
    """
    Analyze the sentiment of the provided text, returning both the sentiment analysis and a derived confidence score.
    
    The confidence score is a heuristic based on the polarity and subjectivity of the sentiment analysis.
    
    Parameters:
    - text (str): The text to analyze.
    
    Returns:
    - dict: A dictionary containing the sentiment analysis and a derived confidence score.
    """
    # Create a TextBlob object for the given text
    blob = TextBlob(text)
    
    # Analyze the sentiment of the text
    sentiment = blob.sentiment
    
    # Derive a simple confidence score
    # Here, we're considering the absolute value of polarity (for sentiment strength)
    # and adjusting it by the objectivity (1 - subjectivity) for confidence
    confidence = abs(sentiment.polarity) * (1 - sentiment.subjectivity)
    
    # Returning the sentiment analysis results along with the derived confidence score
    return {
        "polarity": sentiment.polarity,
        "subjectivity": sentiment.subjectivity,
        "confidence": confidence
    }

# Example text for analysis
text = "I love this product. It works amazingly well!"
analysis_result = analyze_text_confidence(text)

print(f"Analysis Result: {analysis_result}")
