import streamlit as st
import plotly.express as px

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

st.subheader("Sales Trend Over Time")
monthly = data.sales_by_month(df)
trend = px.line(monthly, x="month", y="sales", markers=True)
trend.update_layout(xaxis_title="Month", yaxis_title="Sales ($)")
st.plotly_chart(trend, use_container_width=True)
