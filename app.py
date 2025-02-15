from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "ChatGPT Wrapper API is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Invalid request. Please send a JSON payload with a 'message' field."}), 400

    message = data["message"]
    response_text = f"You said: {message}"  # Replace with OpenAI API call if needed

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

