import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    
    # Check if the request was successful
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        
        # Extracting emotion predictions
        emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']

        # Extracting individual emotion scores
        anger_score = emotion_predictions['anger']
        disgust_score = emotion_predictions['disgust']
        fear_score = emotion_predictions['fear']
        joy_score = emotion_predictions['joy']
        sadness_score = emotion_predictions['sadness']

        # Determining the dominant emotion
        emotions = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}
        dominant_emotion = max(emotions, key=emotions.get)

        # Constructing the result dictionary
        result = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

        return result
    else:
        # Handle the error condition (e.g., by raising an exception or returning a default value)
        return {'error': f"Error occurred: HTTP status code {response.status_code}"}
