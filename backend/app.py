from flask import Flask, request
from relations import db, Course
import json

# Initialize Flask
app = Flask(__name__)

# DB config
db_filename = "course_advisor.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/', methods=["GET"])
def home():
    return "Welcome to Course Advisor- TechElevate"


@app.route('/courses/', methods=["GET"])
def get_courses():
    courses = [crs.serialize() for crs in Course.query.all()]
    return json.dumps(courses)

@app.route('/courses/', methods=["POST"])
def create_course_comment():
    body = json.loads(request.data)
    comments, author = body.get("author"), body.get("comments")
    professor, time = body.get("time"), body.get("professor")
    year, semester = body.get("semester"), body.get("year")
    
    crs = Course(author=author, comments=comments, time=time, professor=professor, semester=semester, year=year)
    db.session.add(crs)
    db.session.commit()

    return 'Created'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
