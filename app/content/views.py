from flask import render_template
from app import app
from .models import Post
from datetime import datetime, timedelta


@app.route('/')
@app.route('/index')
@app.route('/fresh')
def fresh_post():
    posts = Post.query.order_by('created_time desc').all()
    post_array = []

    for i, post in enumerate(posts):
        if i > 10:
            break
        message_id = post.message_id
        page_post = message_id.split('_', 1)
        url = 'https://www.facebook.com/' + page_post[0] \
            + '/posts/' + page_post[1]
        post_array.append({'url': url})
    return render_template("index.html",
                           posts=post_array)


@app.route('/trend')
def trend_post():
    posts = Post.query.filter_by(trend=1) \
        .order_by('liked desc').all()
    post_array = []

    for i, post in enumerate(posts):
        if i > 10:
            break
        message_id = post.message_id
        page_post = message_id.split('_', 1)
        url = 'https://www.facebook.com/' + page_post[0] \
            + '/posts/' + page_post[1]
        post_array.append({'url': url})
    return render_template("index.html",
                           posts=post_array)


@app.route('/hot')
def hot_post():

    hot_time = datetime.utcnow() - timedelta(hours=15)

    posts = Post.query.filter(Post.created_time >= hot_time).all()
    post_array = []

    for i, post in enumerate(posts):
        if i > 10:
            break
        print datetime.now()
        print post.created_time
        message_id = post.message_id
        page_post = message_id.split('_', 1)
        url = 'https://www.facebook.com/' + page_post[0] \
            + '/posts/' + page_post[1]
        post_array.append({'url': url})
    return render_template("index.html",
                           posts=post_array)
