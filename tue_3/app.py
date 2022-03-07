from bottle import get, run, static_file, view


# dictionary 
person = {
    "id": "1",
    "first_name": "Linea",
    "last_name" : "Lindebjerg"
}

##############################
@get("/app.css")
def _():
    return static_file("app.css", root=".")


##############################
@get("/person/<person_id>")
def _(person_id):
    # person["last_name"] = "Lindebjerg"
    return person_id

##############################
@get("/person/<first_name>/<last_name>")
def _(first_name, last_name):
    return f"Hi {first_name} {last_name}."


##############################

@get("/") # if someone inters the root, show (@view) this page
@view("index.html")
def _():
    return

##############################

@get("/items")
@view("items") # items.html
def _():
    letters = ["a", "b", "c", "x"]
    return "yes" if "x" in letters else "no" # ternary 

    # print(type(letters))
    # print(dir(letters))
    # is_b_in_list = "no"
    # if "b" in letters: is_b_in_list = "yes"
    # return is_b_in_list
    # print(letters)
    # return letters

##############################

@get("/item")
def _():
    name = "Linea" # string
    year = 2022 # iteger
    return f"Hi {name} the year is {year}" # f string (like back ticks in javascript = `${}`)

    # return "Hi " + name + " it is " + str(year) NOT DO LIKE THIS, DO THIS ^^
    # return str(year) # type-cast or cast (converterting number into string)

##############################

# Port from 0 to 65535
# Reserved from 0 to 1024

run(host="127.0.0.1", port=3333, debug=True, reloader=True)
