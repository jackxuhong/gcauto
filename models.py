from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.String(64), primary_key=True)


class ManagedCourse(db.Model):
    userId = db.Column(db.String(64), primary_key=True)
    courseId = db.Column(db.String(64), primary_key=True)
