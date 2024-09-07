# std imports
import time

# installed imports
import flask
import timeago
import tinydb
import logging

# handlers
from handlers import friends, login, posts, test_blue

app = flask.Flask(__name__)

# app.logger.setLevel(logging.INFO)  # Set log level to INFO
# handler = logging.FileHandler('app.log')  # Create the file logger
# app.logger.addHandler(handler)  # Add the file logger to the app


# @app.route('/')
# def home():
#     app.logger.info('info')
#     return flask.send_from_directory('frontend/build', 'index.html');


# @app.route('/<path:path>')
# def static_proxy(path):
#     return flask.send_from_directory('frontend/build', path)

app.register_blueprint(test_blue.blueprint)
app.register_blueprint(login.blueprint)


# @app.template_filter('convert_time')
# def convert_time(ts):
#     """A jinja template helper to convert timestamps to timeago."""
#     print('convert_time')
#     return timeago.format(ts, time.time())

app.register_blueprint(friends.blueprint)

app.register_blueprint(posts.blueprint)
# app.register_blueprint(test_blue.blueprint)

app.secret_key = 'mygroup'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.run(debug=True, host='0.0.0.0', port=3000)
