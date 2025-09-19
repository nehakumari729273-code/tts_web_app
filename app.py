from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

@app.route('/sender')
def sender():
    return render_template('sender.html')

@app.route('/receiver')
def receiver():
    return render_template('receiver.html')

@socketio.on('send_text')
def handle_send_text(data):
    text = data['text']
    print(f"Received text: {text}")
    emit('receive_text', {'text': text}, broadcast=True)

if __name__ == '__main__':
    print("\n--- Server running ---")
    socketio.run(app, host='0.0.0.0', port=5000)
