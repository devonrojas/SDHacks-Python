import 


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
