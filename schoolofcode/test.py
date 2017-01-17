'''import flask'''
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity

app = Flask(__name__)

stores = [
    {
        'name': 'test store',
        'items':
        [
            {
                'name': 'test product',
                'price': 20.00
            }
        ]
    }
]

@app.route('/store', methods=['POST'])
def create_store():
    '''create store'''
    requestData = request.get_json()
    newStore = {
        'name': requestData['name'],
        'items': []
    }
    stores.append(newStore)
    return jsonify(newStore)

@app.route('/store/<string:name>')
def get_store(name):
    '''get store'''
    #need to loop through the stores list
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'can not find ' + name + ' store'})

# get all store
@app.route('/store')
def get_all_store():
    '''get all store'''
    return jsonify({'stores': stores})

#post product in store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    '''create intem in store'''
    for store in stores:
        if store['name'] == name:
            requestData = request.get_json()
            newItem = {
                'name': requestData['name'],
                'price': requestData['price']
            }
            store['items'].append(newItem)
            return jsonify(store)
    return jsonify({'message': 'store not found!'})

#get product in store
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    '''get item in store'''
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found!'})

###

api = Api(app)
jwt = JWT(app, authenticate, identity)
app.secret_key = 'tuan'

items = []

class Item(Resource):
    '''item'''
    def get(self, name):
        '''get'''
        item = next(filter(lambda item: item['name'] == name, items), default=None)
        return item
        return {'item': None}, 200 if item else 404

    def post(self, name):
        '''post'''
        item = next(filter(lambda item: item['name'] == name, items), default=None)
        if item:
            return {'message': '{} already existed!'.format(name)}, 400
        postData = request.get_json()
        item = {
            'name': postData['name'],
            'price': postData['price']
        }
        items.append(item)
        return item, 201

class ItemList(Resource):
    ''' item list '''
    def get(self):
        ''' get '''
        return {"items": items}, 200

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
