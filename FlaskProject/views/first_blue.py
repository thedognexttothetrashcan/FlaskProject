from flask import Blueprint
from FlaskProject.models import Student

blue = Blueprint("blue", __name__, url_prefix='/blue')


@blue.route("/")
def index():
    return "Index"