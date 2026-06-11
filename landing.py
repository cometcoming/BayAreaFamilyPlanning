import streamlit as st

st.title("Bay Area Household Planner")

col1, col2 = st.columns(2)

with col1:
    if st.button("Future Planning Simulator"):
        st.switch_page("pages/1_Future_Planning.py")

with col2:
    if st.button("Current Budget Analyzer"):
        st.switch_page("pages/2_Budget_Analyzer.py")