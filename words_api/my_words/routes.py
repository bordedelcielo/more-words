from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login.utils import login_required
import requests
from words_api.forms import AddWordForm
from words_api.headers import headers
from words_api.models import Word, db

prod = Blueprint('prod', __name__, template_folder = 'my_words_templates')

@prod.route('/mywords', methods = ['GET', 'POST'])
@login_required
def mywords():
    username = session["username"]
    form = AddWordForm()

    try:
        if request.method == 'POST':
            word = form.word.data
            url = f"https://lingua-robot.p.rapidapi.com/language/v1/entries/en/{word}"
            response = requests.request("GET", url, headers=headers)

            if response.status_code == 200:

                definition = response.json()["entries"][0]["lexemes"][0]["senses"][0]["definition"]
                added_by_user = username

                entry = Word(word, definition, added_by_user)

                db.session.add(entry)
                db.session.commit()

                flash(f"{word.title()} added to {added_by_user}'s word list. {word.title()}: {definition}", 'user-created')
            else:
                flash(f'The word \'{word}\' did not appear in our search. Please check the spelling of the word you entered or try another word.')

    except:
        # raise Exception('Invalid Form Data: Please check your form')
        flash(f'The word \'{word}\' did not appear in our search. Please check the spelling of the word you entered or try another word.')

    return render_template('mywords.html', form = form)