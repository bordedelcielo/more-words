from flask import Blueprint, render_template, request, redirect, url_for, flash, session
prod = Blueprint('prod', __name__, template_folder = 'my_words_templates')
from flask_login import login_required
from words_api.secrets import con, headers
cursor = con.cursor()

display = Blueprint('display', __name__, template_folder = 'display_words_templates')

@display.route('/displaywords')
@login_required
def displaywords():
    cursor.execute("select definition from public.word")
    result = cursor.fetchall()
    print(result)
    return render_template('display_words.html', data=result)