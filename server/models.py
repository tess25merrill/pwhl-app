from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from config import app, db, api

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    #relationships
    #serialization
    def to_dict(self):
        return {
            'id': self.id, 
            'username': self.username,
            'email': self.email
        }

    #validations
    validation_errors = []

    @classmethod
    def clear_validation_errors(cls):
        cls.validation_errors = []

    @validates('username')
    def validate_username(self, key, username):
        if type(username) is str and 0 < len(username) < 21:
            return username
        else:
            self.validation_errors.append('Username must be between 1 and 20 characters.')

class Quiz(db.Model):
    __tablename__ = 'quizzes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    category = db.Column(db.String)

    #serialization
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category
        }

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.String)

    #relationships
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)

    #serialization
    #validations
    validation_errors = []

    @classmethod
    def clear_validation_errors(cls):
        cls.validation_errors = []

    @validates('prompt')
    def validate_username(self, key, prompt):
        if type(prompt) is str:
            return prompt
        else:
            self.validation_errors.append('Prompt must be a string.')

class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    correct = db.Column(db.Boolean)

    #relationships
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)

    #serialization
    #validations
    validation_errors = []

    @classmethod
    def clear_validation_errors(cls):
        cls.validation_errors = []

    @validates('text')
    def validate_username(self, key, text):
        if type(text) is str:
            return text
        else:
            self.validation_errors.append('Text must be a string.')

class Score(db.Model):
    __tablename__ = 'scores'

    id = db.Column(db.Integer, primary_key=True)
    num_correct = db.Column(db.Integer)

    #relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)