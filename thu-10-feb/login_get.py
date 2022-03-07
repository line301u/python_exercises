from bottle import get, view, request

# query string will be used in this route
# Eg: /login=error=user_email
# Eg: /login=error=user_password
@get("/login")
@view("login")
def _():
    user_email = request.params.get("user_email")
    error = request.params.get("error")
    return dict(error=error, user_email=user_email)
