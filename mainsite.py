# cd ~\Users\Andre\OneDrive\Documents\GitHub\SDHacks-Python
# FLASK_APP=mainsite.py FLASK_DEBUG=1 flask run

from flask import Flask, render_template, request
import requests
import json
import random
from datetime import datetime



"""
Item{"id", "name", "category", "price"}
"""
def add_item(item):
    description = item["name"]
    category = item["category"]
    price = item["price"]

    data = {"query": "mutation($item: ItemInput!) { addItem(item: $item) { id description category price } }",
    "variables": {"item": {"description": description, "category": category, "price": price}}}
    stringify = json.dumps(data)

    requests.post(url = "https://murmuring-lake-39323.herokuapp.com/graphql", data = stringify, headers={"content-Type": "application/json"})



"""
User{"id", "displayname", "username", "email", "password"}
"""
def add_user(user):
    id = user["id"]
    displayname = user["displayname"]
    username = user["username"]
    email = user["email"]
    password = user["password"]

    data = {"query": "mutation($user: UserInput!) { createUser(user: $user) { user { id } token  } }",
	"variables": {"user": {"displayName": displayname,"username": username,"password": password,"id": id,"email": email}}}

    stringify = json.dumps(data)

    requests.post(url = "https://murmuring-lake-39323.herokuapp.com/graphql", data = stringify, headers={"content-Type": "application/json"})



"""
Vendor{"id", "name", "category"}
"""
def add_vendor(vendor):
    name = vendor["name"]
    category = vendor["category"]

    data = {"query": "mutation($vendor: VendorInput!) { addVendor(vendor: $vendor) { id name category }}",
    "variables": {"vendor": {"name": name,"category": category}}}

    stringify = json.dumps(data)

    requests.post(url = "https://murmuring-lake-39323.herokuapp.com/graphql", data = stringify, headers={"content-Type": "application/json"})



"""
transaction{"student_id", "item_id", "vendor_id", quantity}
"""
def add_transaction(transaction):
    student_id = str(transaction["student_id"])
    item_id = str(transaction["item_id"])
    vendor_id = str(transaction["vendor_id"])
    qty = int(transaction["quantity"])

    data = {"query": "mutation($transaction: TransactionInput!) { addTransaction(transaction: $transaction) { id studentID itemID vendorID qty timestamp } }",
    "variables": {"transaction": {"studentID": student_id,"itemID": item_id,"vendorID": vendor_id,"qty": qty}}}

    stringify = json.dumps(data)

    requests.post(url = "https://murmuring-lake-39323.herokuapp.com/graphql", data = stringify, headers={"content-Type": "application/json"})





def calculate_CO2_emissions(dollars_spent, category, months):
    #source http://www.carbonglobe.com/carbon-footprint-formula.php
    gram_to_pound_conversion = .0022
    emmisions_factors = {"meatfisheggs": 1452,
                        "cerealsbakeryproducts": 741,
                        "dairy": 1911,
                        "fruitsvegetables": 1176,
                        "eatingout": 368,
                        "otherfoods": 467}
    CO2_emissions = (dollars_spent * emmisions_factors[category] * months) * gram_to_pound_conversion
    return CO2_emissions
