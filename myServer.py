from flask import Flask, url_for, redirect, request, abort, jsonify, render_template, session
#import requests
import datetime
app = Flask(__name__, static_url_path='', static_folder='staticpages')
from yourDAO import class_instance
url = "http://127.0.0.1:5000/"


dishes = [
    {"id":1, "Name": "Onion Bhajee", "Category":"Starter", "Price":6},
    {"id":2, "Name": "Veg Samosa", "Category":"Starter", "Price": 4.50},
    {"id":3, "Name": "Lamb Biriyani", "Category":"Main", "Price": 15},
    {"id":4, "Name": "Vegetable Madras, Pilau Rice", "Category":"Main", "Price": 12.50},
    {"id":5, "Name": "Chicken Tikka Masala, Boiled Rice", "Category":"Main", "Price":14},
    {"id":6, "Name": "Chicken Rogan Josh, Pilau Rice", "Category":"Main", "Price":14},
    {"id":7, "Name": "Lamb Balti, Boiled Rice", "Category":"Main", "Price":14.80},
    {"id":8, "Name": "Lamb Vindaloo, Naan Bread", "Category":"Main", "Price":15.30},
    {"id":9, "Name": "Kulfi Ice Cream", "Category":"Dessert", "Price":7}
]


nextID = 10

@app.route('/publicMenu')
def viewMenuOnWebpage():
    if not 'username' in session:
        abort(401)
    else:
        render_template('menu1.html', utc_dt = datetime.datetime.utcnow())



@app.route('/menu')
def viewMenuOnWebpage():
    if not 'username' in session:
        abort(401)
    else:
        render_template('myMenuViewer.html', utc_dt = datetime.datetime.utcnow())



@app.route('/menu/<int:id>')
def getID(id):
    foodItem = class_instance.findByID(id)
    return jsonify(foodItem)
    

@app.route('/menu/display/<int:id>')
def orderByID(id):
    for dish in dishes:
        for id, name, category, price in dish.items():
            return jsonify(name)



@app.route('/menu/display')
def getAll2():
    for dish in dishes:
        for id, name, category, price in dish.items():
            return jsonify(category, name, str(price) + " euro")



@app.route('/menu/<name>', methods=['GET'])
def orderADish(name):
    if not 'usename' in session:
        abort(401)
    else:
        ip_addr = request.remote_addr
        data = (id, ip_addr)
        order = class_instance.order_food(data)
        return jsonify({order})



@app.route('/menu/new', methods=["POST"])
def createNewDish():
    global nextID
    dish = {
        "id":nextID,
        "Name":"Chicken Curry and Rice",
        "Price": 12.50
    }
    dishes.append(dish)
    nextID += 1
    return jsonify(dish)



@app.route('/menu', methods=["PUT"])
def updateItem(id):
    found_dishes = list(filter(lambda t: t["id"] == id, dishes))
    if len(found_dishes) == 0:
        abort(401)
    currentItem = found_dishes[0]
    if "Name" in request.json:
        currentItem["Name"] == request.json["Name"]
    if "Category" in request.json:
        currentItem["Category"] == request.json["Category"]
    if "Price" in request.json:
        currentItem["Price"] == request.json["Price"]
    return jsonify(currentItem)


@app.route('/menu/<int:id>', methods=["DELETE"])
def delete(id):
    foundItems = list(filter(lambda t: t["id"] == id, dishes))
    if len(foundItems) == 0:
        abort(401)
    dishes.remove(foundItems[0])
    return jsonify({"done": True})


@app.route('/')
def index():
    count = 0
    if not 'counter' in session:
        session['counter'] = 0
    else:
        count = session['counter']
        count += 1
        session['counter'] = count
    return str(count)


@app.route('/login')
def login():
    return '<h2>Login</h2> '+\
        '<button>'+\
            '<a href="'+url_for('process_login')+'">' +\
                'login' +\
            '<a>' +\
        '<button>'


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect('home')

if __name__ == "__main__":
    app.run(debug=True)