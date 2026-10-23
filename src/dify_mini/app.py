import json
from flask import Flask, request,Response
from .events import sse_generator

app = Flask(__name__)

@app.route("/v1/chat-messages", methods=["POST"])
def chat_messages():
    data = request.get_json()
    query = data.get("query", "")
    messages = [{"role": "user", "content": query}]
    return Response(
        sse_generator(messages),
        mimetype="text/event-stream",
    )

if __name__ == "__main__":
    app.run()