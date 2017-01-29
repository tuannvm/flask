from app import app

app.run(port=6666, debug=app.config['DEBUG'])
