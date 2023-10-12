#!/usr/bin/env python3

from flask import request, make_response, session
from flask_restful import Resource
from sqlalchemy.orm import validates

# Local imports
from config import app, db, api

# Add your model imports
from models import *

#routes
@app.route('/')
def home():
    return 'Getting to Know the PWHL Server'

class User_By_Id(Resource):
    def get(self, id):
        user = User.query.get(id)
        if user:
            user_json = user.to_dict()
            return make_response(user_json, 200)
        else:
            return make_response({"error": "User not found"}, 404)
    
    def patch(self, id):
        user = User.query.get(id)
        r = request.get_json()
        if user:
            try:
                for attr in r:
                    setattr(user, attr, r.get(attr))
                db.session.commit()
                user_json = user.to_dict()
                return make_response(user_json, 202)
            except:
                errors = user.validation_errors
                user.clear_validation_errors()
                return make_response({"errors": errors}, 422)
        else:
            return make_response({"error": "User not found"}, 404)

    def delete(self, id):
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error": "User not found"}, 404)

class Quiz_By_Id(Resource):
    def get(self, id):
        quiz = Quiz.query.get(id)
        if quiz:
            quiz_json = quiz.to_dict()
            return make_response(quiz_json, 200)
        else:
            return make_response({"error": "Quiz not found"}, 404)

class Score(Resource):
    def post(self):
        r = request.get_json()
        num_correct = r.get("num_correct")
        score = Score(num_correct=num_correct)
    
        try:
            db.session.add(score)
            db.session.commit()
            session["user_id"] = score.user_id
            return score.to_dict(), 201

        except ValueError:
            return make_response({"error": "422 Unprocessable Entity"}, 422)
        
class News(Resource):
    def get(self):
        URL = "https://newsapi.org/v2/everything?q=PWHL&apiKey=5202fc131d704365898754aeb2834af7"
        r = request.get(URL)
        return r.articles

class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get("user_id")).first()
        if user:
            return make_response(user.to_dict(), 200)
        return make_response({"error": "401 Unauthorized"}, 401)

class Login(Resource):
    def post(self):
        r = request.get_json()
        username = r.get("username")
        password = r.get("password")
        user = User.query.filter(User.username == username).first()
        if user:
            if user.authenticate(password):
                session["user_id"] = user.id
                response = make_response(user.to_dict(), 200)
                return response
        return make_response({"error": "401 Unauthorized"}, 401)

class Logout(Resource):
    def delete(self):
        session["user_id"] = None
        return make_response({}, 204)
    
class Create_Account(Resource):
    def post(self):
        r = request.get_json()

        username = r.get("username")
        email = r.get("email")
        password = r.get("password")
        user = User(username=username, email=email)
        user.password_hash = password

        try:
            db.session.add(user)
            db.session.commit()
            session["user_id"] = user.id
            return user.to_dict(), 201
        
        except ValueError:
            return make_response({"error": "422 Unprocessable Entity"}, 422)

api.add_resource(CheckSession, "/check-session")
api.add_resource(User_By_Id, "/user/<int:id>")
api.add_resource(Score, "/scores")
api.add_resource(News, "/news")
api.add_resource(Login, "/login")
api.add_resource(Logout, "/logout")
api.add_resource(Create_Account, "/create-account")


if __name__ == '__main__':
    app.run(port=5555, debug=True)