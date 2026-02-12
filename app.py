from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load("model/iris_data_model")


@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    sl = float(request.form["sepal_length"])
    sw = float(request.form["sepal_width"])
    pl = float(request.form["petal_length"])
    pw = float(request.form["petal_width"])

    data = np.array([[sl, sw, pl, pw]])
    prediction = model.predict(data)[0]

    return render_template("index.html", prediction=prediction)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
