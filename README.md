# 🌸 Iris Flower Classification Web App

A professional end-to-end **Machine Learning project** that classifies iris flowers into species using their physical measurements.
The project includes data analysis, model training, evaluation, and a **Streamlit web application** for real-time predictions.

---

## 🚀 Project Overview

This project builds a classification model using the famous **Iris dataset**.
The goal is to predict the species of a flower based on:

* Sepal length
* Sepal width
* Petal length
* Petal width

The trained model is deployed as an **interactive web app** using Streamlit.

---

## 📊 Dataset Information

* **Dataset:** Iris Dataset (UCI Machine Learning Repository)
* **Total samples:** 150
* **Features:** 4
* **Classes:** 3

  * Iris-setosa
  * Iris-versicolor
  * Iris-virginica

---

## 🧠 Machine Learning Pipeline

The project follows an industry-standard ML workflow:

1. Data loading and inspection
2. Feature–target separation
3. Train–test split with stratification
4. Feature scaling using `StandardScaler`
5. Model training using **K-Nearest Neighbors (KNN)**
6. Hyperparameter tuning with cross-validation
7. Model evaluation
8. Model saving using `joblib`
9. Deployment with Streamlit

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:**

  * pandas
  * scikit-learn
  * joblib
  * streamlit

---

## 📁 Project Structure

```
iris-ml-project/
│
├── data/
│   └── iris.csv
│
├── model/
│   └── iris_model.pkl
│
├── src/
│   ├── train.py
│   └── predict.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 📈 Model Performance

* **Algorithm:** K-Nearest Neighbors
* **Preprocessing:** StandardScaler
* **Evaluation method:** Train–test split + cross-validation
* **Accuracy:** ~95–100% (depending on split and k value)

---

## ▶️ How to Run the Project

### 1. Clone the repository

```
git clone <your-repo-link>
cd iris-ml-project
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Train the model

```
python src/train.py
```

### 4. Run the Streamlit app

```
streamlit run app.py
```

The app will open automatically in your browser.

---

## 🌐 Web App Features

* Interactive sliders for flower measurements
* Real-time species prediction
* Clean and simple UI
* Fast inference using saved model

---

## 📌 Key Learnings

* End-to-end ML pipeline
* Feature scaling importance in distance-based models
* Hyperparameter tuning
* Model serialization
* Deploying ML models with Streamlit

---

## 🔮 Future Improvements

* Add multiple model comparison
* Deploy app online (Streamlit Cloud or Render)
* Add confusion matrix visualization
* Add model explainability

---

## 👨‍💻 Author

**Shivam Gupta**
B.Tech Student | Aspiring Data Scientist & ML Engineer

---

## ⭐ If you like this project

Give it a star on GitHub and feel free to fork or contribute!
