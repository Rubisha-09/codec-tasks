from flask import Flask, request, jsonify
from chatbot import chatbot_response

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Chatbot is running successfully!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data["message"]
    response = chatbot_response(user_message)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
