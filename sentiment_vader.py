
import os
import csv
import pandas as pd
import matplotlib.pyplot as plt

# NLTK VADER setup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def ensure_vader():
    try:
        nltk.data.find("sentiment/vader_lexicon.zip")
    except LookupError:
        nltk.download("vader_lexicon")

def label_from_compound(c):
    if c >= 0.05:
        return "Positive"
    elif c <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def main():
    ensure_vader()
    sia = SentimentIntensityAnalyzer()

    df = pd.read_csv("reviews.csv")
    scores = df["review"].apply(lambda t: sia.polarity_scores(str(t))["compound"])
    df["compound"] = scores
    df["label"] = df["compound"].apply(label_from_compound)
    df.to_csv("reviews_scored.csv", index=False)

    # Plot counts
    counts = df["label"].value_counts().reindex(["Positive","Neutral","Negative"]).fillna(0)
    plt.figure()
    counts.plot(kind="bar")
    plt.title("Sentiment Class Counts")
    plt.xlabel("Class")
    plt.ylabel("Count")
    plt.savefig("sentiment_counts.png")
    plt.close()
    print("Done. Wrote reviews_scored.csv and sentiment_counts.png")

if __name__ == "__main__":
    main()
