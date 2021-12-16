from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login.utils import login_required
from words_api.secrets import con, headers
import requests
from words_api.forms import AddWordForm
from words_api.secrets import headers
from words_api.models import Word, db

cursor = con.cursor()

prod = Blueprint('prod', __name__, template_folder = 'my_words_templates')

@prod.route('/mywords', methods = ['GET', 'POST'])
@login_required
def mywords():
    username = session["username"]
    form = AddWordForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            word = form.word.data
            url = f"https://lingua-robot.p.rapidapi.com/language/v1/entries/en/{word}"
            response = requests.request("GET", url, headers=headers)
            definition = response.json()["entries"][0]["lexemes"][0]["senses"][0]["definition"]
            added_by_user = username
            # print(definition)

            entry = Word(word, definition, added_by_user) # needs a user token passed in. The Matas 100% guarantee.

            db.session.add(entry)
            db.session.commit()

            flash(f"{word.title()} added to {added_by_user}'s word list. {word.title()}: {definition}.", 'user-created')

    except:
        raise Exception('Invalid Form Data: Please check your form')

    return render_template('mywords.html', form = form)

# @prod.route('/mywords')
# @login_required
# def viewmywords():
#     cursor.execute("select definition from public.word")
#     result = cursor.fetchall()
#     print(result)
#     return render_template('mywords.html', data=result)

    # try:
    #     if request.method == 'POST' and form.validate_on_submit():
    #         username = form.username.data