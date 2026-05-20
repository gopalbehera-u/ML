# 📚 Student Mark Predictor

Predict student marks based on study hours using Linear Regression.

---

## 📁 Files
- `markPredictor.ipynb` — Main notebook
- `student_info.csv` — Dataset

---

## 🗃️ Dataset
| Column | Description |
|--------|-------------|
| study_hours | Hours a student studies per day |
| student_marks | Marks scored by the student 🎯 |

- **Rows:** 200
- **Missing values:** 5 in `study_hours` → filled with mean (6.99)
- **Train / Test Split:** 80% / 20% → 160 train, 40 test

---

## 🔄 Steps
1. Load dataset
2. EDA — scatter plot (study hours vs marks)
3. Data cleaning — fill missing values with mean
4. Train test split
5. Train Linear Regression
6. Predict & compare actual vs predicted
7. Evaluate metrics
8. Visualize regression line

---

## 📐 Model — Linear Regression
```
Marks = (3.93 × study_hours) + 50.45
```
- **Coefficient:** 3.93 → every 1 extra hour = +3.93 marks
- **Intercept:** 50.45

**Sample prediction:**
```python
lr.predict([[4]])  →  66.17 marks
```

---

## 📊 Results

| Metric | Value |
|--------|-------|
| R² Score | **0.87** |
| MAE | ~1.8 marks |
| RMSE | ~2.2 marks |

Model explains **87% of variance** in student marks — good fit! ✅

---

## 🛠️ Libraries
`pandas` `numpy` `matplotlib` `scikit-learn`