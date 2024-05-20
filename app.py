from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.json
    prompt = data.get('prompt', '')
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return jsonify(response['choices'][0]['message']['content'])

if __name__ == '__main__':
    app.run(port=5000)
