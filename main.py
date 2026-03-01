import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from google import genai
from google.genai import types
import json
from utils import load_system_prompt

load_dotenv()

app = Flask(__name__, static_folder='frontend')
CORS(app)

client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({'error': 'Missing prompt'}), 400
    
    try:
        system_prompt = load_system_prompt()
        
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0,
                response_mime_type="application/json",
                system_instruction=system_prompt
            )
        )
        
        reply = response.text.strip()
        print('reply:', reply)
        
        try:
            parsed = json.loads(reply)
        except json.JSONDecodeError:
            return jsonify({
                'error': 'Failed to parse Gemini response as JSON',
                'raw': reply
            }), 500
        
        return jsonify(parsed)
    
    except Exception as err:
        print('Server error:', err)
        return jsonify({'error': 'Internal error', 'details': str(err)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=True)

