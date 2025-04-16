# 💸 Expense Tracking System

A GUI-based web application that allows you to track, analyze, and visualize your daily expenses with ease. Built with **FastAPI** for the backend, **Streamlit** for the frontend, and **MySQL** as the database.

---

## 🛠 Tech Stack

- **Frontend:** Streamlit (Python)
- **Backend:** FastAPI (Python)
- **Database:** MySQL
- **HTTP Requests:** `requests` module (Python)
- **Environment:** Virtualenv (.venv)

---

## 🚀 Features

- 📅 Add daily expenses with categories and notes  
- 📊 View daily or range-based expense summaries  
- 📈 Analytics with category-wise breakdown  
- 🧠 Intuitive UI with Streamlit  
- 🔄 CRUD operations handled via FastAPI

---

## 📷 Screenshots

_Add UI screenshots here to showcase your app interface._

---

## 🧪 Run Locally

### 1. Clone the Repository
git clone https://github.com/your-username/Expense_Tracking_System.git
cd Expense_Tracking_System

### 2. Set up Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Set up MySQL Database
CREATE DATABASE expense_manager;

USE expense_manager;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATETIME NOT NULL,
    amount FLOAT NOT NULL,
    category VARCHAR(255),
    notes TEXT
);

### 5. Run Backend Server(FastAPI)
cd Backend
uvicorn main:app --reload

### 6. Run Frontend App(Streamlit)
cd ../Frontend
streamlit run app.py

## API Endpoints
GET /expenses/{date} – Fetch all expenses for a date

POST /expenses/{date} – Add or update expenses for a date

POST /analytics/ – Get category-wise analytics for a date range

## Project Structure
Expense_Tracking_System/
│
├── Backend/
│   ├── main.py
│   ├── db_helper.py
│   └── models.py
│
├── Frontend/
│   └── app.py
│
├── requirements.txt
└── README.md

# Author
Neel Madhav
****
