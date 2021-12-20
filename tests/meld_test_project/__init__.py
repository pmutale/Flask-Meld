import secrets
from flask import Flask, render_template
from flask_meld import Meld
from flask_socketio import SocketIO

# extensions
meld = Meld()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config["DEBUG"] = False
    socketio = SocketIO(app, async_mode="threading")
    meld.init_app(app, socketio)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
