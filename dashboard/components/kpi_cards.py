import streamlit as st
from utils.data_loader import load_dashboard_data


def show_kpis(state, category, year):

    df = load_dashboard_data()

    if state != "All":
        df = df[df["state"] == state]

    if category != "All":
        df = df[df["category_name"] == category]

    if year != "All":
        df = df[df["Year"] == year]

    revenue = df["Revenue"].sum()
    profit = df["Profit"].sum()
    orders = df["order_id"].nunique()
    customers = df["customer_id"].nunique()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Revenue", f"₹ {revenue:,.0f}")
    c2.metric("Profit", f"₹ {profit:,.0f}")
    c3.metric("Orders", f"{orders:,}")
    c4.metric("Customers", f"{customers:,}")