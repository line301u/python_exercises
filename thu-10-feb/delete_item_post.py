from bottle import get, post, request, redirect
import g

@post("/delete-item")
def _():
    # REMEMBER VALIDATION
    item_id = request.forms.get("item_id")
    for index, item in enumerate(g.ITEMS):
        if item["id"] == item_id:
            g.ITEMS.pop(index)
            return redirect("/items")

    return redirect("/items")
    
