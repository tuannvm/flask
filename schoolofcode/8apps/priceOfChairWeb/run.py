from app import app

app.run(host="0.0.0.0", port=6666, debug=app.config['DEBUG'])
