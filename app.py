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

left, right = st.columns(2)

with left:
    st.subheader("Sales by Category")
    category = data.sales_by_category(df)
    cat_chart = px.bar(category, x="sales", y="category", orientation="h")
    cat_chart.update_layout(
        xaxis_title="Sales ($)",
        yaxis_title="",
        yaxis={"categoryorder": "total ascending"},
    )
    st.plotly_chart(cat_chart, use_container_width=True)

with right:
    st.subheader("Sales by Region")
    region = data.sales_by_region(df)
    reg_chart = px.bar(region, x="sales", y="region", orientation="h")
    reg_chart.update_layout(
        xaxis_title="Sales ($)",
        yaxis_title="",
        yaxis={"categoryorder": "total ascending"},
    )
    st.plotly_chart(reg_chart, use_container_width=True)
