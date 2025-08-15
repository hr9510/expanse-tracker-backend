# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.update({
    #    'SQLALCHEMY_DATABASE_URI': "postgresql://flaskdb_60cb_user:5YN8MXljQ395a0gqS5jSTmIb7lcsRLY2@dpg-d2fevlumcj7s73eogqdg-a.oregon-postgres.render.com/flaskdb_60cb",
        "SQLALCHEMY_DATABASE_URI": "postgresql://postgres:himanshu%409510@localhost:5432/flaskdb",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "SQLALCHEMY_ECHO": True,
    })

    db.init_app(app)

    with app.app_context():
        from .models import ExpanseTracker  # Import models
        db.create_all()                     # Ensure tables are created

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app


