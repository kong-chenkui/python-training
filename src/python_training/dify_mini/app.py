import json
from flask import Flask, request

app = Flask(__name__)

@app.route("/v1/chat-messages",methods=["POST"])
def chat_messages():
    data = request.get_json()
    query=data.get("query","")
    return query

if __name__ == "__main__":
    app.run()