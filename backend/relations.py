from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    advices = db.relationship('Advice', backref='course')

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.author = kwargs.get("author")
        self.advices = kwargs.get("advices")

    def serialise_advice(self):
        return {
            "id":self.id,
            "advice":self.advice
        }

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "author": self.author,
            "advices": [advice.serialize_advice() for advice in self.advices]
        }

class Advice(db.Model):
    __tablename__ = "advice"
    id = db.Column(db.Integer, primary_key=True)
    advice = db.Column(db.String, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'),
        nullable=False)
    author = db.Column(db.String)
    comments = db.Column(db.String)
    time = db.Column(db.String)
    professor = db.Column(db.String)
    semester = db.Column(db.String)
    year = db.Column(db.String)
    
    def serialize(self):
        return ({
            "id": self.id,
            "author": self.author,
            "comments": self.comments,
            "time": self.time,
            "professor": self.professor,
            "semester": self.semester,
            "year": self.year
        })







class Post(db.Model):
    pass


    def serialize_for_course(self):
        """ An object representation of a post"""
        pass
