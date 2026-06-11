import streamlit as st

st.title("Bay Area Household Planner")

col1, col2 = st.columns(2)

with col1:
    if st.button("Future Planning Simulator", key="prospective_btn"):
        st.switch_page("pages/prospective.py")

with col2:
    if st.button("Current Budget Analyzer", key="budget_btn"):
        st.switch_page("pages/budget.py")