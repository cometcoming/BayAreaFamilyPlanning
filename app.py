import streamlit as st

st.title("Bay Area Household Planner")

st.subheader("Necessary Information")

city = st.selectbox(
    "City of Interest",
    ["San Jose", "San Francisco", "Oakland", "Santa Clara", "Sunnyvale", "Mountain View", "Palo Alto", "Cupertino", "Milpitas", "Saratoga", "Los Gatos", "Daly City", "San Mateo", "Redwood City", "South San Francisco", "Burlingame", "Menlo Park", "Palo Alto", "Los Altos", "Foster City", "Berkeley", "Fremont", "Hayward", "Concord", "Richmond", "Pleasanton", "Walnut Creek", "Livermore", "Dublin", "Alameda", "San Leandro", "Antioch", "Pittsburg", "Martinez"]
)

adults = st.slider(
    "Number of Adults",
    1,
    10,
    2
)

children = st.slider(
    "Number of Children",
    0,
    5,
    0
)

for i in range(children):
    age = st.number_input(
        f"Child {i+1} Age",
        min_value=0,
        max_value=25
    )

vehicles = st.slider(
    "Number of Vehicles",
    0,
    5,
    1
)

for i in range(vehicles):
    with st.expander(f"Vehicle {i+1} Ownership Status"):
        status = st.radio("Ownership", ["Owned", "Leased", "Rented"], key=f"vehicle_radio_{i}", label_visibility="collapsed")

properties = st.slider(
    "Number of (Bay Area) Properties",
    0,
    5,
    1
)

for i in range(properties):
    with st.expander(f"Property {i+1} Ownership Status"):
        status = st.radio("Ownership", ["Owned", "Leased", "Rented"], key=f"property_radio_{i}", label_visibility="collapsed")

st.subheader("Recommended Information")



st.subheader("Optional Information")


st.write("### Your Inputs")

st.write("City:", city)
#st.write("Income:", income)
st.write("Children:", children)
st.write("Vehicles:", vehicles)
