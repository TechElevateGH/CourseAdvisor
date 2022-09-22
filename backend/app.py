from flask import Flask, request
from relations import Department
from relations import db, Course, University
import json
from datetime import datetime
from utils import error_response, success_response
from relations import db, Course, Post

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
    return success_response(courses, 200)


@app.route("/universities/<int:univ_id>/departments/<int:dept_id>/courses/", methods=["POST"])
def create_course(univ_id: int, dept_id: int):
    """ Creates university course """

    university = University.query.filter_by(id=univ_id)
    if not university:
        return error_response("Univeristy Not Found!", 404)
    department = Department.query.filter_by(id=dept_id)
    if not department:
        return error_response("Department Not Found!", 404)

    body = json.loads(request.data)
    try:
        professor, time = body.get("time"), body.get("professor")
        year, semester = body.get("semester"), body.get("year")
    except Exception as e:
        return error_response(e, 400)

    course = Course(
        time=time,
        professor=professor,
        department=dept_id,
        university=univ_id
    )

    db.session.add(course)
    db.session.commit()

    return 'Created'

####################### POST ROUTES #######################


@app.route('/courses/<int:course_id>/posts/', methods=["GET"])
def get_course_posts(course_id: int):
    course = Course.query.filter_by(id=course_id).first()
    if not course:
        return error_response("Course Not Found!", 404)

    posts = [post.serialize_for_course() for post in course.posts]
    return success_response(posts, 200)


@app.route('/courses/<int:course_id>/posts/', methods=["POST"])
def create_course_posts(course_id: int):
    """ Create a post for a course """

    course = Course.query.filter_by(id=course_id).first()
    if not course:
        return error_response("Course Not Found!", 404)

    body = json.loads(request.data)
    try:
        author, message, rating, instructor, date = body.get("author"), body.get(
            "message"), body.get("rating"), body.get("instructor"), datetime.now()
    except Exception as e:
        return error_response("Author, Message, Rating and Instructor Fields Required!")

    post = Post(
        author=author,
        message=message,
        ratin=rating,
        instructor=instructor,
        date=date
    )
    course.posts.append(post)
    db.session.add(post)
    db.session.commit()

    return success_response(post.serialize_for_course(), 200)


@app.route('/courses/<int:course_id>/posts/<int:post_id>/', methods=["GET"])
def edit_course_posts(course_id: int, post_id: int):
    course = Course.query.filter_by(id=course_id).first()
    if not course:
        return error_response("Course Not Found!", 404)

    post = Post.query.filter_by(id=post_id).first()
    if not post:
        return error_response("Post Not Found!", 404)

    body = request.data
    try:
        post.author, post.message, post.rating, post.instructor, post.date = body[
            "author"], body["message"], body["rating"], body["instructor"], datetime.now()
    except Exception as _:
        return error_response("Author, Message, Rating and Instructor Fields Required!")

    db.session.commit()
    return success_response(post, 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
