import json
import random

with open("intents.json") as file:
    intents = json.load(file)

def chatbot_response(message):
    message = message.lower()

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in message:
                return random.choice(intent["responses"])

    return "Sorry, I don't understand your question."
