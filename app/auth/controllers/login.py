import datetime
import json
from re import A
from flask import abort, jsonify, make_response, request, session
from flask_restful import Resource
from app import app
from app.md.models import User
import jwt

from app.md.serde import UserSchema

class LoginView(Resource):
    def get(self):
        return {"Login":"Successful"}

    def post(self):
        credentials=request.get_json()
        user=User.query.filter_by(username=credentials["username"]).first()
        session['user_id']=user.id
        if not user:
            abort(401)

        if not user.verify_password(credentials["password"]):
            abort(401)
        token = jwt.encode({'user_id' : user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, app.config['SECRET_KEY'],algorithm="HS256")
        return jsonify({'token' : token})
        
        