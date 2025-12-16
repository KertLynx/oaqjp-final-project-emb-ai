import requests

_URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
_HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
_KEYS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze: str) -> dict:
    resp = requests.post(        _URL, json={"raw_document": {"text": text_to_analyze}}, headers=_HEADERS)
    emotions = (resp.json().get("emotionPredictions") or [{}])[0].get("emotion", {})
    scores = {k: float(emotions.get(k, 0.0)) for k in _KEYS}
    return {**scores, "dominant_emotion": max(scores, key=scores.get)}
