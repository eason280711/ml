import pandas as pd

url = "https://raw.githubusercontent.com/eason280711/ml/main/Data/student_study_hours_vs_grades.csv"
df = pd.read_csv(url)

print(df)

x = df["Study Hours"]
y = df["Grade"]

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import fontManager

fontManager.addfont("Font/ChineseFont.ttf")
matplotlib.rc('font', family="ChineseFont")

plt.scatter(x, y, marker="x", color="red")
plt.title("時間-成績關係圖")
plt.xlabel("時間(小時)")
plt.ylabel("成績(分)")
plt.show()