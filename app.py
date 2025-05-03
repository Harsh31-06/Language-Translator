from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form.get('text', '')
    
    if not text.strip():
        return jsonify({'error': 'No text provided'}), 400

    try:
        hindi_translation = GoogleTranslator(source='en', target='hi').translate(text)
        return jsonify({'english': text, 'hindi': hindi_translation})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
