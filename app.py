import streamlit as st

import data

st.set_page_config(page_title="ShopSmart Sales Dashboard", layout="wide")
st.title("ShopSmart Sales Dashboard")


@st.cache_data
def get_data():
    return data.load_data("data/sales-data.csv")


df = get_data()

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${data.total_sales(df):,.0f}")
col2.metric("Total Orders", f"{data.total_orders(df):,}")
