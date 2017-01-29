''' app main file '''
from flask import Flask
from common.database import Database

app = Flask(__name__)
app.config.from_object('config')


@app.before_first_request
def init_db():
    Database.initialize()

from models.users.views import userBlueprint
app.register_blueprint(userBlueprint, url_prefix="/users")
