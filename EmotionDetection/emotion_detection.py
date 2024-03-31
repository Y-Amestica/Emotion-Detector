import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyse.strip(): #Check for empty or blank input

    # URL for the Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Define headers for the request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Define input JSON for the request
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
        response = requests.post(url, headers=headers, json=input_json)
        formatted_response = json.loads(response.text)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON and extract emotion scores
            emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
            dominant_emotion = max(emotion_predictions.items(), key=lambda x: x[1])[0]
            
          return {
            'anger': emotion_predictions['anger'],
            'disgust': emotion_predictions['disgust'],
            'fear': emotion_predictions['fear'],
            'joy': emotion_predictions['joy'],
            'sadness': emotion_predictions['sadness']
            'dominant_emotion': dominant_emotion
          }
          else:
            return None