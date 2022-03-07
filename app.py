from bottle import run, get, default_app, view, post, put, delete, request, response
import g
import uuid
import time
import re

tweets = {}

#########################
@post("/tweets")
def _():
    try:
        # VALIDATE
        if not request.forms.get("tweet_text"):
            return "tweet_text missing"

        tweet_text = request.forms.get("tweet_text").strip()

        # VALIDATE
        if len(tweet_text) < g.TWEET_MIN_LEN:
            return f"tweet must be at least {g.TWEET_MIN_LEN} characther"

        if len(tweet_text) > g.TWEET_MAX_LEN:
            return f"tweet cant be more than {g.TWEET_MAX_LEN} characthers"

        tweet_id = str(uuid.uuid4())
        tweet_created_at = (int(time.time()))
        tweet = {
            "tweet_id" : tweet_id,
            "tweet_text" : tweet_text,
            "tweet_created_at" : tweet_created_at
        }
        tweets[tweet_id] = tweet

        # SUCCESS
        response.status = 201
        return {"tweet_id":tweet_id}
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info":"something went wrong"}


#########################
@put("/tweets/<id>")
def _(id):
    try:
        # VALIDATE
        if not re.match(g.REGEX_UUID4, id):
            response.status = 204
            return

        if id not in tweets:
            response.status = 204
            return 

        if not request.forms.get("tweet_text"):
            response.status = 400
            return {"info": "tweet_text is missing"}

        tweet_text = request.forms.get("tweet_text").strip()

        if len(tweet_text) < g.TWEET_MIN_LEN:
            response.status = 400
            return {"info": f"tweet must be at least {g.TWEET_MIN_LEN} characther"}

        if len(tweet_text) > g.TWEET_MAX_LEN:
            response.status = 400
            return {"info": f"tweet cant be more than {g.TWEET_MAX_LEN} characthers"}

        # UPDATE TWEET
        tweets[id]["tweet_text"] = tweet_text
        tweets[id]["updated_at"] = int(time.time())

        # SUCESS
        return tweets[id]
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info":"something went wrong"}


#########################
@delete("/tweets/<id>")
def _(id):
    try:
        # VALIDATION
        if not re.match(g.REGEX_UUID4, id):
            response.status = 204
            return

        if id not in tweets:
            response.status = 204
            return 

        # delete tweet
        tweets.pop(id)

        # SUCESS
        return {"info" : "tweet deleted"}
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info":"something went wrong"}


#########################
@get("/tweets/<id>")
@get("/tweets/<id>/") # if you want to allow user add trailing slash
def _(id):
    try:
        # VALIDATION
        if not re.match(g.REGEX_UUID4, id):
            response.status = 204
            return

        if id not in tweets:
            response.status = 204
            return 

        # SUCESS
        return tweets[id]
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info":"something went wrong"}


#########################
@get("/tweets")
def _():
    try:
        return tweets
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info":"something went wrong"}


#########################
try:
    # Production server
    import production
    application = default_app()

except:
    # Development server
    run(host="127.0.0.1", port=3333, debug=True, reloader=True)