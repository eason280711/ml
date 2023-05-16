import csv
import random

with open('student_study_hours_vs_grades.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)

  writer.writerow(['Study Hours', 'Grade'])

  for i in range(100):
    study_hours = round(random.uniform(1, 10), 2)
    grade = int(study_hours * 10) + random.randint(-5, 5)
    writer.writerow([study_hours, grade])
