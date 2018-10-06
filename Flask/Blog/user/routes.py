from flask import Flask, render_template, Response, redirect, flash, url_for, request, abort, Blueprint
from flask_login import current_user, login_user, logout_user, login_required, logout_user
from Blog.user.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from Blog.post.forms import PostForm
from Blog.user.models import User
from Blog import bcrypt, db
from Blog.post.models import Posts
import secrets
import os, json
from PIL import Image
from Blog.user.utls import save_picture, sende_email

user = Blueprint('user', __name__)

@user.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Posts.query.filter_by(author=user).order_by(Posts.date_posted.desc()).paginate(page = page, per_page = 5)
    return render_template('user_posts.html', posts=posts, user=user)


@user.route("/rest_password", methods=['GET', 'POST'])
def rest_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        sende_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect('user.login')
    return render_template('reset_request.html', title = "Reset Password", form=form)


@user.route("/rest_password/<string:token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_passwor = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_passwor
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('user.login'))
    return render_template('reset_token.html', title='Rest Password', form=form)



@user.route('/register', methods=["GET", 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_passwor = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email = form.email.data, password=hashed_passwor)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('user.login'))
    return render_template('register.html', title="register", form=form)


@user.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('main.home')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title="login", form=form)

@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@user.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('user.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', 
                            title='account', 
                            image_file=image_file,
                                form=form)
