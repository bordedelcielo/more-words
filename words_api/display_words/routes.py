from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from words_api.models import Word, db
prod = Blueprint('prod', __name__, template_folder = 'my_words_templates')
from flask_login import login_required
from words_api.secrets import con, headers
cursor = con.cursor()

display = Blueprint('display', __name__, template_folder = 'display_words_templates')

@display.route('/displaywords')
@login_required
def displaywords():
    username = session["username"]
    # cursor.execute("select * from public.word")
    cursor.execute(f"select * from public.word where added_by_user = '{username}'")
    result = cursor.fetchall()
    # print(result)
    return render_template('display_words.html', data=result)

@display.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Word.query.get(id)
    print(my_data)
    db.session.delete(my_data)
    db.session.commit()
    flash(f"Word deleted successfully")
    return redirect(url_for('display.displaywords'))