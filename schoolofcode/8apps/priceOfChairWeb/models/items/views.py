from flask import Blueprint

itemBlueprint = Blueprint('items', __name__)

@itemBlueprint.route('/item/<string:name>')
def page_item():
    pass

@itemBlueprint.route('/load')
def load_item():
    ''' load item data and return json representation '''
    pass
