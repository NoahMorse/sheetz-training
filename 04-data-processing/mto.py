"""
Write a script that will:
    1. Add a new order that includes at least two items
    2. Replace the mozarella-sticks in Jane's classic-sample with jalapeno-popperz
    3. Write the updated order to a new file
    3. Total all four orders, print the result

"""
import json
from pprint import pprint

with open("mto.json") as file:
    orders = json.load(file)


# Adding a new order
orders["081"] = {
    "customer_name": ""
    "items": [
        {
            ...
        },
        {
            ...
        }
    ],
    "total_price": ...
    "order_status": ...

}



# Replacing Mozarella-sticks with Jalapeno-poppers
orders["079"]...  = "jalapeno-popperz"


# Totaling the orders
total = 0
for order in orders:
    ...


# Writing the updated order to a new file
with ...

print(total)


