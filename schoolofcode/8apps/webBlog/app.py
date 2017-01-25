''' main app '''
from flask import Flask, render_template, request, session
from models.user import User
from common.database import Database

app = Flask(__name__)
app.secret_key = 'tuan'

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/login')
def login_landing():
    ''' hello route '''
    return render_template('login.html')

@app.route('/register')
def register_landing():
    ''' hello route '''
    return render_template('register.html')

@app.route('/auth/login', methods=['POST'])
def login():
    ''' login route '''
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
        return render_template('profile.html', email=session['email'])
    return render_template('login.html')

@app.route('/auth/register', methods=['POST'])
def register():
    ''' register route '''
    email = request.form['email']
    password = request.form['password']
    if User.find_by_email(email):
        return "user already registered!"
    User.register(email, password)
    return render_template('profile.html', email=session['email'])

@app.route('/blogs/<string:userId>')
@app.route('/blogs')
def user_blogs(userId=None):
    if userId is not None:
        user = User.find_by_id(userId)
    else:
        user = User.find_by_email(session['email'])
    blogs = user.get_blogs()
    return render_template('blogs.html', blogs=blogs, email=user.email)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
