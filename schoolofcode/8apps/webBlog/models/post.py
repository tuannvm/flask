import uuid
import datetime
from common.database import Database

class Post(object):

    def __init__(self, blogId, title, content, author, createdDate=datetime.datetime.utcnow(), _id=None):
        self.blogId = blogId
        self.title = title
        self.content = content
        self.author = author
        self._id = uuid.uuid4().hex if _id is None else _id
        self.createdDate = createdDate

    def save_to_mongo(self):
        Database.insert('posts', self.json())

    def json(self):
        return {
            'blogId': self.blogId,
            '_id': self._id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'createdDate': self.createdDate
        }

    @classmethod
    def get_from_mongo_by_id(cls, _id):
        postData = Database.find_one(collection='posts', query={'_id': _id})
        return cls(**postData)


    @staticmethod
    def from_blog(blogId):
        return [post for post in Database.find(collection='posts', query={'blogId': blogId})]
