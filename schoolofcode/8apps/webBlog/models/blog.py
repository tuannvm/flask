import uuid
import datetime
from common.database import Database
from models.post import Post

class Blog(object):

    def __init__(self, title, description, author, authorId, createdDate=datetime.datetime.utcnow(), _id=None):
        self.title = title
        self.description = description
        self.author = author
        self.authorId = authorId
        self._id = uuid.uuid4() if _id is None else _id
        self.createdDate = createdDate

    def new_post(self, title, content, date=datetime.datetime.utcnow()):
        ''' create new post inside blog model'''
        post = Post(blogId=self._id,
                    title=title,
                    content=content,
                    createdDate=date,
                    author=self.author)
        post.save_to_mongo()

    def get_post(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert('blogs', self.json())

    def json(self):
        return {
            '_id': self._id,
            'author': self.author,
            'authorId': self.authorId,
            'description': self.description,
            'title': self.title,
            'createdDate': self.createdDate
        }
    
    @classmethod
    def find_by_id(cls, _id):
        blogData = Database.find_one(collection='blogs', query={'_id': _id})
        return cls(**blogData)

    @classmethod
    def find_by_author_id(cls, authorId):
        ''' find by author id '''
        blogs = Database.find("blogs", {'authorId': authorId})
        return [cls(**blog) for blog in blogs]
