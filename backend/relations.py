from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150),)
    author = db.Column(db.String(150),)
    advices = db.relationship('Advice', backref='course')


    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.author = kwargs.get("author")
        self.advices = kwargs.get("advices")

    def serialise_advice(self):
        return {
            "id":self.id,
            "advices":self.advices
        }

    def serialize_for_advice(self):
        return {
            "id": self.id,
            "name": self.name,
            "author": self.author,
            "advices": [advice.serialize_advice() for advice in self.advices]
        }



class Advice(db.Model):
    __tablename__ = "advice"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    advice = db.Column(db.String(15000))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    date = db.column(db.DateTime(timezone=True), default=func.now())
    
    


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(150))
    comments = db.relationship('Comment', backref='post')
    time = db.column(db.DateTime(timezone=True), default=func.now())
    professor = db.Column(db.String(150))
    semester = db.Column(db.Integer)
    year = db.column(db.DateTime(timezone=False), default=func.now())
    
    

    def __init__(self, **kwargs):
        self.author = kwargs.get("author")
        self.comments = kwargs.get("comments")
        self.time = kwargs.get("time")
        self.professor = kwargs.get("professor")
        self.semester = kwargs.get("semester")
        self.year = kwargs.get("year")

    def serialise_post(self):
        return {
            "id":self.id,
            "comments":self.comments
        }

    def serialize_for_course(self):
        """ An object representation of a post"""
        return {
            "id": self.id,
            "author": self.author,
            "comments": [comment.serialize_post() for comment in self.comments],
            "time": self.time,
            "professor": self.professor,
            "semester": self.semester,
            "year": self.year,
        }
        
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comments = db.Column(db.String(15000))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    date = db.column(db.DateTime(timezone=True), default=func.now())