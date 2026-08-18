import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('Student Study Efficiency Analyzer/Cleaned_Dataset.csv')
print(data.info())

# Avg Test score
avg_test_score = data['Test_scores'].mean()
print(f"Average Test Score: {avg_test_score}")

#Students with above 80 test scores
above_80_students = data[data['Test_scores'] > 80]
print(f"Number of students with above 80 test scores: {len(above_80_students)}")

#Student's average test score with above 4 hours of sleep
avg_test_score_below_4_sleep = data[data['Sleep_hours'] < 4]['Test_scores'].mean()
print(f"Average Test Score of students with below 4 hours of sleep: {avg_test_score_below_4_sleep}")

#relationship between study hours and test scores
correlation_study_test_scores = data['Study_hours'].corr(data['Test_scores'])
print(f"Correlation between Study Hours and Test Scores: {correlation_study_test_scores}")

#relationship between attendance and test scores
correlation_attendance_test_scores = data['Attendance'].corr(data['Test_scores'])
print(f"Correlation between Attendance and Test Scores: {correlation_attendance_test_scores}")

#relationship between sleep hours and test scores
correlation_sleep_test_scores = data['Sleep_hours'].corr(data['Test_scores'])
print(f"Correlation between Sleep Hours and Test Scores: {correlation_sleep_test_scores}")

#relationship between phone usage and test scores
correlation_phone_test_scores = data['Phone_usage'].corr(data['Test_scores'])
print(f"Correlation between Phone Usage and Test Scores: {correlation_phone_test_scores}")

#relationship between assignment completed and test scores
correlation_assignment_test_scores = data['Assignment_completed'].corr(data['Test_scores'])
print(f"Correlation between Assignment Completed and Test Scores: {correlation_assignment_test_scores}")

Outstanding_O=data[data['Test_scores']>90]
Excellent_A=data[data['Test_scores']>80]
Great_B=data[data['Test_scores']>80]
Fair_C=data[data['Test_scores']>60]
Average_D=data[data['Test_scores']>50]
Below_Average_E=data[data['Test_scores']>40]
need_improvement_F=data[data['Test_scores']<40]
print(f"Category")
print(f"Outstanding_O: {len(Outstanding_O)} Students")
print(f"Excellent_A: {len(Excellent_A)} Students")
print(f"Great_B: {len(Great_B)} Students")
print(f"Fair_C: {len(Fair_C)} Students")
print(f"Average_D: {len(Average_D)} Students")
print(f"Below_Average_E: {len(Below_Average_E)} Students")
print(f"need_improvement_F: {len(need_improvement_F)} Students")

#anomaly detection
students_with_anomalies = data[(data['Study_hours'] > 6) & (data['Test_scores'] <50)]
print(f"Number of students with anomalies (Study hours > 5 and Test scores < 50): {len(students_with_anomalies)}")
# why?
print(students_with_anomalies[['Student_id', 'Study_hours', 'Phone_usage', 'Sleep_hours','Test_scores']])
#Students scored less than 50 even after studying for more than 6 hours, which is an anomaly. This could be due to excessive phone usage or lack of sleep.


# From the above analysis, we can conclude that study hours, attendance, sleep hours, and assignment completed have a positive correlation with test scores, while phone usage has a negative correlation with test scores. 
# This suggests that students who study more, attend classes regularly, get enough sleep, and complete their assignments tend to perform better in tests, while excessive phone usage can negatively impact their performance.