
from flask import Flask, request, jsonify, render_template
from chatbot import get_response
from database import save_chat

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"]

    response = get_response(message)

    save_chat(message, response)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)