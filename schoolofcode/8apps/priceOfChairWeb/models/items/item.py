''' Item model '''
from common.general import BeautifulSoup, requests, regex, uuid4
from common.database import Database
import constants

class Item(object):
    def __init__(self, name, url, store, _id=None):
        self.name = name
        self.store = store
        self.url = url
        self.price = self.load_price(store.tagName, store.queryString)
        self._id = uuid4().hex if _id is None else _id

    def __repr__(self):
        return "Show item {} with url {}".format(self.name, self.url)

    def load_price(self, tagName, queryString):
        request = requests.get(self.url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")

        #find the value inside html tag, strip off the whitespace
        element = soup.find(tagName, queryString).text.strip()

        #define pattern to match against element
        pattern = regex.compile('([\d]+\.[\d]+\.[\d]+)')

        #return matched string, take the first group if multiple group found
        return pattern.search(element).group()

    def save_to_db(self):
        Database.insert(constants.COLLECTION, self.json())

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "url": self.url,
            "store": self.store,
            "price": self.price
        }
