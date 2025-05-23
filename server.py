"""Emotion detector web server."""
from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """Renders the home page."""
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    """Analyzes the provided text to identify emotions."""
    text_to_analyze = request.args.get('textToAnalyze', '')
    result = emotion_detector(text_to_analyze)
    dominant_emotion = result['dominant_emotion']

    if dominant_emotion is None:
        return 'Invalid text! Please try again!'

    emotions = [f"'{k}': {v}"  for k,v in result.items() if k != 'dominant_emotion']
    return f'For the given statement, the system response is {", ".join(emotions)}. ' + \
        f'The dominant emotion is {dominant_emotion}'

app.run()
