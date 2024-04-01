"""
This module implements a Flask application for emotion detection.
"""
#Import Flask, render_template, request from the flask framework package:
from flask import Flask, render_template, request

#Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector as detect_emotion

#Initiate the flask app:
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector():
    """
    This function receives text from the HTML interface and runs emotion detection.
    It returns the dominant emotion detected for the provided text.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = detect_emotion(text_to_analyze)
    if dominant_emotion['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return f"For the given statement the response is {dominant_emotion['dominant_emotion']}."

@app.route("/")
def index():
    """
    This function renders the index.html template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
