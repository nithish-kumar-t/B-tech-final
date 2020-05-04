from flask import Flask,render_template
from flask_socketio import SocketIO,emit
app = Flask(__name__)
app.config['SECRET_KEY']='kite!'
socketio=SocketIO(app)

@app.route("/")
def hello():
    return "Hello World!"
@app.route("/camera")
def camera():
    return render_template('video.html')
@app.route("/test")
def newCamera():
    return render_template('test.html')
@app.route("/test1")
def options():
    return render_template('new.html')
@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')
@socketio.on('camera')
def handler(message):
    socketio.emit('video',message)
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8000, debug=True,ssl_context=('cert.pem', 'key.pem'))
    socketio.run(app,host='0.0.0.0',port=8000,debug=True,ssl_context=('cert.pem','key.pem'))
