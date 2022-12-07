from flask import Flask
from .controllers import controllers
from .models import UPLOAD_FOLDER


def init_app():
    """Initialise Flask app and run"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret stuff'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.register_blueprint(controllers, url_prefix='/')

    return app
