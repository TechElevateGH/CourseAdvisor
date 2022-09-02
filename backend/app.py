from flask import Flask, request
from relations import db, Course

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
    courses = Course.query.all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
