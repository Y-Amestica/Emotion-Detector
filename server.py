from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector as detect_emotion

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = detect_emotion(text_to_analyze)  # Use detect_emotion instead of emotion_detector
    if dominant_emotion['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    else:
        return "For the given statement, the system response is {}.".format(dominant_emotion['dominant_emotion'])

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
