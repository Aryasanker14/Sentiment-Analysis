Sentiment analysis:
Sentiment analysis (also known as opinion mining or emotion AI) is the use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information.
# Task 4 — Sentiment Analysis (VADER)

Classify text reviews as **Positive / Neutral / Negative** using **NLTK's VADER**.

## What it does
- Loads `reviews.csv` (sample dataset provided)
- Applies VADER to compute sentiment scores
- Labels each review and saves `reviews_scored.csv`
- Plots a simple bar chart with class counts

## How to run
```bash
pip install nltk
python sentiment_vader.py
```

## Files generated
- `reviews_scored.csv` with scores and labels
- `sentiment_counts.png` chart
