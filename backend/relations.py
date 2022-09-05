from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Course(db.Model):
    pass







class Post(db.Model):
    pass


    def serialize_for_course(self):
        """ An object representation of a post"""
        pass