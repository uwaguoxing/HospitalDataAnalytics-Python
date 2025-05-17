
# Hospital Data Analysis

The project focuses on analyzing hospital datasets from multiple countries to compute health-related statistics, similarities, and trends.

---

## 📁 Repository Contents

- `analysis.py` – Main program file containing all logic and functions.
- `hospital_data.csv` – Sample dataset with hospital-level information across countries.
- `disease.txt` – Sample TXT file with case data for COVID, stroke, and cancer patients.
- *(Optional test files, e.g., `hospital_data_case_sensitivity.csv`, etc.)*

---

## 🧠 Project Tasks

### ✅ Task 1 – Country-Specific Hospital Data

Generates three dictionaries:
- `Country_to_hospitals`: country → list of hospital IDs
- `Country_to_death`: country → list of deaths (2022) per hospital
- `Country_to_covid&stroke`: country → list of COVID + stroke cases (2022) per hospital

### ✅ Task 2 – Cosine Similarity

For each country, computes the **cosine similarity** between:
- Number of deaths in 2022
- Total COVID + stroke admissions (2022)

Result is a dictionary:  
`Cosine_dict[country] = cosine_similarity_value`

### ✅ Task 3 – Variance in Cancer Admissions

For a given hospital category (e.g. `'children'`), computes:
- Variance of cancer admission numbers per country

Result is a dictionary:  
`Variance_dict[country] = variance_value`

### ✅ Task 4 – Hospital Category Statistics

Builds a nested dictionary structure:  
```python
{
  'category': {
    'country': [
      avg_female_patients,
      max_staff_count,
      percentage_change_in_deaths_2022_to_2023
    ],
    ...
  },
  ...
}

# 🚀 How to Use

## In Python

```python
from analysis import main

OP1, OP2, OP3, OP4 = main("hospital_data.csv", "disease.txt", "children")
```

## 📤 Sample Output

```python
>>> OP1[0]['canada']
['a1b2c3', 'd4e5f6']

>>> OP2['canada']
0.7632

>>> OP3['canada']
25401.23

>>> OP4['children']['canada']
[3925.4, 4448, 22.0588]
```

---

## 📌 Requirements

- ✅ Written in pure Python 3  
- ❌ No external modules (e.g., no `csv`, `math`, or `pandas`)  
- ❌ Do not use `input()` or `print()` (except for error messages)  
- ✅ Case-insensitive matching of strings  
- ✅ Graceful handling of invalid/missing data  

---

## 🎯 Goals

- Practice structured programming  
- Perform text file parsing manually  
- Implement vector similarity, variance, and percentage change calculations  
- Handle irregular and incomplete data inputs  

---

