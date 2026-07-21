import streamlit as st

from utils.filters import (
    get_states,
    get_categories,
    get_years
)


def show_sidebar():

    st.sidebar.title("🔍 Filters")

    state = st.sidebar.selectbox(
        "🌍 State",
        get_states()
    )

    category = st.sidebar.selectbox(
        "📦 Category",
        get_categories()
    )

    year = st.sidebar.selectbox(
        "📅 Year",
        get_years()
    )

    return state, category, year