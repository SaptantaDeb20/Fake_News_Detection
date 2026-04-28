# 📰 Fake News Detection System using Machine Learning

A web-based application that detects whether a news article is **Real or Fake** using Natural Language Processing (NLP) and Machine Learning.

---

## 🚀 Features

* 🔍 Classifies news as **Real** or **Fake**
* 🧠 Uses **TF-IDF Vectorization** for text feature extraction
* ⚡ Trained with **Logistic Regression**
* 🌐 Built with **Flask API** for real-time predictions
* 🎨 Interactive frontend using **HTML, Tailwind CSS, JavaScript**

---

## 🧠 Machine Learning Pipeline

1. **Data Collection**

   * Dataset of 44,000+ news articles (True & Fake)

2. **Preprocessing**

   * Combined `title + text`
   * Lowercasing and cleaning (removing special characters)

3. **Feature Engineering**

   * TF-IDF Vectorization
   * N-grams for contextual understanding

4. **Model Training**

   * Logistic Regression
   * Balanced class weights

5. **Evaluation**

   * ~98–99% accuracy on test data

---

## 📂 Project Structure

```
project/
 ├── app.py
 ├── model/
 │    ├── model_lr.pkl
 │    └── vectorization.pkl
 ├── templates/
 │    └── index.html
 ├── static/
 │    ├── bg1.webp
 │    ├── correct.png
 │    └── fake.png
 ├── data_set/
 │    ├── True.csv
 │    └── Fake.csv
 └── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/fake-news-detection.git
cd fake-news-detection
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Run the application

```
python app.py
```

---

### 4️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 🧪 Example Inputs

### ✅ Real News

```
WASHINGTON (Reuters) - The government announced new healthcare reforms to improve hospital services.
```

### ❌ Fake News

```
BREAKING: Secret government plan reveals citizens are being controlled using hidden microchips!
```

---

## 📡 API Endpoint

### POST `/predictdata`

#### Request:

```json
{
  "news": "Your news text here"
}
```

#### Response:

```json
{
  "result": "Real News"
}
```

---

## 🛠️ Tech Stack

* Python 🐍
* Flask 🌐
* Scikit-learn 🤖
* Pandas & NumPy 📊
* HTML + Tailwind CSS 🎨
* JavaScript ⚡

---

## 📈 Future Improvements

* 🔥 Use Deep Learning models (LSTM, BERT)
* 🌍 Deploy on cloud (AWS / Render / Heroku)
* 📊 Add confidence score visualization
* 📱 Mobile-friendly UI

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 🙌 Acknowledgements

* Kaggle Fake News Dataset
* Scikit-learn Documentation
* Flask Framework

---
