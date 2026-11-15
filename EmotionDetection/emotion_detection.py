import json
import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_object = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=input_object, headers=header, timeout=5).json()
    emo_dict = response["emotionPredictions"][0]["emotion"]

    dom_emo = max(emo_dict, key=emo_dict.get)

    emo_dict["dominant_emotion"] = dom_emo

    return emo_dict
