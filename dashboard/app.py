import streamlit as st

from components.kpi_cards import show_kpis
from components.charts import (
    monthly_sales_chart,
    category_sales_chart
)

st.set_page_config(
    page_title="Retail Sales Intelligence",
    layout="wide"
)

st.title("📊 Retail Sales Intelligence Dashboard")

st.divider()

show_kpis()

st.divider()

col1, col2 = st.columns(2)

with col1:
    monthly_sales_chart()

with col2:
    category_sales_chart()