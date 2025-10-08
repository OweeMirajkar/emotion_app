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
        emotions = result["emotion"]["document"]["emotion"]

    return render_template("index.html", emotions=emotions, text=text)

if __name__ == "__main__":
    app.run(debug=True)
