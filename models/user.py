from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.imports import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username
        }

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_task = db.Column(db.String(200), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    user_tasks = db.relationship('User', backref=db.backref('tasks',lazy=True))