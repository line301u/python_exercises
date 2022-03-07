from bottle import run, get, view, post, request, response, redirect
import uuid
import jwt
import time

cookie_secret = "this is a secret key"
sessions = [1, 2, 3 , 4, 5]

##############################
@get("/login")
@view("login")
def _():
    return

##############################
@get("/logout")
def _():
    user_session_id = request.get_cookie("uuid4")
    sessions.remove(user_session_id)
    return redirect("/login")

##############################
@get("/admin")
@view("admin")
def _():
    user_session_id = request.get_cookie("uuid4")
    # compare the uuid from the cookie to the uuid from sessions
    if user_session_id not in sessions:
        return redirect("/login")
    user_email = request.get_cookie("user_email", secret=cookie_secret)
    jwt = request.get_cookie("jwt", secret=cookie_secret)
    return dict(user_email=user_email)


##############################
@post("/login")
def _():
    # VALIDATION
    user_email = request.forms.get("user_email")
    user_session_id = str(uuid.uuid4())
    sessions.append(user_session_id)
    response.set_cookie("uuid4", user_session_id)
    user = {
        "user_email" : user_email,
        "iat" : int(time.time())
    }
    encoded_jwt = jwt.encode(user, cookie_secret, algorithm="HS256")
    response.set_cookie("jwt", encoded_jwt)
    return redirect("/admin")


##############################

# Port from 0 to 65535
# Reserved from 0 to 1024

run(host="127.0.0.1", port=3333, debug=True, reloader=True)