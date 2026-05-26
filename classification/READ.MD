# 🔵 Logistic Regression — Purchase Prediction

Predict whether a user will purchase a product based on Age and Salary.

---

## 📁 Files
- `logistic_regression.ipynb` — Main notebook
- `logit classification.csv` — Dataset

---

## 🧠 Key Concepts

**Classification**
Predicting a category/label instead of a number.
- Regression → predicts number (salary, price)
- Classification → predicts category (yes/no, spam/not spam)

**Logistic Regression**
A classification algorithm that predicts the probability of a class (0 or 1).
Uses sigmoid function to output values between 0 and 1.
```
if probability > 0.5 → class 1 (Purchased)
if probability < 0.5 → class 0 (Not Purchased)
```

**Confusion Matrix**
A table that shows how many predictions were correct and incorrect.
```
                  Predicted 0    Predicted 1
Actual 0       True Negative   False Positive
Actual 1      False Negative    True Positive
```
- **True Positive (TP)** → Predicted Purchased, Actually Purchased ✅
- **True Negative (TN)** → Predicted Not Purchased, Actually Not Purchased ✅
- **False Positive (FP)** → Predicted Purchased, Actually Not Purchased ❌
- **False Negative (FN)** → Predicted Not Purchased, Actually Purchased ❌

**Accuracy** → Out of all predictions, how many were correct?
```
Accuracy = (TP + TN) / Total
```

**Precision** → Out of all predicted positive, how many were actually positive?
```
Precision = TP / (TP + FP)
```

**Recall** → Out of all actual positives, how many did we correctly predict?
```
Recall = TP / (TP + FN)
```

**F1 Score** → Balance between Precision and Recall
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

---

## 🗃️ Dataset
| Column | Description |
|--------|-------------|
| User ID | Unique user ID (dropped) |
| Gender | Male / Female (dropped) |
| Age | Age of user → ✅ used |
| EstimatedSalary | Estimated salary → ✅ used |
| Purchased | 0 = Not Purchased, 1 = Purchased 🎯 |

- **Rows:** 400
- **Train / Test Split:** 80% / 20% → 320 train, 80 test

---

## 🔄 Steps
1. Load dataset
2. Select features → `Age`, `EstimatedSalary`
3. Train test split
4. Feature scaling → `StandardScaler`
5. Train `LogisticRegression`
6. Predict on test data
7. Evaluate — Confusion Matrix, Accuracy, Classification Report

---

## 📊 Results

### Confusion Matrix
```
[[57,  1],
 [ 5, 17]]
```
- **57** → Correctly predicted Not Purchased ✅
- **17** → Correctly predicted Purchased ✅
- **1**  → Predicted Purchased but actually Not Purchased ❌
- **5**  → Predicted Not Purchased but actually Purchased ❌

### Metrics
| Metric | Value |
|--------|-------|
| Accuracy | **92.5%** |
| Precision (class 1) | 0.94 |
| Recall (class 1) | 0.77 |
| F1 Score (class 1) | 0.85 |

---

## 🛠️ Libraries
`pandas` `numpy` `matplotlib` `scikit-learn`