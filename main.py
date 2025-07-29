from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Initialiseer een lichte samenvattingspipeline
summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        data = request.get_json()
        text = data.get("text", "")
        if not text:
            return jsonify({"error": "Geen tekst ontvangen"}), 400

        summary = summarizer(text, max_length=100, min_length=20, do_sample=False)[0]["summary_text"]
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def index():
    return "✅ Samenvattings-API is online!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
