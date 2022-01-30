from flask import Flask
from flask_jwt_extended import (
  JWTManager,
)
from flask_sqlalchemy import SQLAlchemy
from .settings import JWT_SECRET_KEY, DB_PATH, ACCESS_EXPIRE

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRE
app.config["SQLALCHEMY_DATABASE_URI"] = DB_PATH
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
jwt = JWTManager(app)
db = SQLAlchemy(app)
