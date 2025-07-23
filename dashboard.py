# dashboard.py
import streamlit as st
from utils import load_data, calculate_bmi_stats, get_top_patients_by_bmi

st.set_page_config(page_title="🩺 Diabetes Dashboard", layout="centered")
st.title("🩺 Diabetes Health Data Dashboard")

# Load CSV data
df = load_data()

st.subheader("📊 Raw Data Sample")
st.dataframe(df.head())

# BMI Statistics
if "BMI" in df.columns:
    st.subheader("📈 BMI Statistics")
    bmi_stats = calculate_bmi_stats(df)
    st.json(bmi_stats)

    st.subheader("🔥 Top 5 Patients with Highest BMI")
    top_bmi = get_top_patients_by_bmi(df)
    st.table(top_bmi[["BMI", "Age"] if "Age" in df.columns else "BMI"])
else:
    st.warning("BMI column not found in the CSV.")
