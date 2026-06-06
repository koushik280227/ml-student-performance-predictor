# Student Performance Predictor

A Machine Learning project that predicts student scores based on study hours and attendance.

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

## Future Improvements

- Larger datasets
- Additional ML algorithms
- Database integration
- Frontend interface
- Deployment on cloud platforms