import json

with open("intents.json", "r") as file:
    data = json.load(file)

def get_response(user_message):
    user_message = user_message.lower()

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern in user_message:
                return intent["response"]

    return "Sorry, I don't understand your question."