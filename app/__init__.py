# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.update({
        "SQLALCHEMY_DATABASE_URI": "sqlite:///expanse_tracker.db",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    })

    db.init_app(app)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
