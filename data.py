import numpy as np
import pandas as pd
np.random.seed(6)
student_id=np.random.permutation(np.arange(1,201))
study_hours=np.random.randint(1,11,200)
sleep_hours=np.random.randint(2,7,200)
attendance=np.random.randint(0,100,200)
phone_usage = 15 - study_hours +np.random.randint(0,2,200)
assignment_completed = np.random.randint(0,10,200)
breaks_taken = np.clip(12 - study_hours*2 + np.random.randint(0,2,200), 0, 10)
previous_scores = np.random.randint(0,100,200)
test_scores = np.clip(
    study_hours * 3 +
    sleep_hours * 3 +
    (attendance / 10) * 2.0 -
    phone_usage * 1 +
    assignment_completed * 1.8 -
    breaks_taken * 0.5 +
    previous_scores * 0.4 +
    np.random.normal(0, 5, len(study_hours)),
    0, 100
)
Data=pd.DataFrame({
    'Student_id': student_id,
    'Study_hours': study_hours,
    'Sleep_hours': sleep_hours,
    'Attendance': attendance,
    'Phone_usage': phone_usage,
    'Assignment_completed': assignment_completed,
    'Breaks_taken': breaks_taken,
    'Previous_scores': previous_scores,
    'Test_scores': test_scores
})
nan_indices = np.random.choice(Data.index, size=10, replace=False)
Data.loc[nan_indices, 'Phone_usage'] = np.nan
wrong_indices = np.random.choice(Data.index, size=10, replace=False)
Data.loc[wrong_indices, 'Sleep_hours'] = 50
Data['Attendance'] = Data['Attendance'].astype(object)
Data.loc[86, 'Attendance'] = 'ten'
Data.loc[136, 'Attendance'] = 'twenty'
Data = pd.concat([Data, Data.loc[[5,10,54]]], ignore_index=True)
Data.to_csv('Dataset.csv', index=False)
