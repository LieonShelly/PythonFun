from flask import Blueprint, redirect, render_template, request, url_for, flash
from Blog import db
from flask_login import login_required
from Blog.post.forms import PostForm
from flask_login import current_user
from Blog.post.models import Posts


post = Blueprint('post', __name__)


@post.route('/post/new', methods = ['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Posts(title = form.title.data, content = form.content.data, author = current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title="New Post",  form=form, legend = 'New Post')

@post.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Posts.query.get_or_404(post_id)
    return render_template('post.html', titile = post.title, post = post)

@post.route('/post/<int:post_id>/delete', methods = ['POST'])
def delete_post(post_id):
    post = Posts.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))

@post.route('/post/<int:post_id>/update', methods = ['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Posts.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post.post_detail', post_id = post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title = 'Update Post', form = form, legend = 'Update Post')
