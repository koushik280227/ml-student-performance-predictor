# import pandas as pd
# df = pd.read_csv("../data/students.csv")
# print(df)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/students.csv")

plt.scatter(df["Study_Hours"], df["Score"])

plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.title("Study Hours vs Score")

plt.savefig("../graphs/study_hours_vs_score.png")
plt.show()