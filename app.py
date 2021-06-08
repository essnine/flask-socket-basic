from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
import os
from loguru import logger


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "")
socketio = SocketIO(app)


@socketio.on('message', namespace='/chat')
def handle_message(data):
    logger.info(f"received message: {data}")


@socketio.on('json', namespace='/chat')
def handle_json(json):
    logger.info(f"received message: {str(json)}")
    emit("chat",{"message":"message received"}, namespace="/chat")
    

@socketio.on('chatMessage', namespace='/chat')
def handle_chat_message(data):
    msg_val = data.get("message")
    if msg_val is None:
        logger.error("message not in payload")
    else:
        logger.info(f"chatmessage value: {msg_val}")
        emit("chatMessage", {"success": True, "message": msg_val})


@app.route('/chat')
def chat():
    return render_template('chat.html')


if __name__ == "__main__":
    socketio.run(app)
