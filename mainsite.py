# cd ~\Users\Andre\OneDrive\Documents\GitHub\SDHacks-Python
# FLASK_APP=mainsite.py FLASK_DEBUG=1 flask run


from flask import Flask, render_template, request
app = Flask(__name__)

import requests
import json
import random


#Home Page
@app.route('/')
@app.route('/Home')
def home_page():
    return render_template('home_page.html')

@app.route('/admin')
def admin_page():
    return render_template('admin_main_page.html')

@app.route('/vendor')
def vendor_page():
    return render_template('vendor_main_page.html')



gram_to_pound_conversion = .0022
emmisions_factors = {"meatfisheggs": 1452,
                    "cerealsbakeryproducts": 741,
                    "dairy": 1911,
                    "fruitsvegetables": 1176,
                    "eatingout": 368,
                    "otherfoods": 467,
                    }

#source http://www.carbonglobe.com/carbon-footprint-formula.php
def calculate_CO2_emissions(dollars_spent, category, months):
    CO2_emissions = (dollars_spent * emmisions_factors[category] * months) * gram_to_pound_conversion
    return CO2_emissions

def get_dollars_spent_by_category(category):
    response = requests.get("INSERT URL HERE")
    response


users = []
def generate_users(amount):
    for i in range(amount):
        user = {"id": i, "Username": f"username{i}", "email": f"email{i}", "password": f"password{i}"}
        users.append(user)
    #print(users)

items = []
dozen_eggs = {"id": 0, "name": "DozenEggs", "type": "meatfisheggs", "price": 3.99}
ham = {"id": 1, "name": "Ham", "type": "meatfisheggs", "price": 5.99}
bread = {"id": 2, "name": "WhiteBread", "type": "cerealsbakeryproducts", "price": 1.99}
milk = {"id": 3, "name": "milk", "type": "dairy", "price": 3.00}
apple = {"id": 4, "name": "Apple", "type": "fruitsvegetables", "price": 1.50}
pizza = {"id": 5, "name": "DominosPizza", "type": "eatingout", "price": 12.99}
sauce = {"id": 6, "name": "ChiliSauce", "type": "otherfoods", "price": 1.99}
items.append(dozen_eggs)
items.append(ham)
items.append(bread)
items.append(milk)
items.append(apple)
items.append(pizza)
items.append(sauce)

vendors = []
McDonalds = {"id": 1, "name": "Subway", "type": "FastFood"}
Vons = {"id": 2, "name": "Vons", "type": "GrocceryStore"}
vendors.append(McDonalds)
vendors.append(Vons)



transactions = []
def generate_transactions(amount):
    generate_users(amount)
    for i in range(amount):
        random_user_id = random.choice(users)["id"]
        random_item_id = random.choice(items)["id"]
        random_quantity = random.randint(1,9)
        random_vendor = random.choice(vendors)
        random_timestamp = random.randint(1,3)
        transaction = {"transaction_id": i,
                        "user_id": random_user_id,
                        "item_id": random_item_id,
                        "quantity": random_quantity,
                        "vendor_id": random_vendor,
                        "timestamp": random_timestamp,
                        }
        transactions.append(transaction)
    print(transactions)

generate_transactions(5)
