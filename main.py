from flask import Flask, request, jsonify
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

app = Flask(__name__)
summarizer = LsaSummarizer()

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    parser = PlaintextParser.from_string(text, Tokenizer("dutch"))
    summary_sentences = summarizer(parser.document, 3)  # 3 zinnen samenvatting

    summary = " ".join(str(sentence) for sentence in summary_sentences)
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
