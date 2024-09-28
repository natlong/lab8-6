from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/', methods=["POST", "GET"])
def index():
    return render_template('index.html')


    
if __name__ == "__main__":
    app.run(debug=True)