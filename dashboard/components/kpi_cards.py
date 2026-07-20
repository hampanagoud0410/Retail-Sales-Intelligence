import streamlit as st

from utils.queries import (
    total_revenue,
    total_profit,
    total_orders,
    total_customers
)


def show_kpis():

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Revenue",
        f"₹ {total_revenue():,.0f}"
    )

    c2.metric(
        "Profit",
        f"₹ {total_profit():,.0f}"
    )

    c3.metric(
        "Orders",
        f"{total_orders():,}"
    )

    c4.metric(
        "Customers",
        f"{total_customers():,}"
    )