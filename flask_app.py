from flask import Flask
from flask import request
import requests
app = Flask(__name__)
import json
import green_grocer
import sys 

#url of receipt image is sent via POST request 

@app.route('/recieve_receipt', methods=["POST", "GET"])
def post():
    
    if request.method == "POST":
        body = request.get_json()
        green_grocer.main(body["url"])
        return('success')

    else:
        return('failure')    

    return 'posting here'

@app.route('/')
def hello_world():

    return 'Hello World!'


