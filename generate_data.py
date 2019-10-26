import random
from mainsite import *



users = []
def generate_users(amount):
    for i in range(amount):
        user = {"id": f"{i}", "displayname": f"displayname{i}", "username": f"username{i}", "email": f"email{i}", "password": f"password{i}"}
        users.append(user)

generate_users(5)

def addusers():
    for user in users:
        add_user(user)
        print("Added: " + str(user))

addusers()



items = []
dozen_eggs = {"id": 0, "name": "DozenEggs", "category": "meatfisheggs", "price": 4}
ham = {"id": 1, "name": "Ham", "category": "meatfisheggs", "price": 6}
bread = {"id": 2, "name": "WhiteBread", "category": "cerealsbakeryproducts", "price": 1}
milk = {"id": 3, "name": "milk", "category": "dairy", "price": 3}
apple = {"id": 4, "name": "Apple", "category": "fruitsvegetables", "price": 2}
pizza = {"id": 5, "name": "DominosPizza", "category": "eatingout", "price": 13}
sauce = {"id": 6, "name": "ChiliSauce", "category": "otherfoods", "price": 2}
items.append(dozen_eggs)
items.append(ham)
items.append(bread)
items.append(milk)
items.append(apple)
items.append(pizza)
items.append(sauce)

def additems():
    for item in items:
        add_item(item)
        print("Added: " + str(item))

#additems()



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
