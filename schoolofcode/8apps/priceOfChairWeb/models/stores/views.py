from flask import Blueprint

storeBlueprint = Blueprint('stores', __name__)

@storeBlueprint.route('/store/<string:name>')
def store():
    pass
