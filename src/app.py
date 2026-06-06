from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pydantic import BaseModel, Field


app = FastAPI()

model = joblib.load("../models/student_score_model.pkl")


class StudentInput(BaseModel):
    study_hours: float = Field(..., ge=0, le=24)
    attendance: float = Field(..., ge=0, le=100)

@app.get("/")
def home():
    return {
        "message": "Student Performance Predictor API is running!"
    }


@app.get("/predict")
def predict(study_hours: float, attendance: float):

    input_data = pd.DataFrame({
        "Study_Hours": [study_hours],
        "Attendance": [attendance]
    })

    prediction = model.predict(input_data)

    return {
        "predicted_score": round(float(prediction[0]), 2)
    }


@app.post("/predict")
def predict_post(data: StudentInput):

    input_data = pd.DataFrame({
        "Study_Hours": [data.study_hours],
        "Attendance": [data.attendance]
    })

    prediction = model.predict(input_data)

    return {
        "predicted_score": round(float(prediction[0]), 2)
    }