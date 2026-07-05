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


def sales_by_month(df):
    """Sales summed per calendar month, ordered chronologically.

    Returns a DataFrame with columns 'month' (Timestamp) and 'sales'.
    """
    grouped = df.groupby(df["date"].dt.to_period("M"))["total_amount"].sum()
    result = grouped.reset_index()
    result.columns = ["month", "sales"]
    result["month"] = result["month"].dt.to_timestamp()
    return result


def sales_by_category(df):
    """Sales per product category, sorted highest to lowest."""
    grouped = df.groupby("category")["total_amount"].sum()
    result = grouped.sort_values(ascending=False).reset_index()
    result.columns = ["category", "sales"]
    return result


def sales_by_region(df):
    """Sales per geographic region, sorted highest to lowest."""
    grouped = df.groupby("region")["total_amount"].sum()
    result = grouped.sort_values(ascending=False).reset_index()
    result.columns = ["region", "sales"]
    return result
