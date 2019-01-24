from FlaskProject.extension import db


class Teacher(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    t_name = db.Column(db.String(16))