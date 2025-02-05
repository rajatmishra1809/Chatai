from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get the OpenAI API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client with the API key from .env
client = OpenAI(api_key=api_key)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    try:
        # Create chat completion with OpenAI's new API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[{"role": "user", "content": user_message}]
        )
        
        # Extract the AI's response
        ai_response = response.choices[0].message.content
        
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
