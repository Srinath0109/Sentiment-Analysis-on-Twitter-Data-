import joblib
from preprocess import clean_text
from fetch_tweets import fetch_tweets

def analyze_tweets(query, count=10):
    model = joblib.load("sentiment_model.pkl")
    tweets = fetch_tweets(query, count)

    for tweet in tweets:
        cleaned_tweet = clean_text(tweet)
        sentiment = model.predict([cleaned_tweet])
        print(f"TWEET: {tweet}\nSENTIMENT: {'😊 Positive' if sentiment == 1 else '😞 Negative'}\n")

if __name__ == "__main__":
    analyze_tweets("AI", 5)
