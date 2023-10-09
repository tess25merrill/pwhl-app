#!/usr/bin/env python3

from flask import request, make_response, session
from flask_restful import Resource
from sqlalchemy.orm import validates

# Local imports
from config import app, db, api

# Add your model imports
from models import *

#routes

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

class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get("user_id")).first()
        if user:
            return make_response(user.to_dict(), 200)
        return make_response({"error": "401 Unauthorized"}, 401)

api.add_resource(CheckSession, "/check-session")
api.add_resource(User_By_Id, "/user/<int:id>")
api.add_resource(Score, "/scores")

@app.route('/')
def index():
    return '<h1>PWHL Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)