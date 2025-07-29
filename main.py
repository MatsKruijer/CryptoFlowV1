from transformers import pipeline
from flask import Flask, request, jsonify

app = Flask(__name__)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

@app.route("/samenvatten", methods=["POST"])
def samenvatten():
    data = request.get_json()
    tekst = data.get("text", "")
    summary = summarizer(tekst, max_length=60, min_length=20, do_sample=False)
    return jsonify(summary)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
