import tweepy
import os
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
#print("AUTH", type(auth))

api = tweepy.API(auth)
#print("API CLIENT", type(api))

# another approach to puth inside the function and import
# def twitter_api_client():
#     return tweepy.API(auth)

if __name__ == "__main__":
    
    user = api.get_user('tigju24')
    # print(type(user))
    # pprint(user._json)
    # print(user.id)
    # print(user.screen_name)
    # print(user.name)
    # print(user.followers_count)

    # tweets = api.user_timeline("tigju24", tweet_mode="extended",
                            #    count=150, exclude_replies=True, include_rts=False)
    tweets = api.user_timeline("tigju24", tweet_mode="extended", count=150)
    print(type(tweets))  # > <class 'tweepy.models.ResultSet'>

    # print(tweets[0].id)
    # print(tweets[0].full_text)

    for tweet in tweets:
        print("---------")
        print(tweet.id, tweet.full_text)


