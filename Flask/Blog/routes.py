from flask import Flask, render_template, Response, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from Blog.Forms import RegistrationForm, LoginForm
from Blog.Models import User
from Blog import app

@app.route('/')
@app.route('/home')
def home():
    print('______')
    return "home page"

@app.route('/about')
def about():
    render_template('about.html', title="About")

@app.route('/register', methods=["GET", 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_passwor = bcrypt.generate_password_hash(form.password.data).decode('urf-8')
        user = User(username=form.username.data, email = form.email.data, password=hashed_passwor)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for='login')
    return render_template('register.html', title="register", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
#     if current_user.is_authenticated:
#         return redirect('home')
    form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.fliter_by(email=form.email.data).first()
#         if user and bcrypt.check_password_hash(user.password, form.password.data):
#             login_user(user, remember=form.remember.data)
#             next_page = request.args.get('next')
#             return redirect(next_page) if next_page else redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title="login", form=form)


