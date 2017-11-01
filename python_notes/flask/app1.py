from flask import Flask, jsonify,request

app = Flask(__name__)

stores = [
	{ 
		'name': 'snehaElec',
		'items': [
			{
			'name':'item_name',
			'price':49.99
}

]
}
]

#Note: POST is used to receive data and GET is used to send data from browsers point of view.


#POST /store data:{name:}
@app.route('/store', methods=['POST']) #Note:By default the method is 'GET' if nothing is mentioned.
def create_store():
	request_data = request.get_json()
	print(request_data)
	new_store = {
		'name':request_data['name'],
		'items':[]
	}
	stores.append(new_store)
	return jsonify(new_store)


#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify(store)
		else:
			return jsonify({'message':'store not found'})


#GET /store
@app.route('/store')
def get_stores():
	return jsonify({'stores': stores})


#POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
	request_data = request.get_json()
	for store in stores:
		if store['name'] == name :
			new_item = {
				'name':request_data['name'],
				'price':request_data['price']
			}
			store['items'].append(new_item)
			return jsonify(new_item)
	return jsonify({'message':'store not found'})


#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
	for store in stores:
		if store['name']== name:
			return jsonify({'items':store['items']}) 
	return jsonify({'message':'store not found'})



app.run(port=5000)


