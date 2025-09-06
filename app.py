import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk

# Download stopwords only
@st.cache_data(show_spinner=False)
def download_stopwords():
    nltk.download('stopwords')

download_stopwords()

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = text.split()  # Simple tokenizer without nltk.word_tokenize

    # Keep only alphanumeric words
    y = [word for word in text if word.isalnum()]

    # Remove stopwords and punctuation
    y = [word for word in y if word not in stopwords.words('english') and word not in string.punctuation]

    # Stemming
    y = [ps.stem(word) for word in y]

    return " ".join(y)

# Load your pickled model and vectorizer (with exact filenames)
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    # 1. Preprocess
    transformed_sms = transform_text(input_sms)
    # 2. Vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. Predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
