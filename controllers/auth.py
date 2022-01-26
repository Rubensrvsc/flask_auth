from crypt import methods
from flask import jsonify, request
from config.imports import app
from models.user import User
from config.imports import db
import pdb
from flask_jwt_extended import (
  jwt_required,
  create_access_token,
)
import json

@app.route('/login',methods=["POST"])
def login():
  pass

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
def hello_world():
  query = [ result.serialize for result in User.query.all() ] 
  return jsonify(data=query)