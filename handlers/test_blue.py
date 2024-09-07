import flask

from db import helpers, users

blueprint = flask.Blueprint("test", __name__, template_folder='../frontend/build')

# @blueprint.route('/')
# def root():

#     return flask.send_from_directory('frontend/build', 'index.html')

@blueprint.route('/_app/<path:path>')
def test_blue(path):
    if path.endswith('/'):
        path = path + 'index.html'
    return flask.send_from_directory('frontend/build/_app', path)

# @blueprint.route('/blue_test/<name>')
# def blue_test(name):
#     return flask.render_template('/test_blue/index.html', message=name)