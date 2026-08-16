import numpy as np
import pandas as pd
np.random.seed(3)
student_id=np.random.permutation(np.arange(1,201))
study_hours=np.random.randint(1,11,200)
sleep_hours=np.random.randint(2,7,200)
attendance=np.random.randint(0,100,200)
phone_usage = 12 - study_hours +np.random.randint(0,2,200)
assignment_completed = np.random.randint(0,10,200)
breaks_taken = np.clip(12 - study_hours*2 + np.random.randint(0,2,200), 0, 10)
previous_scores = np.random.randint(0,100,200)
test_scores =np.clip((study_hours*3 + sleep_hours*2 + attendance*1 - phone_usage*2 + assignment_completed*1.5 - breaks_taken*2 + previous_scores*0.3)  ,0,100)
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
dup1=Data.loc[5]
dup2=Data.loc[10]
dup3=Data.loc[54]
Data.loc[150] = dup1
Data.loc[181] = dup2
Data.loc[135] = dup3
Data.to_csv('Dataset.csv', index=False)
