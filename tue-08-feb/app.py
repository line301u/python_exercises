from bottle import run, get, response, request, post, delete
import json 
import uuid
import re

items = [
    {"id":"1", "name":"a"},
    {"id":"2", "name":"b"},
    {"id":"3", "name":"c"}
]


#####################################
# decorator
@get("/")
def _():
    return "home"

#####################################
@get("/items")
def _():
    return json.dumps(items)

#####################################
# every other varible after the 1st one starts with &
# 127.0.0.1:4444/test?id=1&name=a
# Query string = every thing from ? anf forward
@get("/test")
def _():
    user_name = "Linea"
    if not re.match("^[A-Za-z]*$", user_name):
        return "not a valid name"
    return "congrats"

    # user_phone = "12345678"
    # if not re.match("^[1-9][0-9]{7}$", user_phone): # true or false
    #     return "not a valid form"
        
    # return "congrats"

    # school_name = request.params.get("school-name")
    # year = request.params.get("year")
    # age = request.params.get("age")
    # return f"Hi, you are at {school_name}. The year is {year} and you are {age} years old"
    
#####################################
# Query string with a friendly URL
# 127.0.0.1:4444/friendly/brand/nike/color/red
@get("/friendly/brand/<brand>/color/<color>")
def _(brand, color):
    return f"You want for adidas: {brand} and the color is: {color}"

#####################################
@post("/items")
def _():

    # VALIDATION
    if not request.forms.get("item_name"):
        response.status = 400
        return "item name is missing"
    if len(request.forms.get("item_name")) < 2:
        response.status = 400
        return "item name must be at least 2 characters"
    if len(request.forms.get("item_name")) > 20:
        response.status = 400
        return "item name can not contain more than 20 characters"

    item_id = str(uuid.uuid4())
    item_name = request.forms.get("item_name")
    item_price = request.forms.get("item_price")
    item = {
        "id": item_id,
        "item_name": item_name,
        "item_price": item_price,
    }
    items.append(item)
    return f"id: {item_id} name: {item_name} price: {item_price}"

#####################################
@get("/items/<item_id>")
def _(item_id):

    # VALIDATION
    if not item_id:
        response.status = 400 
        return "item id is missing"
    for item in items:
        if item["id"] == item_id:
            return item

    response.status = 400
    return "item not found"

#####################################
@delete("/items/<item_id>")
def _(item_id):
    # VALIDATION (remember!!!)
    for index, item in enumerate(items):
        if item["id"] == item_id:
            items.pop(index)
            return item

    response.status = 400
    return "item not found"
    

#####################################


# Port from 0 to 65535
# Reserved from 0 to 1024

run(host="127.0.0.1", port=4444, debug=True, reloader=True)
