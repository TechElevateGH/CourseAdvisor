from flask import Flask, request
from relations import db, Course
import json
from datetime import date, datetime
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

####################### POST ROUTES #######################
@app.route('/courses/<int: course_id>/posts/', methods=["GET"])
def get_course_posts(course_id: int):
    course = Course.query.filter_by(id=course_id).first()
    if not course:
        return error_response("Course Not Found!", 404)

    posts = [post.serialize_for_course() for post in course.posts]
    return success_response(posts, 200)


@app.route('/courses/<int: course_id>/posts/', methods=["POST"])
def create_course_posts(course_id: int):
    """ Create a post for a course """

    course = Course.query.filter_by(id=course_id).first()
    if not course:
        return error_response("Course Not Found!", 404)

    body = request.data
    try:
        author, message, rating, instructor, date = body["author"], body[
            "message"], body["rating"], body["instructor"], datetime.now()
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


@app.route('/courses/<int: course_id>/posts/<int: post_id>/', methods=["GET"])
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
    except Exception as e:
        return error_response("Author, Message, Rating and Instructor Fields Required!")

    db.session.commit()
    return success_response(post, 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)