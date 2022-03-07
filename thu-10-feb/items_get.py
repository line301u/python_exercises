from bottle import get, view
import g

@get("/items")
@view("items")
def _():
    return dict(items=g.ITEMS)
