# Iris Flower Prediction Web App

A simple and elegant **Machine Learning web application** that predicts the species of an Iris flower based on its measurements.
This project demonstrates the **complete ML workflow** — from training a model to deploying it as a web application.

---

## Live Demo

https://irisdatapridicitor2.vercel.app/

---

## Project Overview

This application takes four input features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

Using a trained **scikit-learn classification model**, it predicts the species of the Iris flower:

* Iris Setosa
* Iris Versicolor
* Iris Virginica

---

## Tech Stack

**Machine Learning**

* Python
* scikit-learn
* NumPy
* Joblib

**Backend**

* Flask

**Frontend**

* HTML
* CSS

**Deployment**

* Render (Web Service)
* Vercel (Web Service)

---

## Project Structure

```
MyDailyWork_Task2/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── model/
│   └── iris_model.pkl
└── templates/
    └── index.html
```

---

## Installation (Local Setup)

### 1. Clone the repository

```
git clone https://github.com/your-username/MyDailyWork_Task2.git
cd MyDailyWork_Task2
```

### 2. Create virtual environment (optional but recommended)

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the application

```
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000
```

---

## Deployment on Render

1. Push the project to GitHub.
2. Go to **Render Dashboard**.
3. Create a **New Web Service**.
4. Connect your GitHub repository.
5. Use these settings:

**Build Command**

```
pip install -r requirements.txt
```

**Start Command**

```
gunicorn app:app
```

Render will automatically use the Python version specified in:

```
runtime.txt
```

---

## Features

* Clean and modern UI
* Real-time prediction
* Lightweight ML model
* Deployable Flask architecture
* Beginner-friendly project structure

---

## Author

**Shivam Gupta**
Machine Learning & Data Science Enthusiast



## License

This project is for educational and portfolio purposes.
