import flask

from db import posts, users, helpers
from db.emoji import encode, decode
from db.aes import decrypt

blueprint = flask.Blueprint("posts", __name__)

@blueprint.route('/post', methods=['POST'])
def post():
    """Creates a new post."""
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))

    post = flask.request.form.get('post')
    password = flask.request.form.get('password')
    posts.add_post(db, user, post, password)

    return flask.redirect(flask.url_for('login.index'))

@blueprint.route('/api/posts', methods=['GET'])
def get_posts():
    """Get all posts for users feed. """
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    # get the info for the user's feed
    friends = users.get_user_friends(db, user)
    all_posts = []
    for friend in friends + [user]:
        all_posts += posts.get_posts(db, friend)
    # sort posts
    sorted_posts = sorted(all_posts, key=lambda post: post['time'], reverse=True)

    return flask.make_response(flask.jsonify({'posts': sorted_posts}), 200)

@blueprint.route('/api/posts', methods=['POST'])
def create_post():
    """Creates a new post."""
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        return flask.make_response(flask.jsonify({'error': 'You need to be logged in to do that.'}), 401)

    content = flask.request.json
    post = content.get('content')
    postpassword = content.get('password')
    posts.add_post(db, user, post, postpassword)

    return flask.make_response(flask.jsonify({'success': 'Post created successfully!'}), 200)

@blueprint.route('/api/posts/decrypt', methods=['POST'])
def decrypt_post():
    """Decrypts a post."""
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        return flask.make_response(flask.jsonify({'error': 'You need to be logged in to do that.'}), 401)

    content = flask.request.json
    postid = content.get('id')

    print(postid)
    postpassword = content.get('password')
    post = posts.get_post(db, postid)
    if post is None:
        return flask.make_response(flask.jsonify({'error': 'Post not found.'}), 404)


    enc = {
        'cipher_text': post['text'],
        'salt': post['salt'],
        'iv': post['iv']
    
    }
    enc['cipher_text'] = decode(enc['cipher_text'])
    decrypted = decrypt(enc, postpassword)

    return flask.make_response(flask.jsonify({'content': decrypted}), 200)