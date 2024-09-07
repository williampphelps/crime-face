import flask

from handlers import copy
from db import posts, users, helpers

blueprint = flask.Blueprint("login", __name__)

@blueprint.route('/account/login/')
def loginscreen():
    """Present a form to the user to enter their username and password."""
    db = helpers.load_db()

    # First check if already logged in
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    if username is not None and password is not None:
        if users.get_user(db, username, password):
            # If they are logged in, redirect them to the feed page
            flask.flash('You are already logged in.', 'warning')
            return flask.redirect(flask.url_for('login.index'))

    return flask.send_from_directory('frontend/build/account/login', 'index.html')

@blueprint.route('/account/signup/')
def signupscreen():
    """Present a form to the user to enter their username and password."""
    db = helpers.load_db()

    # First check if already logged in
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    if username is not None and password is not None:
        if users.get_user(db, username, password):
            # If they are logged in, redirect them to the feed page
            flask.flash('You are already logged in.', 'warning')
            return flask.redirect(flask.url_for('login.index'))

    return flask.send_from_directory('frontend/build/account/signup', 'index.html')

@blueprint.route('/login', methods=['POST'])
def login():
    """Log in the user.

    Using the username and password fields on the form, create, delete, or
    log in a user, based on what button they click.
    """
    db = helpers.load_db()

    content = flask.request.json

    username = content.get('username')
    password = content.get('password')

    if username is None or password is None:
        return flask.make_response(flask.jsonify({'error': 'Username and password required!'}), 400)

    resp = flask.make_response(flask.jsonify({'success': 'User logged in successfully!'}))
    

    user = users.get_user(db, username, password)
    if not user:
        resp = flask.make_response(flask.jsonify({'error': 'Invalid credentials. Please try again.'}), 400)
        resp.set_cookie('username', '', expires=0)
        resp.set_cookie('password', '', expires=0)
    resp.set_cookie('username', username)
    resp.set_cookie('password', password)

    submit = content.get('type')
    if submit == 'Create':
        if users.new_user(db, username, password) is None:
            resp.set_cookie('username', '', expires=0)
            resp.set_cookie('password', '', expires=0)
            flask.flash('Username {} already taken!'.format(username), 'danger')
            # return flask.redirect(flask.url_for('login.loginscreen'))
            return flask.make_response(flask.jsonify({'error': 'Username {} already taken!'.format(username)}), 400)
        # flask.flash('User {} created successfully!'.format(username), 'success')
        return flask.make_response(flask.jsonify({'success': 'User {} created successfully!'.format(username)}), 200)
    elif submit == 'Delete':
        if users.delete_user(db, username, password):
            resp.set_cookie('username', '', expires=0)
            resp.set_cookie('password', '', expires=0)
            flask.flash('User {} deleted successfully!'.format(username), 'success')

    return resp

@blueprint.route('/logout', methods=['POST'])
def logout():
    """Log out the user."""
    db = helpers.load_db()

    resp = flask.make_response(flask.jsonify({'success': 'User logged out successfully!'}), 200)
    resp.set_cookie('username', '', expires=0)
    resp.set_cookie('password', '', expires=0)
    return resp

@blueprint.route('/')
def index():
    """Serves the main feed page for the user."""
    db = helpers.load_db()

    # make sure the user is logged in
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')
    if username is None and password is None:
        return flask.redirect(flask.url_for('login.loginscreen'))
    user = users.get_user(db, username, password)
    print(user)
    if not user:
        flask.flash('Invalid credentials. Please try again.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))

    # get the info for the user's feed
    # friends = users.get_user_friends(db, user)
    # all_posts = []
    # for friend in friends + [user]:
    #     all_posts += posts.get_posts(db, friend)
    # # sort posts
    # sorted_posts = sorted(all_posts, key=lambda post: post['time'], reverse=True)

    # return flask.render_template('feed.html', title=copy.title,
    #         subtitle=copy.subtitle, user=user, username=username,
    #         friends=friends, posts=sorted_posts)

    return flask.send_from_directory('frontend/build', 'index.html')
