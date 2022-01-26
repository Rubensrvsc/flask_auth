from flask import Flask, jsonify, request
from flask_jwt_extended import (
  JWTManager,
)
from flask_sqlalchemy import SQLAlchemy
from settings import JWT_SECRET_KEY, DB_PATH

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY  # Change this!
app.config['SQLALCHEMY_DATABASE_URI'] = DB_PATH
jwt = JWTManager(app)
db = SQLAlchemy(app)
