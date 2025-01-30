import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("stopwords")
nltk.download("punkt")

def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r"\@\w+|\#", "", text)  # Remove mentions and hashtags
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    text = text.lower()  # Convert to lowercase
    return text

def tokenize_text(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    return [word for word in words if word not in stop_words]

if __name__ == "__main__":
    sample_tweet = "This is an amazing AI project! #AI #MachineLearning 🚀"
    cleaned = clean_text(sample_tweet)
    tokens = tokenize_text(cleaned)
    print("Cleaned:", cleaned)
    print("Tokens:", tokens)
