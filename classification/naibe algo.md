# 🔵 Naive Bayes — Purchase Prediction

Comparing 3 Naive Bayes algorithms on the same dataset.

---

## 📁 Files
- `naiva_bayes.ipynb` — Main notebook
- `logit classification.csv` — Dataset (400 rows)

---

## 🧠 What is Naive Bayes?
A classification algorithm based on **Bayes Theorem**.
It assumes all features are **independent** of each other (that's why "Naive").
Fast, simple, works well even with small data.

---

## 3 Types of Naive Bayes

### 1️⃣ GaussianNB
- Used when features are **continuous numbers**
- Assumes data follows a **normal distribution**
- Example: Age, Salary, Height, Weight
- **Needs StandardScaler** ✅

### 2️⃣ MultinomialNB
- Used for **count-based data** like word counts in text
- Example: Spam detection, document classification
- **Needs MinMaxScaler** (values must be ≥ 0) ✅

### 3️⃣ BernoulliNB
- Used when features are **binary (0 or 1)**
- Example: word present or not present
- **No scaling needed** ❌

---

## 📏 Scaling Summary

| Model | Scaling Needed | Scaler |
|-------|---------------|--------|
| GaussianNB | ✅ Yes | `StandardScaler` |
| MultinomialNB | ✅ Yes | `MinMaxScaler` (no negatives) |
| BernoulliNB | ❌ No | None |

---

## 📊 Results

| Model | Accuracy | Best For |
|-------|----------|---------|
| **GaussianNB** | **91.25%** 🏆 | Continuous features |
| BernoulliNB | 82.5% | Binary features |
| MultinomialNB | 72.5% ❌ | Text/count data |

---

## ⚠️ Why MultinomialNB scored low?
MultinomialNB is designed for **text/count data** — not for continuous features like Age and Salary. Using it here is the wrong choice for this dataset. Confusion matrix shows it predicted **class 0 for everything** — that's why accuracy is low.

---

## 🏆 Best Model
**GaussianNB** with **91.25%** — correct choice for continuous numeric features! ✅

---

## 🛠️ Libraries
`pandas` `numpy` `scikit-learn` `matplotlib`