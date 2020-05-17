import functools
import json
import os

import flask

from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery
from googleapiclient.discovery import build

import google_auth

app = flask.Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", default=False)
app.config['SESSION_TYPE'] = 'filesystem'

app.register_blueprint(google_auth.app)


@app.route('/')
def index():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()

        credentials = google_auth.build_credentials()
        service = build('classroom', 'v1', credentials=credentials)
        results = service.courses().list(pageSize=10).execute()
        courses = results.get('courses', [])
        print(courses)

        return flask.render_template('home.html', user_info=user_info, courses=courses)

    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run()
