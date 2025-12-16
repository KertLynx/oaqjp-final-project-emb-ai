from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    text_to_analyze = request.args.get("textToAnalyze", "")
    if not text_to_analyze.strip():
        return "Invalid text! Please try again!"
    try:
        result = emotion_detector(text_to_analyze)
        if result.get("dominant_emotion") is None:
            return "Invalid text! Please try again!"
        response = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return response
    except Exception as e:
        return "Invalid text! Please try again!"


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
