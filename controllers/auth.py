from crypt import methods
from os import access
from flask import jsonify, request
from config.imports import app
from models.user import User
from config.imports import db
import pdb
from flask_jwt_extended import (
  jwt_required,
  create_access_token,
)

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
def all_users():
  query = [ result.serialize for result in User.query.all() ] 
  return jsonify(data=query)

@app.route('/create_task', methods=["POST"])
def create_task():
  pass