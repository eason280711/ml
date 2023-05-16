import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read Data
url = "https://raw.githubusercontent.com/eason280711/ml/main/Data/student_study_hours_vs_grades.csv"
df = pd.read_csv(url)

x = df["Study Hours"]
y = df["Grade"]

# Cost Function
def cost_function(x, y, w, b):
    n = len(x)
    return np.sum((y - (w*x + b))**2) / n

# Calculate cost for a range of w values (b fixed)
b_fixed = 10
w_values = np.arange(-50, 51) # Adjust the range and number of w values as needed
costs_w = [cost_function(x, y, w, b_fixed) for w in w_values]

# Find minimum cost and its corresponding w
min_cost_w = min(costs_w)
min_w = w_values[costs_w.index(min_cost_w)]

# Plot cost vs w (b fixed)
plt.figure(figsize=(10, 5))
plt.plot(w_values, costs_w)
plt.scatter(min_w, min_cost_w, color='r') # plot the minimum point
plt.title('Cost vs. Weight')
plt.xlabel('Weight (w)')
plt.ylabel('Cost')
plt.grid(True)
plt.show()

# Calculate cost for a range of w and b values
w_values = np.arange(-50, 51)
b_values = np.arange(-50, 51)
costs_wb = np.zeros((len(w_values), len(b_values)))

for i, w in enumerate(w_values):
    for j, b in enumerate(b_values):
        costs_wb[i, j] = cost_function(x, y, w, b)

# Find minimum cost and its corresponding w and b
min_cost_wb = np.min(costs_wb)
min_wb_index = np.unravel_index(np.argmin(costs_wb), costs_wb.shape)
min_w, min_b = w_values[min_wb_index[0]], b_values[min_wb_index[1]]

# Plot cost vs w and b
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
w_values, b_values = np.meshgrid(w_values, b_values)
ax.plot_surface(w_values, b_values, costs_wb, cmap='viridis')
ax.scatter(min_w, min_b, min_cost_wb, color='r')
ax.set_title('Cost vs. Weight and Bias')
ax.set_xlabel('Weight (w)')
ax.set_ylabel('Bias (b)')
ax.set_zlabel('Cost')
plt.show()
