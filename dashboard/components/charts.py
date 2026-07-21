import streamlit as st
import plotly.express as px

from utils.queries import (
    monthly_sales,
    category_sales,
    state_sales,
    top_products,
    payment_methods,
    return_analysis
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

def state_sales_chart():

    df = state_sales()

    fig = px.bar(
        df,
        x="state",
        y="revenue",
        title="Revenue by State"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def top_products_chart():

    df = top_products()

    fig = px.bar(
        df,
        x="product_name",
        y="revenue",
        title="Top 10 Products"
    )

    fig.update_layout(
        xaxis_tickangle=-45
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

def payment_methods_chart():

    df = payment_methods()

    fig = px.pie(
        df,
        names="payment_method",
        values="total",
        title="Payment Methods"
    )

    st.plotly_chart(fig, use_container_width=True)


def return_analysis_chart():

    df = return_analysis()

    fig = px.pie(
        df,
        names="return_reason",
        values="total",
        title="Return Reasons"
    )

    st.plotly_chart(fig, use_container_width=True)