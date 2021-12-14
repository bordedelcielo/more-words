# from flask import Blueprint
# from words_api.helpers import token_required



# api = Blueprint('api', __name__, url_prefix = '/api')

# @api.route('/getdata')
# @token_required
# def getdata(current_user_token):
#     return { 'some': 'value' }

# @api.route('/words', methods = ['POST'])
# @token_required
# def create_hero(current_user_token):
#     name = 