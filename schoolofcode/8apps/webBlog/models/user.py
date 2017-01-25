from common.database import Database
from models.blog import Blog
from models.post import Post
from uuid import uuid4
from flask import session
import datetime

class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid4().hex if _id is None else _id

    @classmethod
    def find_by_email(cls, email):
        ''' find by email '''
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def find_by_id(cls, _id):
        data = Database.find_one("users", {"_id": _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        user = User.find_by_email(email)
        if user is not None:
            return user.password == password
        return False

    @classmethod
    def register(cls, email, password):
        user = cls.find_by_email(email)
        if user is not None:
            return False
        newUser = cls(email, password)
        newUser.save_to_mongo()
        session['email'] = email

    @staticmethod
    def login(email):
        #after pass login_valid
        session['email'] = email

    @staticmethod
    def logout():
        session['email'] = None

    def get_blogs(self):
        blogs = Blog.find_by_author_id(self._id)
        if blogs is not None:
            return blogs
        

    def new_blog(self, title, description):
        ''' create new blog '''
        #title, description, author, authorId, createdDate=datetime.datetime.utcnow(), _id=None
        blog = Blog(title, description, self.email, self._id)
        blog.save_to_mongo()

    @staticmethod
    def new_post(blogId, title, content, createdDate=datetime.datetime.utcnow()):
        ''' create new post '''
        #blogId, title, content, author, createdDate=datetime.datetime.utcnow(), _id=None
        blog = Blog.find_by_id(blogId)
        blog.new_post(title, content, createdDate)

    def save_to_mongo(self):
        Database.insert("users", self.json())

    def json(self):
        return {
            '_id': self._id,
            'email': self.email,
            'password': self.password
        }
        