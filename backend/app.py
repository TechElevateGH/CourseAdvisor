from flask import Flask, request
from CourseAdvisor.backend.utils import error_response, success_response
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





####################### POST ROUTES #######################
@app.route('/courses/<int: course_id>/posts/<int: post_id>/', methods=["GET"])
def get_course_posts(course_id: int, post_id: int):
    course = Course.query.filter_by(id=course_id).first()
    if not course:
        return error_response("Course Not Found!", 404)
    
    posts = [post.serialize_for_course() for post in course.posts]

    return success_response(posts, 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
