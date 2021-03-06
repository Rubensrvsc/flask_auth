from crypt import methods
from os import access
from flask import jsonify, request
from config.imports import app
from models.user import User, Task
from config.imports import db, jwt
from flask_jwt_extended import (
  jwt_required,
  create_access_token,
  current_user,
)
from services.get_all_tasks_for_user import all_tasks
from services.create_task import create_task_to_user


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(username=identity).one_or_none()

# @jwt.user_identity_loader
# def user_identity_lookup(user):
#   return user.id

@app.route('/login',methods=["POST"])
def login():
  username = request.json.get('username')
  email = request.json.get('email')

  if username and email:
    user = User.query.filter_by(username=username, email=email).first()
    access_token = create_access_token(identity=user.username)
    return jsonify(access_token=access_token)
    
  return jsonify({"msg": "Without username or password"}), 401

@app.route('/register',methods=["POST"])
def register():

  if request.json.get('username') and request.json.get('email'):
    user = User(username=request.json['username'], email=request.json['email'])
    db.session.add(user)
    db.session.commit()
    access_token = create_access_token(identity=request.json['username'])
    return jsonify(access_token=access_token)

  return jsonify({"msg": "Without username or password"}), 401

@app.route('/')
@jwt_required()
def all_users():
  query = all_tasks(current_user.id)
  return jsonify(data=query)

@app.route('/create_task', methods=["POST"])
@jwt_required()
def create_task():
  data = create_task_to_user(current_user.id, request.json.get('name_task'))
  return jsonify(data=data)