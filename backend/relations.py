from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


class University(db.Model):
    __tablename__ = "university"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    logo = db.Column(db.String, nullable=False)
    departments = db.relationship("Department", backref="university")
    courses = db.relationship("Course", backref="university")

    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get("name")
        self.logo = kwargs.get("logo")


class Department(db.Model):
    __tablename__ = "department"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    university = db.Column(db.Integer, db.ForeignKey("university.id"))
    courses = db.relationship("Course", backref="department")

    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get("name")
        self.university = kwargs.get("university")
        self.logo = kwargs.get("logo")

    def serialize(self):
        return ({
            "name": self.name,
            "university": self.university,
            "courses": [course.serialize() for course in self.courses]
        })


class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    university = db.Column(db.Integer, db.ForeignKey('university.id'),
                           nullable=False)
    reviews = db.relationship('Review', backref='course')
    num_reviews = db.Column(db.Integer)
    overall_rating = db.Column(db.Integer)

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.university = kwargs.get("university")

    def serialize(self):
        return ({
            "id": self.id,
            "name": self.name,
            "university": self.university,
            "reviews": [review.serialize() for review in self.reviews],
            "num_posts": self.num_posts,
            "overall_rating": self.overall_rating
        })



class Review(db.Model):
    __tablename__ = "review"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course = db.Column(db.Integer, db.ForeignKey('course.id'),
                       nullable=False)
    author = db.Column(db.String, nullable=False)
    professor = db.Column(db.String)
    semester = db.Column(db.String)
    year = db.Column(db.String)
    comments = db.relationship('Comment', backref='review')
    rating = db.Column(db.Integer)
    time_stamp = db.Column(db.DateTime(timezone=True),nullable=False, server_default=func.utcnow())

    def __init__(self, **kwargs):
        self.comment = kwargs.get("comment")
        self.author = kwargs.get("author")

    def serialize(self):
        return ({
            "id": self.id,
            "course": self.course,
            "author": self.author,
            "professor": self.professor,
            "semester": self.semester,
            "year": self.year,
            "comments": [comment.serialize() for comment in self.comments],
            "rating": self.rating,
            "time": self.time
        })


    def serialize_for_course(self):
        return ({
            "author": self.author,
            "comment": self.comment,
            "rating": self.rating,
        })

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    review = db.Column(db.Integer, db.ForeignKey("review.id"))
    author = db.Column(db.String,nullable = False)
    comment = db.Column(db.Text, nullable=False)
    num_likes = db.Column(db.Integer)

    def __init__(self,**kwargs):
        self.author = kwargs.get("author")
        self.comment = kwargs.get("comment")   

    def serialize(self):
        return {
            "id":self.id,
            "review":self.review,
            "author":self.author,
            "comment":self.comment,
            "num_likes":self.num_likes
        }     
    

