from flask import Blueprint, render_template, session, flash, request, redirect, url_for
from flask_login.utils import login_required
from words_api.models import User, db
from words_api.forms import UpdateEmail

site = Blueprint('site', __name__, template_folder = 'site-templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
@login_required
def profile():
    print(session)
    id = session["_user_id"]
    user = User.query.get(id)
    nameEmail = [user.username, user.email]
    return render_template('profile.html', data=nameEmail)
    # return render_template('profile.html')

@site.route('/update_email', methods = ['GET', 'POST'])
@login_required
def update_email():
    id = session["_user_id"]
    user = User.query.get(id)
    children_list = [element for element in user.children.all()]
    form = UpdateEmail()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            user.email = form.email.data
            db.session.commit()
            flash(f'Your email address has been updated to {user.email} 🙂', 'user-created')
            return redirect(url_for('site.home'))

    except:
        raise Exception('Invalid Form Data: Please check your form')

    return render_template('update_email.html', form = form)

# @site.route('/update_email/<id>', methods = ['GET', 'PUT'])
# def update_email(id):
#     username = session["username"]
#     form = UpdateEmail()
#     my_data = User.query.get(id)
#     my_data.email = form.email.data
#     db.session.commit()
#     flash(f'Email address successfully updated for {username}')