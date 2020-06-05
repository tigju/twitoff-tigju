# app/routes/book_routes.py

from flask import Blueprint, jsonify, request, render_template #, flash, redirect

from app.models import db, Tweet, parse_records

tweet_routes = Blueprint("tweet_routes", __name__)

@tweet_routes.route("/tweets.json")
def list_tweets():

    tweet_records = Tweet.query.all()
    print(tweet_records)

    tweets = parse_records(tweet_records)
    return jsonify(tweet)

@tweet_routes.route("/tweets")
def show_tweets():

    tweet_records = Tweet.query.all()
    print(tweet_records)

    tweets = parse_records(tweet_records)
    return render_template("tweets.html", message="List of Tweets", tweets=tweets)

@tweet_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@tweet_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form))
    # store in database
    new_tweet = Tweet(text=request.form["tweet_text"], user_id=request.form["username"])
    db.session.add(new_tweet)
    db.session.commit()

    return jsonify({
        "message": "TWEET CREATED OK ",
        "tweet": dict(request.form)
    })
