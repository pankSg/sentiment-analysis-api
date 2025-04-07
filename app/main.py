from flask import Flask, request, jsonify
from model import analyze_sentiment

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Endpoint to analyze the sentiment of the given text.
    
    Returns:
        JSON response containing the sentiment of the text.
    """
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    sentiment = analyze_sentiment(text)
    
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)