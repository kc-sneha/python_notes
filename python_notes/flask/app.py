from flask import Flask

app = Flask(__name__) #creating an object of Flask with a particular name

@app.route('/') #creating a route or home page for our application
def home():
	return "hello world"

app.run(port =5000)
