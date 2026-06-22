from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")

class CustomerData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float

@app.get("/")
def home():
    return {"message": "Customer Churn API Running"}

@app.post("/predict")
def predict(data: CustomerData):

    features = np.array([[
        data.feature1,
        data.feature2,
        data.feature3,
        data.feature4
    ]])

    prediction = model.predict(features)[0]

    return {
        "prediction": int(prediction)
    }