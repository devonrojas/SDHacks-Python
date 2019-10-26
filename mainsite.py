# cd ~/github/website
# FLASK_APP=mainsite.py FLASK_DEBUG=1 flask run

from flask import Flask, render_template, request
app = Flask(__name__)

def home_page():
    return render_template('home_page.html')
