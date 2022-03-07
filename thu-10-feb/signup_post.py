from bottle import get, post, request, redirect
import uuid
import g

@post("/signup")
def _():
    # VALIDATE
    if not request.forms.get("user_email"):
        return "missing user_email"
    user_id = str(uuid.uuid4())
    user_email = request.forms.get("user_email")
    user_first_name = request.forms.get("user_first_name")
    user_last_name = request.forms.get("user_last_name")
    user_password = request.forms.get("user_password")
    user = {"id":user_id, "email":user_email, "first_name":user_first_name, "last_name": user_last_name, "password": user_password}
    g.USERS.append(user)
    return redirect(f"signup-ok?user-email={user_email}&user-first-name={user_first_name}&user-last-name={user_last_name}")

