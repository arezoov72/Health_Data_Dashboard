# utils.py
import pandas as pd

def load_data(csv_path="diabetes.csv"):
    """
    Load the diabetes data from a CSV file.
    """
    return pd.read_csv(csv_path)

def calculate_bmi_stats(df):
    return {
        "Mean BMI": round(df["BMI"].mean(), 2),
        "Max BMI": round(df["BMI"].max(), 2),
        "Min BMI": round(df["BMI"].min(), 2)
    }

def get_top_patients_by_bmi(df, top_n=5):
    return df.sort_values(by="BMI", ascending=False).head(top_n)
