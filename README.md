# 📱 SMS Spam Classifier

An end-to-end machine learning project that classifies SMS messages as **spam** or **not spam (ham)** using **Natural Language Processing (NLP)** techniques.  
This project includes a **Streamlit web app** for real-time predictions.

---

## 🚀 Live App
👉 Test the live application here: [SMS Spam Classifier](https://sms-spam-classifier97.streamlit.app/)

---

## ✨ Key Features
- **Spam Detection**: A machine learning model that accurately classifies SMS messages as spam or ham.  
- **Interactive UI**: A user-friendly interface built with Streamlit.  
- **Robust Preprocessing**: Comprehensive text cleaning (lowercasing, tokenization, stopword removal, stemming).  
- **Model Persistence**: Trained model & vectorizer are saved (`.pkl`) for instant predictions without retraining.  

---

## 📂 Project Structure  

- `app.py` → Main Streamlit app  
- `nltk.txt` → NLTK corpora requirements (`punkt`, `stopwords`)  
- `requirements.txt` → Python dependencies  
- `model.pkl` → Trained Naive Bayes model  
- `vectorizer.pkl` → Trained TF-IDF vectorizer  
- `README.md` → Project documentation  

---

## 🧠 The Model

- Algorithm: **Multinomial Naive Bayes**  
- Feature extraction: **TfidfVectorizer (TF-IDF)**  
- Why Naive Bayes? Simple, fast, and highly effective for text classification tasks.  

### 🔎 Data Preprocessing
- Lowercasing  
- Tokenization  
- Removing special characters  
- Stopword removal (NLTK English stopwords)  
- Stemming (Porter Stemmer)  

---

## 💾 Dataset
- **Dataset**: [SMS Spam Collection](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)  
- Contains **5,574 English SMS messages** labeled as spam or ham.  

---

## 🛠️ How to Run Locally

### 1️⃣ Installation
```bash
git clone https://github.com/ADITIVERMA956/SMS_SPAM_CLASSIFIER.git
cd SMS_SPAM_CLASSIFIER
pip install -r requirements.txt
```
### 2️⃣ Run the Application
```bash
streamlit run app.py
```
---
## 🤝 Contributing  

Contributions are welcome! 🎉  
To add new features or fix bugs:  

1. **Fork** the repository.  
2. **Clone** your fork:  

```bash
git clone https://github.com/<your-username>/SMS_SPAM_CLASSIFIER.git
```
### Create a New Branch  

```bash
git checkout -b feature/your-feature-name
```
### Make Changes & Commit  

```bash
git commit -m "Added new feature"
```
### Push Changes  

```bash
git push origin feature/your-feature-name
```

---
## 📜 License & Credits  

- **License**: MIT License – free to use, modify, and distribute.  

- **Built With**:  
  - [Streamlit](https://streamlit.io/)  
  - [Scikit-learn](https://scikit-learn.org/)  
  - [NLTK](https://www.nltk.org/)  
---
## 👩‍💻 Author  

Developed with ❤️ by **Aditi Verma**  
📧 Email: [aditivns9569@gmail.com](mailto:aditivns9569@gmail.com)  
🌐 GitHub: [ADITIVERMA956](https://github.com/ADITIVERMA956)  


