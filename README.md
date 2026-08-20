# 🎓 Student Study Efficiency Analyzer

A Python-based data analysis project that explores the relationship between different academic and lifestyle factors and student test performance.

The project analyzes factors such as study hours, sleep, attendance, phone usage, assignment completion, breaks taken, and previous academic performance.

The dataset used in this project was synthetically generated using NumPy. Data-quality issues were intentionally introduced to simulate a realistic data-cleaning and analysis workflow.

---

## 📌 Project Objective

The goal of this project is to explore how different factors are associated with student test scores.

The analysis attempts to answer questions such as:

- Does studying more relate to higher test scores?
- How is sleep associated with academic performance?
- Does attendance have a relationship with test scores?
- How does phone usage relate to student performance?
- Do students who complete more assignments tend to score higher?
- Can students with high study hours but low scores be identified?
- Can multiple factors be combined into a custom efficiency score?

> **Note:** This project explores correlations and patterns within a synthetic dataset. The results should not be interpreted as evidence of causation.

---

## 📊 Dataset

The dataset was synthetically generated using NumPy and initially contained approximately 200 student records.

### Features

| Column | Description |
|---|---|
| `Student_id` | Unique identifier for each student |
| `Study_hours` | Number of hours spent studying |
| `Sleep_hours` | Number of hours of sleep |
| `Attendance` | Student attendance percentage |
| `Phone_usage` | Estimated phone usage |
| `Assignment_completed` | Number of assignments completed |
| `Breaks_taken` | Number of breaks taken while studying |
| `Previous_scores` | Previous academic score |
| `Test_scores` | Final test score |

---

## 🧹 Data Cleaning

To simulate real-world data, several data-quality issues were intentionally introduced into the dataset.

These included:

- Missing values
- Invalid sleep-hour values
- Non-numeric attendance values
- Duplicate student records

The following cleaning steps were performed:

1. Identified missing values.
2. Handled missing phone-usage values.
3. Identified and corrected invalid sleep-hour values.
4. Converted attendance values into numeric format.
5. Handled invalid attendance values.
6. Identified and removed duplicate records.

After cleaning, the dataset contained **190 valid student records**.

---

## 🔍 Analysis Performed

The project includes:

- Exploratory Data Analysis
- Descriptive statistics
- Student performance categorization
- Correlation analysis
- Comparison of study habits and test scores
- Anomaly detection
- Custom student efficiency scoring
- Data visualization

---

## 📈 Key Findings

Some of the main findings from the analysis were:

- The average test score was **54.19**.
- **18 students** scored above 80.
- Study hours had the strongest positive correlation with test scores at approximately **0.61**.
- Students studying more than 4 hours had an average test score of **62.64**, approximately **15.6% higher than the overall average**.
- Phone usage showed a strong negative correlation with test scores at approximately **-0.59**.
- Attendance and assignment completion showed weak positive correlations with test scores.
- Sleep hours also showed a weak positive relationship with test scores.
- **9 students** studied for more than 6 hours but still scored below 50, demonstrating that study time alone does not fully explain academic performance.

For a detailed analysis and discussion of the results, see [`FINAL_REPORT.md`](FINAL_REPORT.md).

---

## ⚡ Custom Efficiency Score

A custom student efficiency score was created by combining multiple academic and lifestyle factors.

The score considers factors such as:

- Study hours
- Sleep hours
- Attendance
- Assignment completion
- Phone usage
- Breaks taken
- Previous academic performance

The purpose of this score was to experiment with combining multiple variables into a single metric.

> This efficiency score is an exploratory metric created for this project and is not scientifically validated.

---

## 📊 Visualizations

The analysis includes visualizations exploring:

- Study Hours vs Test Scores
- Sleep Hours vs Test Scores
- Phone Usage vs Test Scores
- Attendance vs Test Scores
- Student Performance Distribution
- Average Test Score by Performance Category

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

---

## 📂 Project Structure

```text
Student-Study-Efficiency-Analyzer/
│
├── data.py                  # Generates the synthetic dataset
├── CleaningData.py          # Cleans and processes the dataset
├── Analysis.py              # Performs data analysis and visualization
│
├── Dataset.csv              # Original generated dataset
├── Cleaned_Dataset.csv      # Cleaned dataset
│
├── README.md
├── FINAL_REPORT.md
├── requirements.txt
└── .gitignore

## 🚀 How to Run
1.Clone the Repo
    git clone <https://github.com/himla1/Student-Study-Efficiency-Analyzer>
2.Navigate to the project directory
3.Install the required libraries
    pip install -r requirements.txt
4.Generate the dataset
    python data.py
5.Clean the dataset
    python cleaningData.py
6.Run the analysis
    python Analysis.py

⚠️ Limitations

The dataset used in this project is synthetic and was generated using predefined relationships between variables.

Therefore, the findings should not be interpreted as real-world scientific evidence.

For example, a negative correlation between phone usage and test scores does not prove that phone usage causes lower academic performance.

The purpose of this project is to demonstrate practical skills in:

    Data generation
    Data cleaning
    Exploratory Data Analysis
    Correlation analysis
    Anomaly detection
    Data visualization

🔮 Future Improvements

Possible improvements include:

    Using a real-world student dataset
    Adding machine learning models to predict student performance
    Feature engineering
    Advanced anomaly detection
    Personalized study recommendations
    Interactive dashboards
    Converting the project into a web application

👨‍💻 Author : himla1

Built to practice and demonstrate skills in:

Python | NumPy | Pandas | Matplotlib | Seaborn | Data Cleaning | Exploratory Data Analysis
