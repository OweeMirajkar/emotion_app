import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = "Sgknz8qzZfHzK4bSIQjeEnNJrAFhi0-HbpfSsb44JRsW"
url = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/e3247c63-cd08-4d4e-b926-0ca51514fbcf"

@app.route("/", methods=["GET", "POST"])
def home():
    emotions = None
    text = ""
    if request.method == "POST":
        text = request.form["text"]
        headers = {"Content-Type": "application/json"}
        params = {"features": {"emotion": {}}, "text": text}
        response = requests.post(
            f"{url}/v1/analyze?version=2021-08-01",
            json=params,
            headers=headers,
            auth=("apikey", api_key)
        )
        result = response.json()
        emotions = emotion_predictor(result)
        if "error" in emotions:
            return render_template("index.html", error=emotions["error"], text=text)

    return render_template("index.html", emotions=emotions, text=text)

def emotion_predictor(result_json):
    """
    Takes Watson NLP API response JSON and returns a formatted dictionary
    with emotions capitalized and scores rounded to 2 decimal places.
    """
    emotions = result_json["emotion"]["document"]["emotion"]
    formatted = {emotion.capitalize(): round(score, 2) for emotion, score in emotions.items()}
    return formatted

# sample_result = {
#     "emotion": {"document": {"emotion": {"joy": 0.85, "sadness": 0.05, "anger": 0.03, "fear": 0.02, "disgust": 0.05}}}
# }
# print(emotion_predictor(sample_result))

def emotion_detector(text):
    if not text.strip():
        return {"error": "Input cannot be blank"}

    headers = {"Content-Type": "application/json"}
    params = {"features": {"emotion": {}}, "text": text}
    response = requests.post(
        f"{url}/v1/analyze?version=2021-08-01",
        json=params,
        headers=headers,
        auth=("apikey", api_key)
    )

    if response.status_code != 200:
        return {"error": f"API Error: {response.status_code}"}

    return emotion_predictor(response.json())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
