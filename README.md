# 🧠 Sentiment Analysis API with Flask + Streamlit

This project is a simple Sentiment Analysis application built using **Flask** for the backend API and **Streamlit** for the frontend UI. It uses **TextBlob** to analyze the sentiment of the input text.

---

## 📁 Project Structure

```
project-name/
├── app/
│   ├── __init__.py
│   ├── main.py          # Flask API
│   ├── model.py         # Sentiment logic
│   └── utils.py         # Helper functions
├── data/
│   └── sample_texts.txt
├── notebooks/
│   └── sentiment_experiment.ipynb
├── streamlit_app/
│   └── app.py           # Streamlit UI
├── requirements.txt
├── README.md
└── Dockerfile
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/sentiment-analysis-api.git
cd sentiment-analysis-api
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
python -m textblob.download_corpora  # Download necessary corpora
```

### 4. Run the Flask Backend
```bash
cd app
python main.py
```
Visit: `http://localhost:5000/analyze`

### 5. Run the Streamlit Frontend
Open a new terminal:
```bash
cd streamlit_app
streamlit run app.py
```
Visit: `http://localhost:8501`

---

## 🛠️ API Endpoint

### `POST /analyze`
**Request:**
```json
{
  "text": "I love this app!"
}
```
**Response:**
```json
{
  "sentiment": "positive"
}
```

---

## 📦 Requirements
- Flask
- Streamlit
- TextBlob
- Requests

Install via:
```bash
pip install -r requirements.txt
```

---

## 🧪 To-Do / Extensions
- [ ] Add emoji-based output
- [ ] Use a custom-trained model (e.g., sklearn or transformer)
- [ ] Deploy via Docker or on cloud (Heroku, GCP, AWS)

---

## 📄 License
MIT - free to use and modify.

---

## 🙌 Acknowledgments
Built with 💙 using Flask, Streamlit, and TextBlob.
