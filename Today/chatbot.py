import streamlit as st
import pandas as pd
import numpy as np
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

st.set_page_config(page_title="Spam Detection Chatbot", layout="centered")
st.title("📧 Spam Detection Chatbot")

# Load or prepare the dataset
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
    df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])
    return df

data = load_data()
st.write("### Sample Data", data.head())

# Preprocessing function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text

data['cleaned'] = data['message'].apply(clean_text)

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['cleaned'])
y = data['label'].map({'ham': 0, 'spam': 1})

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate
accuracy = accuracy_score(y_test, model.predict(X_test))
st.write(f"✅ Model Accuracy: {accuracy:.2%}")

# Save model and vectorizer
joblib.dump(model, "spam_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

# User input
st.write("### Test the Spam Detection Chatbot")
user_input = st.text_area("Enter your message:", "Hello, I have a special offer for you...")

if st.button("Predict"):
    cleaned_input = clean_text(user_input)
    vect_input = vectorizer.transform([cleaned_input])
    prediction = model.predict(vect_input)[0]
    label = "🚫 Spam" if prediction == 1 else "✅ Not Spam"
    st.write(f"### Prediction: {label}")

st.caption("Model: Multinomial Naive Bayes | Data: SMS Spam Collection | Streamlit Deployment")
