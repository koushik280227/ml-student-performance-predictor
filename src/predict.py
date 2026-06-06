import pandas as pd
import joblib

model = joblib.load("../models/student_score_model.pkl")
study_hours = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance: "))
input_data = pd.DataFrame({
    "Study_Hours": [study_hours],
    "Attendance": [attendance]
})
prediction = model.predict(input_data)
print(f"Predicted Score: {prediction[0]:.2f}")