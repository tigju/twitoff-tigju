# # app/routes/book_routes.py

from app.services.basilica_service import connection as basilica_api_client
from app.services.twitter_service import api as twitter_api_client
from app.models import db, User, Tweet, parse_records
from flask import Blueprint, render_template, jsonify, request, redirect,flash

twitter_routes = Blueprint("twitter_routes", __name__)

######################## Assignment 1 #############################################
# from flask import Blueprint, jsonify, request, render_template #, flash, redirect
# from app.models import db, Tweet, parse_records
# twitter_routes = Blueprint("twitter_routes", __name__)

# @twitter_routes.route("/tweets.json")
# def list_tweets():

#     tweet_records = Tweet.query.all()
#     print(tweet_records)

#     tweets = parse_records(tweet_records)
#     return jsonify(tweets)

@twitter_routes.route("/tweets")
def show_tweets():

    tweet_records = Tweet.query.all()
    user_records = User.query.all()
    print(tweet_records)
    parsed_tweets = parse_records(tweet_records)
    parsed_users = parse_records(user_records)
    # return jsonify(parsed_tweets)
    return render_template("tweets.html", message="List of All Tweets", tweets=parsed_tweets, users=parsed_users)

# @twitter_routes.route("/tweets/new")
# def new_tweet():
#     return render_template("new_tweet.html")

# @twitter_routes.route("/tweets/create", methods=["POST"])
# def create_tweet():
#     print("FORM DATA:", dict(request.form))
#     # store in database
#     new_tweet = Tweet(text=request.form["tweet_text"], user_id=request.form["username"])
#     db.session.add(new_tweet)
#     db.session.commit()

#     return jsonify({
#         "message": "TWEET CREATED OK ",
#         "tweet": dict(request.form)
#     })
##################### end Assignment 1 ####################



@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)

    twitter_user = twitter_api_client.get_user(screen_name)
    user_tweets = twitter_api_client.user_timeline(
        screen_name, tweet_mode="extended", count=150)
    print("STATUSES COUNT:", len(user_tweets))
    #return jsonify({"user": user._json, "tweets": [s._json for s in statuses]})

    # get existing user from the db or initialize a new one:
    user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    user.screen_name = twitter_user.screen_name
    user.name = twitter_user.name
    user.location = twitter_user.location
    user.followers_count = twitter_user.followers_count
    db.session.add(user)
    db.session.commit()
    #return "OK"

    all_tweet_texts = [tweet.full_text for tweet in user_tweets]
    embeddings = list(basilica_api_client.embed_sentences(
        all_tweet_texts, model="twitter"))
    print("NUMBER OF EMBEDDINGS", len(embeddings))

    # TODO: explore using the zip() function maybe...
    counter = 0
    for tweet in user_tweets:
        print(tweet.full_text)
        print("----")
        # get existing tweet from the db or initialize a new one:
        db_tweet = Tweet.query.get(tweet.id) or Tweet(id=tweet.id)
        db_tweet.user_id = tweet.author.id  # or db_user.id
        db_tweet.full_text = tweet.full_text
        embedding = embeddings[counter]
        print(len(embedding))
        db_tweet.embedding = embedding
        db.session.add(db_tweet)
        counter += 1
    db.session.commit()
    # return "OK"
    # tweets=db_tweets
    return render_template("user.html", user=user, tweets=user_tweets)


# user list or find user in db
@twitter_routes.route("/list", methods=["GET","POST"])
def get_user_by_name():
    if request.method == 'GET':
        users = parse_records(User.query.all())
        return render_template('users_list.html', users=users)
    # print("FORM DATA:", dict(request.form))
    else:
        user = dict(request.form)
        # print(user["username"])
        user = User.query.filter_by(screen_name=user["username"]).one_or_none()
        if not user:
            flash("User not found in database", "danger")
            return redirect("/list")
        else:    
            users = []
            users.append(user)
            return render_template('users_list.html', users=users)
    
