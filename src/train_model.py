# import pandas as pd
# df = pd.read_csv("../data/students.csv")
# print(df)

# import pandas as pd
# df = pd.read_csv("../data/students.csv")
# X = df[["Study_Hours", "Attendance"]]
# y = df["Score"]
# print("Features (X):")
# print(X)
# print("\nTarget (y):")
# print(y)

# import pandas as pd
# from sklearn.linear_model import LinearRegression
# df = pd.read_csv("../data/students.csv")
# X = df[["Study_Hours", "Attendance"]]
# y = df["Score"]
# model = LinearRegression()
# model.fit(X, y)
# predicted_score = model.predict([[11, 96]])
# print("Predicted Score:", predicted_score[0])

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
df = pd.read_csv("../data/students.csv")
X = df[["Study_Hours", "Attendance"]]
y = df["Score"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
score = r2_score(y_test, y_pred)
# print("R² Score:", score)
print(f"Model Accuracy (R²): {score:.4f}")
study_hours = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance: "))

if study_hours < 0:
    print("Study Hours cannot be negative.")
    exit()

if attendance < 0 or attendance > 100:
    print("Attendance must be between 0 and 100.")
    exit()

input_data = pd.DataFrame(
    {
        "Study_Hours": [study_hours],
        "Attendance": [attendance]
    }
)

prediction = model.predict(input_data)
print(f"Predicted Score: {prediction[0]:.2f}")