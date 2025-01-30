import tweepy
from twitter_auth import authenticate_twitter

def fetch_tweets(query, count=100):
    API_KEY = "your_api_key"
    API_SECRET = "your_api_secret"
    ACCESS_TOKEN = "your_access_token"
    ACCESS_TOKEN_SECRET = "your_access_token_secret"

    api = authenticate_twitter(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en").items(count)
    return [tweet.text for tweet in tweets]

if __name__ == "__main__":
    tweets = fetch_tweets("AI", 10)
    for tweet in tweets:
        print(tweet)
