from app import db
from sqlalchemy.inspection import inspect

class ExpanseTracker(db.Model):
    __tablename__ = 'expanse_tracker'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False, unique=True)

    def to_dict(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}
    
class Expanses(db.Model):
    __tablename__ = 'user-expanses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    earn = db.Column(db.Integer, nullable=False)
    spend = db.Column(db.Integer, nullable=False)
    totalBalance = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

class LoginUser(db.Model):
    __tablename__ = 'login_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def to_dict(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}