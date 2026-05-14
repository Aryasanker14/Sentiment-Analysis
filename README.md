
# Task 4 — Sentiment Analysis (VADER)

Classify text reviews as **Positive / Neutral / Negative** using **NLTK's VADER**.

## What it does
- Loads `reviews.csv` (sample dataset provided)
- Applies VADER to compute sentiment scores
- Labels each review and saves `reviews_scored.csv`
- Plots a simple bar chart with class counts

## How to run
```bash
pip install -r ../requirements.txt
python sentiment_vader.py
```

## Files generated
- `reviews_scored.csv` with scores and labels
- `sentiment_counts.png` chart
