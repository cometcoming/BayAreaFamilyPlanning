import streamlit as st

st.title("Bay Area Household Planner")

city = st.selectbox(
    "City",
    ["San Francisco", "San Jose", "Oakland"]
)

income = st.number_input(
    "Annual Household Income",
    min_value=0,
    value=100000
)

children = st.slider(
    "Number of Children",
    0,
    5,
    0
)

vehicles = st.slider(
    "Number of Vehicles",
    0,
    5,
    1
)

st.write("### Your Inputs")

st.write("City:", city)
st.write("Income:", income)
st.write("Children:", children)
st.write("Vehicles:", vehicles)
