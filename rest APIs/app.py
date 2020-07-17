from flask import Flask, jsonify request #,render_template
#Flask=class, jsonify(lowercase)=METHOD
#rest apis usually return TEXT!
#we have imported flask
#created an object called app
#created a root called "/"
#assigned a method to it....that has to return something.
# important--- JSON--one key called stores:  dictionaries are NOT ordered! they are sets.
# REST API returns JSON, good for mobile app,  JSON - alway use ""!!! never single   JSON always must start with a Dictionary! never 
# a list only!    

dictionary with 
app = Flask(__name__)  

stores = [
{ 'name': 'My wonderfull store',
    'items': [
        {
            'name': 'My Item',
            'price': 15.99
        }]
}
]



# in here we think of being a server!
# POST - used to recieve data
# GET - used to send data back only

#BROWSERS ONLY DO GET REQUESTS!

# we will
#POST /store data: {name:}


@app.route('/store', methods=['POST'])
def create_store():
        request_data = request.get_json()
        new_store = {
                'name': request_data['name'],
                'items': []

        }
        stores.append(new_store)
        return jsonify(new_store)



#GET /store/<string:name>
@app.route('/store/<string:name>') # http://127.0.0.1:5000/store/some_name
def get_store(name):
        pass
#iterate over stores
  for store in stores:
          if store['name'] == name:
                  return jsonify({'message' : 'store not found'})


#if the store name matches, return it
#if none match, return error





#GET /store

@app.route('/store')
def get_stores():
        return jsonify({'stores': stores}) #key=stores  :  object: list of "stores"



#POST /store/<string:name>/item {name:, price:}

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
        for store in stores:
                if store['name'] == name:
                        new_item ={
                                'name': request_data['name'],
                                'price': request_data['price']
                        }
                store ['items'].append(new_item)
                return jsonify(new_item)
        return jsonify({'message':' store not found'})


#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
       for store in stores:
               if store['name'] == name:
                       return jsonify({'items': store['items']})
        return jsonify({'message' : 'store not found'})

app.run(debug=True,port=5000)