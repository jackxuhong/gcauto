import functools
import json
import os
from datetime import datetime

import flask
import google.oauth2.credentials
import googleapiclient.discovery
from authlib.integrations.requests_client import OAuth2Session
from googleapiclient.discovery import build

import google_auth

app = flask.Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", default=os.urandom(24))
app.config['SESSION_TYPE'] = 'filesystem'

app.register_blueprint(google_auth.google_auth)


def gc_service():
    credentials = google_auth.build_credentials()
    service = build('classroom', 'v1', credentials=credentials)
    return service


def test_task1(courseId):
    today = datetime.today().strftime('%Y-%m-%d')
    daily_workout = {
        'title': f'Daily Workout {today}',
        'description': 'Healthy body healthy brain!',
        'maxPoints': 30,
        'workType': 'ASSIGNMENT',
        'state': 'PUBLISHED'
    }
    daily_workout = gc_service().courses().courseWork().create(
        courseId=courseId, body=daily_workout).execute()


@app.route('/')
def index():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()

        #credentials = google_auth.build_credentials()
        #service = build('classroom', 'v1', credentials=credentials)
        results = gc_service().courses().list(pageSize=10).execute()
        courses = results.get('courses', [])
        print(courses)

        return flask.render_template('home.html', user_info=user_info, courses=courses)

    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run()
