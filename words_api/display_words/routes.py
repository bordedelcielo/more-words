from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from sqlalchemy import select
from words_api.models import Word, User, db
prod = Blueprint('prod', __name__, template_folder = 'my_words_templates')
from flask_login import login_required
from words_api.headers import headers

display = Blueprint('display', __name__, template_folder = 'display_words_templates')

@display.route('/displaywords')
@login_required
def displaywords():
    id = session["_user_id"]
    user = User.query.get(id)
    words = Word.query.filter_by(added_by_user = user.username)
    print(words[0].status)

    return render_template('display_words.html', words=words)

@display.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Word.query.get(id)
    # print(my_data)
    db.session.delete(my_data)
    db.session.commit()
    flash(f"Word deleted successfully")
    return redirect(url_for('display.displaywords'))

@display.route('/update/<id>', methods = ['GET', 'PUT'])
def update(id):
    my_data = Word.query.get(id)
    print(my_data)

    if my_data.status != "Learned":
        my_data.status = "Learned"
        # print(my_data.status)
        db.session.commit()
        flash('You have marked this word as "Learned", congratulations!')
    else:
        my_data.status = "Unlearned"
        # print(my_data.status)
        db.session.commit()
        flash('You have marked this word as "Unlearned."')

    return redirect(url_for('display.displaywords'))