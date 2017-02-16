from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    #return "Hello World!"
    return render_template('home.html')
    
@app.route("/birthday")
def birthday():
    return 'January 10 1997'
    
@app.route("/greeting")
def greet():
    return 'Hello John Doe!'
    
@app.route("/greeting/<name>")
def greeting(name):
    return "Hello {}!".format(str(name))

@app.route("/add/<int:num1>/<int:num2>")
def addition(num1,num2):
    _sum = num1 + num2
    strsum = str(_sum)
    return strsum

@app.route("/subtract/<int:num1>/<int:num2>")
def subtraction(num1,num2):
    _sub = num1 - num2
    strsub = str(_sub)
    return strsub

@app.route("/multiply/<int:num1>/<int:num2>")
def multiplication(num1,num2):
    _product = num1 * num2
    strproduct = str(_product)
    return strproduct
	
@app.route("/favoritefoods")
def favoritefoods():
	myList = ["cheesecake","lasagna","pizza"]
	return jsonify(myList)