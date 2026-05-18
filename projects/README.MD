# 🏠 USA House Price Prediction

## 📁 Dataset
- **File:** USA_Housing.csv
- **Rows:** 5000
- **Columns:** 7
- **Target:** Price (USD)
- **Train / Test Split:** 80% / 20% → 4000 train, 1000 test

### Features
| Column | Description |
|--------|-------------|
| Avg. Area Income | Average income of residents in the area ($) |
| Avg. Area House Age | Average age of houses in the area (years) |
| Avg. Area Number of Rooms | Total rooms (bedroom + kitchen + living room + bathroom etc.) |
| Avg. Area Number of Bedrooms | Only sleeping rooms |
| Area Population | Total population of the area |
| Address | Street address (dropped before training) |
| Price | 🎯 Target — house price in USD |

> **Note:** Rooms > Bedrooms always — bedrooms are a subset of total rooms

---

## 📊 Model Evaluation Results
> Sorted by R² score — best to worst

| Rank | Model | MAE | RMSE | R² |
|------|-------|-----|------|----|
| 🥇 1 | Lasso | $82,657 | $102,711 | 0.9146 |
| 🥇 2 | Linear Regression | $82,657 | $102,711 | 0.9146 |
| 🥈 3 | Ridge | $82,659 | $102,712 | 0.9146 |
| 4 | Polynomial Regression | $83,413 | $103,270 | 0.9137 |
| 5 | LightGBM | $92,133 | $114,445 | 0.8940 |
| 6 | Random Forest | $98,102 | $122,229 | 0.8791 |
| 7 | XGBoost | $125,545 | $159,015 | 0.7954 |
| 8 | KNN | $198,086 | $245,755 | 0.5113 |
| 9 | ANN | $199,315 | $248,156 | 0.5017 |
| 10 | Huber Regressor | $199,465 | $248,324 | 0.5010 |
| 11 | SVR | $282,947 | $351,491 | 0.0004 |
| ❌ 12 | SGD Regressor | very high | very high | negative |

---

## 🏆 Best Model
**Linear Regression / Lasso** — R² of **0.9146** meaning the model explains **91.46%** of the variance in house prices!

---

## ❌ Worst Model
**SGD Regressor** — R² is **negative** which means it performs worse than a simple mean prediction.
This is because SGD Regressor needs **feature scaling** (StandardScaler) before training.



---

## 🤖 Models Used (12 Models)
| # | Model | Library |
|---|-------|---------|
| 1 | Linear Regression | sklearn |
| 2 | Lasso | sklearn |
| 3 | Ridge | sklearn |
| 4 | SVR | sklearn |
| 5 | KNN | sklearn |
| 6 | Random Forest | sklearn |
| 7 | Huber Regressor | sklearn |
| 8 | LightGBM | lightgbm |
| 9 | XGBoost | xgboost |
| 10 | SGD Regressor | sklearn |
| 11 | ANN (MLPRegressor) | sklearn |
| 12 | Polynomial Regression (degree=4) | sklearn |

---

## 📐 Evaluation Metrics Used

### MAE — Mean Absolute Error
```
MAE = (1/n) × Σ |y_actual - y_predicted|
```

### MSE — Mean Squared Error
```
MSE = (1/n) × Σ (y_actual - y_predicted)²
```

### RMSE — Root Mean Squared Error
```
RMSE = √MSE
```

### R² Score
```
R² = 1 - (SS_residual / SS_total)
```

---

## 🖥️ Streamlit App
```bash
streamlit run app.py
```
Enter house details → Select model → Click **Predict Price** 🔍

---

## 📂 Project Structure
```
projects/
├── datasets/
│   └── USA_Housing.csv
├── app.py
├── house_price_pred.ipynb
├── model_evalution_result.csv
├── LinearRegression.pkl
├── Lasso.pkl
├── Ridge.pkl
├── SVR.pkl
├── KNN.pkl
├── RandomForestRegressor.pkl
├── HuberRegressor.pkl
├── Lightgb.pkl
├── xgboost.pkl
├── SGDRegressor.pkl
├── ANN.pkl
├── PolynomialRegressor.pkl
└── README.md
```