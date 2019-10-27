from mainsite import *
from flask import Flask, render_template, request
import requests
import json
import random
from datetime import datetime

data = {"query": "mutation($transaction: TransactionInput!) { addTransaction(transaction: $transaction) { id studentID itemID vendorID qty timestamp } }",
"variables": {"transaction": {"studentID": "sid","itemID": "iid","vendorID": "vid","qty": 4}}}

stringify = json.dumps(data)

requests.post(url = "https://murmuring-lake-39323.herokuapp.com/graphql", data = stringify, headers={"content-Type": "application/json"})
