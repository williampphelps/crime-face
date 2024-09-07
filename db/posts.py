import time
import tinydb

# import emoji from './emoji.py' file

# import encode and decode from emoji.py
from db.emoji import encode, decode
from db.aes import encrypt


def add_post(db, user, text, password = ''):
    posts = db.table('posts')

    if (password != ''):
        # encrypt the post text
        encrypted = encrypt(text, password)
        text = encode(encrypted['cipher_text'])
    else:
        encrypted = { 'salt': '', 'iv': ''}

    print(text)
    print(encrypted)

    posts.insert({'user': user['username'], 'text': text, 'time': time.time(), 'salt': encrypted['salt'], 'iv': encrypted['iv']})

def get_posts(db, user):
    posts = db.table('posts')
    Post = tinydb.Query()
    post_list = posts.search(Post.user==user['username'])
    for post in post_list:
        post['id'] = post.doc_id
    return post_list

def get_post(db, postid):
    posts = db.table('posts')
    Post = tinydb.Query()
    return posts.get(doc_id=postid)


