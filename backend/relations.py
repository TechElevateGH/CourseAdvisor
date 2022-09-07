from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
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
