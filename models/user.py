from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.imports import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tasks = db.relationship('Task',
        backref=db.backref('user', lazy=True))

    def __repr__(self):
        return f"User: {self.username}"
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username
        }

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_task = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)

    def __repr__(self) -> str:
        return f"Task: {self.name_task}"