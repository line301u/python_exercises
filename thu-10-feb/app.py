from bottle import error, get, run, view, static_file, post, request, redirect

#####################################
# ROUTING SYSTEM
import signup_get               # GET
import home_get                 # GET
import login_get                # GET
import users_get                # GET
import items_get                # GET
import admin_get                # GET
import signup_ok_get            # GET

import delete_item_post         # POST
import login_post               # POST
import signup_post              # POST


#####################################
@get("/app.css")
def _():
    return static_file("app.css", root=".") 

#####################################
@error(404)
@view("404")
def _(error):
    print(error)
    return

#####################################

# Port from 0 to 65535
# Reserved from 0 to 1024

run(host="127.0.0.1", port=5555, debug=True, reloader=True)
