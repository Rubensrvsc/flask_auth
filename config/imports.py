from flask import Flask
from flask_jwt_extended import (
  JWTManager,
)
from flask_sqlalchemy import SQLAlchemy
from .settings import JWT_SECRET_KEY, DB_PATH

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DB_PATH
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
jwt = JWTManager(app)
db = SQLAlchemy(app)
