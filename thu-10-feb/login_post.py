from bottle import get, post, request, redirect
import re
import g

@post("/login")
def _():
    # VALIDATE
    # FIRST THING: always chech if the varible was passed in the form
    if not request.forms.get("user_email"):
        return redirect("/login?error=user_email")
    if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
        return redirect("/login?error=user_email")

    user_email = request.forms.get("user_email") # create varible after validation
    if not request.forms.get("user_password"):
        return redirect(f"/login?error=user_password&user_email={user_email}")
    if len(request.forms.get("user_password")) < 6:
        return redirect(f"/login?error=user_password&user_email={user_email}")
    if len(request.forms.get("user_password")) > 50:
        return redirect(f"/login?error=user_password&user_email={user_email}")


# SUCCESS 
    for user in g.USERS:
        if user["email"] == user_email:
            if user["password"] == request.forms.get("user_password"):
                return redirect("/admin")

    return redirect("/login")