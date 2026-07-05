import pandas as pd


def load_data(path):
    """Read the sales CSV and return a DataFrame with a parsed date column."""
    return pd.read_csv(path, parse_dates=["date"])


def total_sales(df):
    """Total revenue across all transactions."""
    return float(df["total_amount"].sum())


def total_orders(df):
    """Number of transactions."""
    return int(len(df))
