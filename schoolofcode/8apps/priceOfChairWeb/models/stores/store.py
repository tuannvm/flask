from common.general import uuid4
from common.database import Database
import constants

class Store(object):
    def __init__(self, name, urlPrefix, tagName, queryString, _id=None):
        self.name = name
        self.urlPrefix = urlPrefix
        self.tagName = tagName
        self.queryString = queryString
        self._id = uuid4().hex if _id is None else _id

    #def __repr__(self):
    #    return "Show Store {} with prefix {}".format(self.name, self.urlPrefix)

    def save_to_db(self):
        Database.insert(constants.COLLECTION, self.json())

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "urlPrefix": self.urlPrefix,
            "tagName": self.tagName,
            "queryString": self.queryString
        }

    @classmethod
    def get_by_id(cls, _id):
        return cls(**Database.find_one(constants.COLLECTION, {"_id": _id}))

    @classmethod
    def get_by_name(cls, name):
        return cls(**Database.find_one(constants.COLLECTION, {"name": name}))

    @classmethod
    def get_by_url_prefix(cls, urlPrefix):
        return cls(**Database.find_one(constants.COLLECTION, {"urlPrefix": {"$regex" : '^{}'.format(urlPrefix)}}))
