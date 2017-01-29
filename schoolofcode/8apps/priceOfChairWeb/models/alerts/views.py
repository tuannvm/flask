from flask import Blueprint

alertBlueprint = Blueprint('alerts', __name__)

@alertBlueprint.route('/new', methods=['POST'])
def new_alert():
    pass

@alertBlueprint.route('/deactivate/<string:alertId>')
def deactivate_alert(alertId):
    pass

@alertBlueprint.route('/alerts')
def show_alerts():
    pass

