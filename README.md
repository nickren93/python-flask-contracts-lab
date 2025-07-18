# Contractors Flask Application

---

## Overview

This is a simple flask website application for a company that manages contracts between
two parties. User can access the page by using URL: http://127.0.0.1:5555/

---

## Routes

### Route 1: contract route

User can obtain contract API information by manually adding the contract id in the URL, 
"/contract/1" for example, if the contract id is indeed a valid id of an existing contract. 
![Sample contract page](/screenshot/contract_routing.png)
However, if user input an invalid id which does not belong to any existing 
contract, a 404 error message would be shown on the page.

---

### Route 2: Customer route

The customer information is secured, so user can not obtain anything by manually adding the 
customer name in the URL, "/customer/jack" for example, if the customer name is indeed a valid 
name of an existing customer. However, if user input a name which does not belong to an existing 
customer, a 404 error message would be shown on the page. ![Sample contract page](/screenshot/customer_routing.png)


