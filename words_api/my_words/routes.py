from flask import Blueprint, render_template
from flask_login.utils import login_required
from words_api.secrets import con

cursor = con.cursor()

prod = Blueprint('prod', __name__, template_folder = 'my_words_templates')

@prod.route('/mywords')
@login_required
def mywords():
    cursor.execute("select * from public.user")
    result = cursor.fetchall()
    return render_template('mywords.html', data=result)