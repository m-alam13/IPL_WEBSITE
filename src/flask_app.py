from flask import Flask
from flask_socketio import SocketIO


socket = SocketIO()
app = Flask(__name__)
app.secret_key = 'murshid'
socket.init_app(app=app)
from .views.home import home_bp
app.register_blueprint(blueprint=home_bp)




