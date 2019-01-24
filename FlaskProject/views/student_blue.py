from flask import Blueprint

blue_student = Blueprint("blue_student", __name__, url_prefix='/students')


@blue_student.route("/")
def haha():
    return "Haha"