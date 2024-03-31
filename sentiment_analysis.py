# import necessary libraries 
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd

# Importing spacy
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

amazon_reviews = pd.read_csv('amazon_product_reviews.csv', low_memory=False)

# remove missing values/nas from the column data
clean_data = amazon_reviews.dropna(subset=['reviews.text'])

# select the column for sentiment analysis
reviews_text = clean_data['reviews.text']

print(reviews_text.head())
print(reviews_text.describe())

# preprocessing steps - e.g.remove stop words, lowercs, stripe
def preprocess_text(text):
    if isinstance(text, str):
        # Convert to lowercase
        text = text.lower()
        # Remove leading/trailing whitespace
        text = text.strip()
        # Remove stopwords
        doc = nlp(text)
        tokens = [token.text for token in doc if not token.is_stop]
        return ' '.join(tokens)
    else:
        return ''

# function for sentiment analysis
def predict_sentiment(review):
    preprocessed_review = preprocess_text(review) # preprocess the review
    # create sentiment analysis
    doc = nlp(preprocessed_review)
    polarity = doc._.blob.polarity
    subjectivity = doc._.blob.subjectivity
    # determine sentiment based on polarity
    if polarity > .2:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment, polarity, subjectivity

# select a 2 reviews to compare sentiment
my_review_of_choice = reviews_text[20]
my_review_of_choice2 = reviews_text[1112]

# preprocess the selected reviews from above
preprocessed_review1 = preprocess_text(my_review_of_choice)
preprocessed_review2 = preprocess_text(my_review_of_choice2)

# apply the sentiment, polarity, and subjectivity to compare reviews
sentiment, polarity, subjectivity = predict_sentiment(my_review_of_choice)
sentiment2, polarity2, subjectivity2 = predict_sentiment(my_review_of_choice2)

# check the sentiment analysis of my_review_of_choice
print(f"Review: {my_review_of_choice}")
print(f"Sentiment: {sentiment}")
print(f"Polarity: {polarity}")
print(f"Subjectivity: {subjectivity}")

print(f"Review: {my_review_of_choice2}")
print(f"Sentiment: {sentiment2}")
print(f"Polarity: {polarity2}")
print(f"Subjectivity: {subjectivity2}")