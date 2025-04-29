"""Provides methods to detect emotion from text."""
import requests

def emotion_detector(text_to_analyze):
    """Detects emotion from a given text."""

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1' + \
        '/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }

    r = requests.post(url, json=data, headers=headers, timeout=10)

    if r.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    emotions = r.json()['emotionPredictions'][0]['emotion']
    emotions['dominant_emotion'] = sorted(emotions, key=emotions.get, reverse=True)[0]
    return emotions
