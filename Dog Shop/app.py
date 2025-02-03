from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dog import dog_bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dogs.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(dog_bp, url_prefix = '/dogs')

    return app