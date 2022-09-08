from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class University(db.Model):
    __tablename__ = "universities"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    logo = db.Column(db.String, nullable=False)
    departments = db.relationship("Department", backref="university")
    courses = db.relationship("Course", backref="university")

    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get("name")
        self.logo = kwargs.get("logo")


class Department(db.Model):
    __tablename__ = "departments"
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
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    department = db.Column(db.Integer, db.ForeignKey("department.id"))
    university = db.Column(db.Integer, db.ForeignKey("university.id"))
    advices = db.relationship('Advice', backref='course')

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.advices = kwargs.get("advices")

    def serialise(self):
        return {
            "id": self.id,
            "name": self.name
        }

    def serialize_for_course(self):
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
