
---

# `FINAL_REPORT.md`

Create a new file called `FINAL_REPORT.md` and paste this:

```md
# 📊 Student Study Efficiency Analyzer – Final Report

## 1. Introduction

Student academic performance can be influenced by multiple academic and lifestyle factors.

This project analyzes the relationship between factors such as study hours, sleep, attendance, phone usage, assignment completion, breaks taken, and previous academic performance with student test scores.

The purpose of this project was to perform exploratory data analysis and identify patterns within the dataset.

This analysis focuses on relationships and correlations and does not attempt to prove causation.

---

## 2. Dataset

A synthetic dataset containing approximately 200 student records was created using NumPy.

The dataset included the following variables:

- Student ID
- Study hours
- Sleep hours
- Attendance
- Phone usage
- Assignments completed
- Breaks taken
- Previous scores
- Test scores

To simulate real-world data, several data-quality issues were intentionally introduced, including missing values, invalid values, incorrect data types, and duplicate records.

After the data-cleaning process, **190 valid student records** remained for analysis.

---

## 3. Data Cleaning

The following steps were performed to prepare the dataset for analysis:

### Missing Values

Missing values were identified and handled before performing the analysis.

### Invalid Sleep Values

Invalid sleep-hour values were identified and replaced using an appropriate statistical method.

### Invalid Attendance Values

Non-numeric attendance values were converted into missing values and handled using the median.

### Duplicate Records

Duplicate student records were identified and removed.

The cleaned dataset was then exported as `Cleaned_Dataset.csv`.

---

## 4. Exploratory Data Analysis

The dataset was explored using descriptive statistics and different filtering techniques.

The analysis included:

- Average test scores
- Number of high-performing students
- Study habits
- Performance categories
- Correlations between variables
- Identification of unusual student performance patterns

The overall average test score was:

**54.19**

A total of:

**18 students scored above 80.**

---

## 5. Correlation Analysis

Correlation analysis was performed to identify relationships between different variables and student test scores.

### Study Hours

Study hours showed the strongest positive relationship with test scores.

**Correlation: 0.61**

Students studying more than 4 hours had an average test score of:

**62.64**

This was approximately **15.6% higher than the overall average test score**.

This suggests that, within this dataset, students who studied more generally tended to achieve higher scores.

---

### Phone Usage

Phone usage showed a strong negative relationship with test scores.

**Correlation: -0.59**

Within this synthetic dataset, students with higher phone usage generally tended to have lower test scores.

However, this correlation does not prove that phone usage directly causes lower academic performance.

---

### Sleep Hours

Sleep hours showed a weak positive relationship with test scores.

**Correlation: 0.15**

Students sleeping less than 4 hours had an average test score of approximately:

**50.73**

This suggests that sleep may have some association with student performance, although the relationship was weaker compared to study hours and phone usage.

---

### Attendance

Attendance showed a weak positive correlation with test scores.

**Correlation: 0.19**

This suggests that higher attendance was somewhat associated with higher test scores within the dataset.

---

### Assignment Completion

Assignment completion also showed a weak positive correlation with test scores.

**Correlation: 0.19**

Students who completed more assignments generally showed a slightly positive association with academic performance.

---

## 6. Student Performance Distribution

Students were categorized according to their test scores.

The performance categories included:

| Performance Category | Number of Students |
|---|---:|
| Outstanding (>90) | 7 |
| Excellent (80–90) | 11 |
| Great (70–80) | 19 |
| Fair (60–70) | 34 |
| Average (50–60) | 41 |
| Below Average (40–50) | 34 |
| Needs Improvement (≤40) | 44 |

The largest group of students was in the **Average (50–60)** category.

---

## 7. Anomaly Analysis

The project also attempted to identify students whose study effort did not appear to match their academic performance.

Students who:

- Studied for more than 6 hours
- Scored below 50

were identified as potential anomalies.

A total of **9 students** matched this pattern.

This demonstrates that study duration alone may not fully explain academic performance.

Other factors such as sleep, phone usage, previous academic performance, study quality, and additional unmeasured factors may also contribute to student outcomes.

---

## 8. Custom Efficiency Score

A custom student efficiency score was created by combining multiple academic and lifestyle factors.

The score considered:

### Positive factors

- Study hours
- Sleep hours
- Attendance
- Assignment completion
- Previous scores

### Negative factors

- Phone usage
- Breaks taken

The purpose of this metric was to experiment with combining multiple variables into a single score that could provide a broader view of student efficiency.

This metric is exploratory and was designed specifically for this project. It should not be interpreted as a scientifically validated measure of student productivity or intelligence.

---

## 9. Conclusion

The analysis revealed several interesting relationships within the synthetic dataset.

Study hours showed the strongest positive relationship with test scores, while phone usage showed the strongest negative relationship.

Sleep, attendance, and assignment completion showed weaker positive relationships with academic performance.

The anomaly analysis also demonstrated that spending more time studying does not necessarily guarantee higher performance. Multiple factors may contribute to student outcomes.

This project provided practical experience in:

- Synthetic data generation
- Data cleaning
- Handling missing and invalid values
- Exploratory Data Analysis
- Correlation analysis
- Data filtering
- Anomaly detection
- Data visualization
- Creating custom analytical metrics

---

## 10. Limitations

This analysis has several limitations.

The dataset is synthetic and was generated using predefined relationships between variables.

Therefore:

- The results may not represent real student behavior.
- Correlation does not imply causation.
- Important factors such as study quality, teaching quality, mental state, socioeconomic factors, and learning style were not included.

The results should therefore be interpreted as an exploration of the synthetic dataset rather than real-world academic research.

---

## 11. Future Improvements

Possible future improvements include:

- Using real-world student data
- Adding additional relevant features
- Applying machine learning models to predict student performance
- Feature engineering
- Advanced anomaly detection
- Personalized study recommendations
- Building an interactive dashboard
- Developing a full-stack web application

---

## Final Takeaway

This project demonstrates a complete basic data-analysis workflow:

**Generate Data → Clean Data → Explore Data → Analyze Relationships → Identify Patterns → Visualize Results → Draw Conclusions**

The project was built to strengthen practical skills in Python, NumPy, Pandas, and data visualization.