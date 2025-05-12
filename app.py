from flask import Flask, render_template, request, jsonify, make_response
from openai_client import client
from uuid import uuid4

app = Flask(__name__)

# storage - redis, db, or in-memory
chat_histories = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/agent/start", methods=["GET"])
def start_session():
    session_id = str(uuid4())
    chat_histories[session_id] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    return jsonify({"session_id": session_id})


@app.route("/agent/ask", methods=["POST"])
def ask():
    data = request.json
    session_id = data.get("session_id")
    user_message = data.get("message")
    if not session_id or not user_message:
        return jsonify({"error": "Missing session_id or message"}), 400
    if session_id not in chat_histories:
        return jsonify({"error": "Invalid session_id"}), 404
    try:
        # Append user message to chat history
        chat_histories[session_id].append({"role": "user", "content": user_message})
        # Send full chat history to OpenAI
        response = client.chat.completions.create(
            model="gpt-4", messages=chat_histories[session_id]
        )
        content = response.choices[0].message.content
        # Add assistant's reply to history
        chat_histories[session_id].append({"role": "assistant", "content": content})
        return make_response(jsonify({"reply": content}), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)


@app.route("/generate", methods=["POST"])
def generate():
    return "generate"


if __name__ == "__main__":
    app.run()
