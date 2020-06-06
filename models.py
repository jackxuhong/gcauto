from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    email = db.Column(db.String(100))
    name = db.Column(db.String(128))
    given_name = db.Column(db.String(64))
    family_name = db.Column(db.String(64))
    picture = db.Column(db.String(256))

    def __repr__(self):
        return f'<User {self.id} {self.name}>'


class ManagedCourse(db.Model):
    userId = db.Column(db.String(64), primary_key=True)
    courseId = db.Column(db.String(64), primary_key=True)

    def __repr__(self):
        return f'<ManagedCourse {self.courseId} of user {self.userId}'


class RecurringCoursework(db.Model):
    courseId: db.Column(db.String(64))

    def __repr__(self):
        return f'<RecurringCoursework {self.courseId}'
