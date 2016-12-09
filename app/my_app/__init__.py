from flask import Flask
from my_app.hello.views import hello
from my_app.product.views import product

app = Flask(__name__)
app.register_blueprint(hello)
app.register_blueprint(product)
