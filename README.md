# 🎓 Student Performance Predictor

An end-to-end Machine Learning project that predicts student exam scores 
based on study hours and attendance — served via a REST API built with FastAPI.

## 🎯 Problem Statement

Can we predict how well a student will perform based on their study habits 
and attendance? This project builds a regression model to answer that, 
achieving an R² score of 0.9973.

## Installation

1. Clone the repository

git clone https://github.com/koushik280227/ml-student-performance-predictor.git

2. Navigate to the project folder

cd ml-student-performance-predictor

3. Create a virtual environment

python -m venv venviron

4. Activate the virtual environment

macOS/Linux:

source venviron/bin/activate

Windows:

venviron\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

## Run FastAPI Server

cd src

uvicorn app:app --reload

Open:

http://127.0.0.1:8000/docs

## Features

- Data loading using Pandas
- Data visualization using Matplotlib
- Linear Regression model using Scikit-Learn
- Train/Test Split for model evaluation
- R² Score calculation
- Model saving and loading using Joblib
- FastAPI integration
- GET prediction endpoint
- POST prediction endpoint
- Input validation using Pydantic

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- FastAPI
- Pydantic
- Joblib
- Git
- GitHub

## Project Structure

```text
ml-student-performance-predictor
│
├── data/
│   └── students.csv
│
├── graphs/
│   └── study_hours_vs_score.png
│
├── models/
│   └── student_score_model.pkl
│
├── src/
│   ├── train_model.py
│   ├── predict.py
│   ├── visualize.py
│   └── app.py
│
├── README.md
└── .gitignore
```

## Machine Learning Workflow

1. Load dataset using Pandas
2. Visualize data using Matplotlib
3. Split data into training and testing sets
4. Train a Linear Regression model
5. Evaluate model using R² Score
6. Save the trained model using Joblib
7. Load the saved model for predictions
8. Serve predictions through FastAPI

## API Endpoints

### Home Endpoint

GET /

Response:

{
  "message": "Student Performance Predictor API is running!"
}

### Prediction Endpoint (GET)

GET /predict?study_hours=8&attendance=90

Response:

{
  "predicted_score": 86.40
}

### Prediction Endpoint (POST)

POST /predict

Request:

{
  "study_hours": 8,
  "attendance": 90
}

Response:

{
  "predicted_score": 86.40
}

## Model Performance

- Algorithm: Linear Regression
- Evaluation Metric: R² Score
- Accuracy Achieved: 0.9973

> An R² of 0.9973 means the model explains 99.7% of the variance 
> in student scores — indicating a strong linear relationship 
> between study hours/attendance and performance.

## 💡 Key Learnings

- Strong linear relationship exists between study habits and performance
- FastAPI makes deploying ML models as REST APIs fast and clean
- Joblib efficiently serializes and reloads trained models
- Input validation with Pydantic prevents bad API requests

## Future Improvements

- Add more features (sleep hours, extracurriculars)
- Try polynomial regression for non-linear patterns
- Deploy on AWS/GCP/Render
- Build a frontend interface with Streamlit