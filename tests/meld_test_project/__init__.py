import secrets
from flask import Flask, render_template
from flask_meld import Meld

# extensions
meld = Meld()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = secrets.token_hex(16)

    meld.init_app(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=5001)
