from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def home():
    return "Chat server is running!"

@socketio.on('message')
def handle_message(msg):
    print("Message:", msg)
    send(msg, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
