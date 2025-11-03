import pandas as pd
import os

# Compute project-relative absolute paths so saving works regardless of CWD.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_PATH = os.path.join(DATA_DIR, "expenses.csv")


# ---- Load Data ----
def load_data():
    """
    Load the CSV if it exists. If not, return an empty DataFrame with the
    expected columns. This function does NOT create the file on disk; saving
    will create the directory if required.
    """
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    else:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])


# ---- Save Data ----
def save_data(df):
    """
    Ensure the data directory exists and save the DataFrame to CSV.
    """
    os.makedirs(DATA_DIR, exist_ok=True)
    df.to_csv(DATA_PATH, index=False)