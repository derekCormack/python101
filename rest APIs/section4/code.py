from flask import Flask, request
from flask_restful import Resource, Api   #flask_restfull handles jsonify!

app = Flask(__name__)
api = Api(app)
app.secret_key = 'jose'

items = []

class Item(Resource):   # this defines the resourse: student
    def get(self, name):    # this defines the METHODS
            # for item in items:
            #     if item['name'] == name:
            #         return item        #what the method will do when resourse is called.
            
            item = next(filter(lambda x: x['name'] == name, items), None)
            return {'item', item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists!".format(name)},400




        data = request.get_json()
        item ={'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get (self):
        return {'items':items}

api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')  #add the resourse and how it will be accesse

app.run(port=5000)   # runs the app!











# from flask import Flask, request
# from flask_restful import Resource, Api, reqparse
# from flask_jwt import JWT, jwt_required, current_identity

# from security import authenticate, identity

# app = Flask(__name__)
# app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
# app.secret_key = 'jose'
# api = Api(app)

# jwt = JWT(app, authenticate, identity)

# items = []

# class Item(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('price',
#         type=float,
#         required=True,
#         help="This field cannot be left blank!"
#     )

#     @jwt_required()
#     def get(self, name):
#         return {'item': next(filter(lambda x: x['name'] == name, items), None)}

#     def post(self, name):
#         if next(filter(lambda x: x['name'] == name, items), None) is not None:
#             return {'message': "An item with name '{}' already exists.".format(name)}

#         data = Item.parser.parse_args()

#         item = {'name': name, 'price': data['price']}
#         items.append(item)
#         return item

#     @jwt_required()
#     def delete(self, name):
#         global items
#         items = list(filter(lambda x: x['name'] != name, items))
#         return {'message': 'Item deleted'}

#     @jwt_required()
#     def put(self, name):
#         data = Item.parser.parse_args()
#         # Once again, print something not in the args to verify everything works
#         item = next(filter(lambda x: x['name'] == name, items), None)
#         if item is None:
#             item = {'name': name, 'price': data['price']}
#             items.append(item)
#         else:
#             item.update(data)
#         return item

# class ItemList(Resource):
#     def get(self):
#         return {'items': items}

# api.add_resource(Item, '/item/<string:name>')
# api.add_resource(ItemList, '/items')

# if __name__ == '__main__':
#     app.run(debug=True)  # important to mention debug=True