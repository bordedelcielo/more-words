from flask import Blueprint, render_template, request, redirect, url_for, flash
from words_api.forms import UserSignupForm
from words_api.models import User, db

auth = Blueprint('auth', __name__, template_folder = 'auth-templates')

@auth.route('/signup')
def signup():
    form = UserSignupForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            username = form.username.data
            password = form.password.data


            user = User(username, password = password)

            db.session.add(user)
            db.session.commit()

            flash(f'You have successfully created a user account {username}', 'user-created')

            return redirect(url_for('site.home'))

    except:
        raise Exception('Invalid Form Data: Please check your form')
    return render_template('signup.html', form = form)