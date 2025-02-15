import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)  # This creates the Flask app

# Initialize the OpenAI client correctly for the latest API version
openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Route for ChatGPT API
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")

    try:
        response = openai_client.chat.completions.create(  # Correct method
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )

        return jsonify({"response": response.choices[0].message.content})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
