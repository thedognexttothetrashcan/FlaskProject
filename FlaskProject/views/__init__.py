from FlaskProject.views.first_blue import blue
from FlaskProject.views.student_blue import blue_student


def init_blue(app):
    app.register_blueprint(blueprint=blue)
    app.register_blueprint(blueprint=blue_student)

