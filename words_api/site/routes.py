from flask import Blueprint, render_template, session, flash, request, redirect, url_for
from flask_login.utils import login_required
from words_api.models import User, db
from words_api.forms import UpdateEmail
from words_api.cursor import con
cursor = con.cursor()

site = Blueprint('site', __name__, template_folder = 'site-templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
@login_required
def profile():

    username = session["username"]
    # cursor.execute("select * from public.word")
    cursor.execute(f"select * from public.user where username = '{username}'")
    result = cursor.fetchall()
    # print(result)
    return render_template('profile.html', data=result)

@site.route('/update_email', methods = ['GET', 'POST'])
@login_required
def update_email():
    username = session["username"]
    cursor.execute(f"SELECT id FROM public.user where username = '{username}';")
    id = cursor.fetchone()
    print(id)
    my_data = User.query.get(id)
    print(my_data.email)
    form = UpdateEmail()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            my_data.email = form.email.data
            db.session.commit()
            flash(f'Your email address has been updated to {my_data.email} 🙂', 'user-created')
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