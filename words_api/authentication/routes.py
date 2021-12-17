from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login.utils import login_required
from words_api.forms import UserSignupForm, UserLoginForm
from words_api.models import User, db
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user

auth = Blueprint('auth', __name__, template_folder = 'auth-templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserSignupForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data 
            username = form.username.data
            password = form.password.data

            user = User(email, username, password = password)

            db.session.add(user)
            db.session.commit()

            flash(f'You have successfully created a user account {username}', 'user-created')

            login()

            return redirect(url_for('site.home'))

    except:
        raise Exception('Invalid Form Data: Please check your form')
    return render_template('signup.html', form = form)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = UserLoginForm()

    try:
        if request.method =='POST' and form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            session["username"] = form.username.data

            logged_user = User.query.filter(User.username == username).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('Login successful!', 'auth-success')
                return redirect(url_for('site.home'))
            else:
                flash('Your username and/or password is incorrect', 'auth-failed')
                return redirect(url_for('auth.login'))
    except:
        raise Exception('Invalid Form Data: Please Check Your Form.')

    return render_template('login.html', form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('site.home'))