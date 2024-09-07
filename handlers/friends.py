import flask

from handlers import copy
from db import posts, users, helpers

blueprint = flask.Blueprint("friends", __name__)

@blueprint.route('/addfriend', methods=['POST'])
def addfriend():
    """Adds a friend to the user's friends list."""
    db = helpers.load_db()

    # make sure the user is logged in
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    if username is None and password is None:
        # return flask.redirect(flask.url_for('login.loginscreen'))
        return flask.make_response(flask.jsonify({'error': 'You need to be logged in to do that.'}), 401)

    user = users.get_user(db, username, password)
    if not user:
        # flash('You need to be logged in to do that.', 'danger')
        # return flask.redirect(flask.url_for('login.loginscreen'))
        return flask.make_response(flask.jsonify({'error': 'You need to be logged in to do that.'}), 401)

    # add the friend
    name = flask.request.json.get('username')
    msg, category = users.add_user_friend(db, user, name)

    # flask.flash(msg, category)
    # return flask.redirect(flask.url_for('login.index'))
    return flask.make_response(flask.jsonify({'success': msg}), 200)

@blueprint.route('/unfriend', methods=['POST'])
def unfriend():
    """Removes a user from the user's friends list."""
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))

    name = flask.request.form.get('name')
    msg, category = users.remove_user_friend(db, user, name)

    flask.flash(msg, category)
    return flask.redirect(flask.url_for('login.index'))

@blueprint.route('/friend/<fname>')
def view_friend(fname):
    """View the page of a given friend."""
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You must be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))

    friend = users.get_user_by_name(db, fname)
    all_posts = posts.get_posts(db, friend)[::-1] # reverse order

    return flask.render_template('friend.html', title=copy.title,
            subtitle=copy.subtitle, user=user, username=username,
            friend=friend['username'],
            friends=users.get_user_friends(db, user), posts=all_posts)

# Path to return data about a user with username
@blueprint.route('/api/user/<username>', methods=['GET'])
def get_user(username):
    """Get the user's info."""
    db = helpers.load_db()

    user = users.get_user_by_name(db, username)
    if not user:
        return flask.make_response(flask.jsonify({'error': 'User not found.'}), 404)

    return flask.make_response(flask.jsonify(user), 200)