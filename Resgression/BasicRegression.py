import pandas as pd

# Read Data

url = "https://raw.githubusercontent.com/eason280711/ml/main/Data/student_study_hours_vs_grades.csv"
df = pd.read_csv(url)

print(df)

x = df["Study Hours"]
y = df["Grade"]

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import fontManager

# Matplotlib Font Setting

fontManager.addfont("Font/ChineseFont.ttf")
matplotlib.rc('font', family="ChineseFont")

# Show Data

plt.scatter(x, y, marker="x", color="red")
plt.title("時間-成績關係圖")
plt.xlabel("時間(小時)")
plt.ylabel("成績(分)")
plt.show()

# Linear Regression: y = wx + b

w = 5
b = 5

y_pred = x*w + b

plt.plot(x, y_pred, color="blue", label="預測線")
plt.scatter(x, y, marker="x", color="red", label="真實數據")
plt.title("時間-成績關係圖")
plt.xlabel("時間(小時)")
plt.ylabel("成績(分)")
plt.xlim([0, 10])
plt.ylim([0, 100])
plt.legend()
plt.show()
