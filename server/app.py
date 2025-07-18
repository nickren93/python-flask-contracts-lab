#!/usr/bin/env python3

#added make_response, jsonify imports:
from flask import Flask, request, current_app, g, make_response, jsonify

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]

app = Flask(__name__)

# main page route:
@app.route('/')
def index():
    return "<h1>Welcome to Contracts Manager home page!</h1>"

# contract page route:
@app.route('/contract/<int:id>')
def find_contract(id):
    for contract in contracts:
        if contract["id"] == id:
            return jsonify(contract), 200  # Return contract info with 200 status
        
    return make_response("Contract not found", 404)  # 404 Not Found

 # customer page route:   
@app.route('/customer/<customer_name>')
def find_customer(customer_name):
    if customer_name.lower() in customers:
        return "", 204   # 204 No Content
    return make_response("Customer not found", 404)  # 404 Not Found


if __name__ == '__main__':
    app.run(port=5555, debug=True)
