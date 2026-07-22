import streamlit as st
import plotly.express as px


def monthly_sales_chart(df):

    monthly = (
        df.groupby("Year", as_index=False)["Revenue"]
        .sum()
        .rename(columns={"Revenue": "revenue"})
    )

    fig = px.line(
        monthly,
        x="Year",
        y="revenue",
        markers=True,
        title="Monthly Sales Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

def category_sales_chart(df):

    category_df = (
        df.groupby("category_name", as_index=False)["Revenue"]
        .sum()
        .rename(columns={"Revenue": "revenue"})
        .sort_values("revenue", ascending=False)
    )

    fig = px.bar(
        category_df,
        x="category_name",
        y="revenue",
        title="Revenue by Category"
    )

    st.plotly_chart(fig, use_container_width=True)

def state_sales_chart(df):

    state_df = (
        df.groupby("state", as_index=False)["Revenue"]
        .sum()
        .rename(columns={"Revenue": "revenue"})
        .sort_values("revenue", ascending=False)
    )

    fig = px.bar(
        state_df,
        x="state",
        y="revenue",
        title="Revenue by State"
    )

    st.plotly_chart(fig, use_container_width=True)


def top_products_chart(df):

    product_df = (
        df.groupby("product_name", as_index=False)["Revenue"]
        .sum()
        .rename(columns={"Revenue": "revenue"})
        .sort_values("revenue", ascending=False)
        .head(10)
    )

    fig = px.bar(
        product_df,
        x="product_name",
        y="revenue",
        title="Top 10 Products"
    )

    fig.update_layout(xaxis_tickangle=-45)

    st.plotly_chart(fig, use_container_width=True)

def payment_methods_chart(df):

    payment_df = (
        df.groupby("payment_method", as_index=False)
        .size()
        .rename(columns={"size": "total"})
    )

    fig = px.pie(
        payment_df,
        names="payment_method",
        values="total",
        title="Payment Methods"
    )

    st.plotly_chart(fig, use_container_width=True)

def return_analysis_chart(df):

    return_df = (
        df[df["return_reason"].notna()]
        .groupby("return_reason", as_index=False)
        .size()
        .rename(columns={"size": "total"})
    )

    fig = px.pie(
        return_df,
        names="return_reason",
        values="total",
        title="Return Reasons"
    )

    st.plotly_chart(fig, use_container_width=True)