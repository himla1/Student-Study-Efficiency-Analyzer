import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('Student Study Efficiency Analyzer/Cleaned_Dataset.csv')
print(data.info())

# Avg Test score
avg_test_score = data['Test_scores'].mean()
print(f"Average Test Score: {avg_test_score}")

#Students with above 80 test scores
above_80_students = data[data['Test_scores'] > 80]
print(f"Number of students with above 80 test scores: {len(above_80_students)}")

#Student's average test score with above 4 hours of sleep
avg_test_score_above_4_sleep = data[data['Sleep_hours'] > 4]['Test_scores'].mean()
print(f"Average Test Score of students with above 4 hours of sleep: {avg_test_score_above_4_sleep}")

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

Outstanding_O = data[data['Test_scores'] > 90]
Excellent_A = data[(data['Test_scores'] > 80) & (data['Test_scores'] <= 90)]
Great_B = data[(data['Test_scores'] > 70) & (data['Test_scores'] <= 80)]
Fair_C = data[(data['Test_scores'] > 60) & (data['Test_scores'] <= 70)]
Average_D = data[(data['Test_scores'] > 50) & (data['Test_scores'] <= 60)]
Below_Average_E = data[(data['Test_scores'] > 40) & (data['Test_scores'] <= 50)]
Need_Improvement_F = data[data['Test_scores'] <= 40]
print(f"Category")
print(f"Outstanding_O: {len(Outstanding_O)} Students")
print(f"Excellent_A: {len(Excellent_A)} Students")
print(f"Great_B: {len(Great_B)} Students")
print(f"Fair_C: {len(Fair_C)} Students")
print(f"Average_D: {len(Average_D)} Students")
print(f"Below_Average_E: {len(Below_Average_E)} Students")
print(f"Need_Improvement_F: {len(Need_Improvement_F)} Students")

students_with_morethan4_study_hours = data[data['Study_hours'] > 4]
print(f"Average Test Score for Students with More than 4 Study Hours: {students_with_morethan4_study_hours['Test_scores'].mean()}")
print(f"students studying more than 4 hours score {((students_with_morethan4_study_hours['Test_scores'].mean()-avg_test_score)/avg_test_score)*100:.2f}% higher on average.")

#anomaly detection
students_with_anomalies = data[(data['Study_hours'] > 6) & (data['Test_scores'] <50)]
print(f"Number of students with anomalies (Study hours > 6 and Test scores < 50): {len(students_with_anomalies)}")
# why?
print(students_with_anomalies[['Student_id', 'Study_hours', 'Phone_usage', 'Sleep_hours','Test_scores']])
#Students scored less than 50 even after studying for more than 6 hours, which is an anomaly. This could be due to excessive phone usage or lack of sleep.

#Efficiency analysis
efficiency_score = np.clip(
    (data['Study_hours'] *5) +          
    (data['Sleep_hours'] *4) +          
    (data['Attendance'] /4) +      
    (data['Assignment_completed'] *2) - 
    (data['Phone_usage'] *2) -          
    (data['Breaks_taken'] *1.5) +         
    (data['Previous_scores'] * 0.3),       
    0, 100
)
print(f"Efficiency Score calculated for each student:\n{efficiency_score.to_string()}")

#Visualization of Efficiency Score vs Test Scores
sns.scatterplot(x='Study_hours', y='Test_scores', data=data, hue='Attendance')
plt.title('Study Hours vs Test Scores')
plt.show()

sns.scatterplot(x='Sleep_hours', y='Test_scores', data=data, hue='Phone_usage')    
plt.title('Sleep Hours vs Test Scores')
plt.show() 

sns.scatterplot(x='Phone_usage', y='Test_scores', data=data, hue='Sleep_hours')
plt.title('Phone Usage vs Test Scores')
plt.show()

sns.scatterplot(x='Attendance', y='Test_scores', data=data, hue='Assignment_completed')
plt.title('Attendance vs Test Scores')
plt.show()

bins = [0, 40, 50, 60, 70, 80, 90, 100]
labels = ['Need_Improvement_F', 'Below_Average_E', 'Average_D', 'Fair_C', 'Great_B', 'Excellent_A', 'Outstanding_O']
data['Performance_Category'] = pd.cut(data['Test_scores'], bins=bins, labels=labels)

plt.figure(figsize=(10,6))
sns.countplot(x='Performance_Category', data=data, palette='viridis')
plt.title('Student Distribution by Performance Category')
plt.xlabel('Performance Category')
plt.ylabel('Number of Students')
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(x='Performance_Category', y='Test_scores', data=data, palette='coolwarm', estimator='mean')
plt.title('Average Test Score by Performance Category')
plt.xlabel('Performance Category')
plt.ylabel('Average Test Score')
plt.show()

