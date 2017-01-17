''' security module '''
from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'tuannvm', '123456')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}
'''
username_mapping = {'bob': {
        'id': 1,
        'username': 'tuannvm',
        'password': '123456'
    }
}
'''



'''
userid_mapping = {'1': {
        'id': 1,
        'username': 'tuannvm',
        'password': '123456'
    }
}
'''

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    userId = payload['identity']
    return userid_mapping.get(userId, None)

