import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

def train_model():
    df = pd.read_csv("data/tweets.csv")  # Dataset with "text" and "label" columns

    X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

    model = Pipeline([
        ("vectorizer", CountVectorizer()),
        ("classifier", MultinomialNB())
    ])

    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    print(f"✅ Model Accuracy: {accuracy:.2f}")

    joblib.dump(model, "sentiment_model.pkl")

if __name__ == "__main__":
    train_model()
