import streamlit as st

from components.kpi_cards import show_kpis
from components.sidebar import show_sidebar
from components.charts import (
    monthly_sales_chart,
    category_sales_chart,
    state_sales_chart,
    top_products_chart,
    payment_methods_chart,
    return_analysis_chart,
)

from utils.data_loader import load_dashboard_data


st.set_page_config(
    page_title="Retail Sales Intelligence",
    layout="wide"
)
state, category, year = show_sidebar()
df = load_dashboard_data()

# Apply filters
if state != "All":
    df = df[df["state"] == state]

if category != "All":
    df = df[df["category_name"] == category]

if year != "All":
    df = df[df["Year"] == year]

# Temporary testing
st.dataframe(df.head())

st.title("📊 Retail Sales Intelligence Dashboard")

st.divider()

show_kpis(state, category, year)

st.divider()

row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    monthly_sales_chart(df)

with row1_col2:
    category_sales_chart(df)

st.divider()

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    state_sales_chart(df)

with row2_col2:
    top_products_chart(df)

st.divider()

row3_col1, row3_col2 = st.columns(2)

with row3_col1:
    payment_methods_chart(df)

with row3_col2:
    return_analysis_chart(df)