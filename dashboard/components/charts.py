import streamlit as st
import plotly.express as px

from utils.queries import (
    monthly_sales,
    category_sales
)


def monthly_sales_chart():

    df = monthly_sales()

    fig = px.line(
        df,
        x="month",
        y="revenue",
        markers=True,
        title="Monthly Sales Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def category_sales_chart():

    df = category_sales()

    fig = px.bar(
        df,
        x="category_name",
        y="revenue",
        title="Revenue by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )