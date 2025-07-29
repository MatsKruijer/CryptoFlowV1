from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
summarizer = pipeline("summarization", model="philschmid/bart-mini-xsum-samsum")

@app.route("/", methods=["POST"])
def summarize():
    data = request.get_json()
    if "text" not in data:
        return jsonify({"error": "No 'text' provided"}), 400

    text = data["text"]
    if not text.strip():
        return jsonify({"summary": ""})

    try:
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return jsonify({"summary": summary[0]["summary_text"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)

