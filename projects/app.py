import streamlit as st
import pandas as pd
import numpy as np
import pickle
# C:\Users\beher\anaconda3\anconda\envs\streamlit_env\Scripts\streamlit.exe run app.py
st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="wide")

# ---- exact model names from your notebook ----
model_names = [
    'LinearRegression', 'Lasso', 'Ridge', 'SVR', 'KNN',
    'RandomForestRegressor', 'HuberRegressor',
    'Lightgb', 'xgboost', 'SGDRegressor', 'ANN', 'PolynomialRegressor'
]

# ---- Load all models ----
models = {}
for name in model_names:
    try:
        with open(f'{name}.pkl', 'rb') as f:
            models[name] = pickle.load(f)
    except:
        pass

# ---- Page: Predict ----
st.title("🏠 USA House Price Predictor")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    avg_income     = st.number_input("Avg. Area Income ($)",          min_value=10000.0,  max_value=200000.0, value=68000.0,  step=1000.0)
    avg_age        = st.number_input("Avg. Area House Age (years)",   min_value=1.0,      max_value=20.0,     value=5.98,    step=0.1)
    avg_rooms      = st.number_input("Avg. Area Number of Rooms",     min_value=1.0,      max_value=15.0,     value=6.98,    step=0.1)

with col2:
    avg_bedrooms   = st.number_input("Avg. Area Number of Bedrooms",  min_value=1.0,      max_value=10.0,     value=3.98,    step=0.1)
    area_population= st.number_input("Area Population",               min_value=1000.0,   max_value=100000.0, value=36000.0, step=500.0)
    model_choice   = st.selectbox("Select Model", model_names)

st.markdown("---")

if st.button("🔍 Predict Price", use_container_width=True):
    input_df = pd.DataFrame([{
        'Avg. Area Income':               avg_income,
        'Avg. Area House Age':            avg_age,
        'Avg. Area Number of Rooms':      avg_rooms,
        'Avg. Area Number of Bedrooms':   avg_bedrooms,
        'Area Population':                area_population
    }])

    if model_choice in models:
        prediction = models[model_choice].predict(input_df)[0]
        st.success(f"🏡 Predicted House Price: **${prediction:,.0f}**")
    else:
        st.error(f"⚠️ {model_choice}.pkl not found — run your notebook first!")

# ---- Model Evaluation Table ----
st.markdown("---")
st.subheader("📊 Model Evaluation Results")

try:
    results_df = pd.read_csv('model_evalution_result.csv')
    results_df = results_df.sort_values('r2', ascending=False).reset_index(drop=True)
    results_df.index += 1
    st.dataframe(results_df, use_container_width=True)
    best = results_df.iloc[0]
    st.info(f"🏆 Best Model: **{best['model']}** with R² = **{best['r2']:.4f}**")
except:
    st.warning("⚠️ model_evalution_result.csv not found — run your notebook first!")