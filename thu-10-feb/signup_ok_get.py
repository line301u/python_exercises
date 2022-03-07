from bottle import get, view, request, redirect

# query string expected with email
@get("/signup-ok")
@view("signup-ok")
def _():
    user_email = request.params.get("user-email")
    user_first_name = request.params.get("user-first-name")
    user_last_name = request.params.get("user-last-name")
    user_password = request.params.get("user-password")
    return dict(user_email=user_email, user_first_name=user_first_name, user_last_name=user_last_name, user_password=user_password)

