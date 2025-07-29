# Samenvatten API

Een eenvoudige Flask API die tekst samenvat met behulp van het `facebook/bart-large-cnn` model via HuggingFace Transformers.

## Gebruik

### POST /

Stuur een JSON met `text` naar de root endpoint:

```json
{
  "text": "Dit is een voorbeeldtekst die samengevat moet worden."
}
