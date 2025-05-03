# English to Hindi Translator Website

Here's a complete solution to create a web-based English to Hindi translator using Python with Flask. This creates a simple but functional website that you can run locally.

## 1. First, install the required packages:
bash
pip install flask deep-translator


## 2. Create the Flask application

Create a file named app.py with the following code:

python
from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        english_text = request.form['text']
        if not english_text.strip():
            return jsonify({'error': 'Please enter some text to translate'})
        
        translation = GoogleTranslator(source='en', target='hi').translate(english_text)
        return jsonify({
            'english': english_text,
            'hindi': translation
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


## 3. Create the HTML template

Create a folder named templates and inside it create index.html:

html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>English to Hindi Translator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .translator-box {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        textarea {
            width: 100%;
            height: 100px;
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            resize: vertical;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #2980b9;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            background-color: #f9f9f9;
            border-radius: 4px;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>English to Hindi Translator</h1>
    
    <div class="translator-box">
        <textarea id="englishText" placeholder="Enter English text here..."></textarea>
        <button onclick="translateText()">Translate to Hindi</button>
        
        <div class="result" id="result">
            <p>Translation will appear here...</p>
        </div>
    </div>

    <script>
        function translateText() {
            const englishText = document.getElementById('englishText').value;
            const resultDiv = document.getElementById('result');
            
            if (!englishText.trim()) {
                resultDiv.innerHTML = '<p class="error">Please enter some text to translate</p>';
                return;
            }
            
            resultDiv.innerHTML = '<p>Translating...</p>';
            
            fetch('/translate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `text=${encodeURIComponent(englishText)}`
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    resultDiv.innerHTML = `<p class="error">${data.error}</p>`;
                } else {
                    resultDiv.innerHTML = `
                        <p><strong>English:</strong> ${data.english}</p>
                        <p><strong>Hindi:</strong> ${data.hindi}</p>
                    `;
                }
            })
            .catch(error => {
                resultDiv.innerHTML = `<p class="error">Translation failed: ${error}</p>`;
            });
        }
    </script>
</body>
</html>


## 4. Run the application

Start the Flask development server by running:
bash
python app.py


## 5. Access the website

Open your web browser and go to:

http://localhost:5000


## Features of this implementation:

1. Clean, responsive web interface
2. Real-time translation without page reload (using fetch API)
3. Error handling
4. Simple but attractive design
5. Easy to deploy to hosting services

## How to Deploy Online:

If you want to make this accessible on the internet, you can:
1. Deploy to PythonAnywhere (free tier available)
2. Use Heroku (free tier available)
3. Use Vercel or Netlify with Python support

Would you like me to provide instructions for any specific deployment method? Or would you like to enhance the website with additional features like pronunciation, history, or user accounts?
