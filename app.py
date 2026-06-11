import streamlit as st

st.markdown('<p style="font-size: 60px; font-weight: bold;">Bay Area Household Planner</p>', unsafe_allow_html=True)
st.text("Disclaimer: Not meant to be taken completely seriously as financial advice, simply a tool for financial planning in the Bay Area.")

st.space("medium")

st.subheader("Location")

city = st.selectbox(
    "City of Interest",
    ["San Jose", "San Francisco", "Oakland", "Santa Clara", "Sunnyvale", "Mountain View", "Palo Alto", "Cupertino", "Milpitas", "Saratoga", "Los Gatos", "Daly City", "San Mateo", "Redwood City", "South San Francisco", "Burlingame", "Menlo Park", "Palo Alto", "Los Altos", "Foster City", "Berkeley", "Fremont", "Hayward", "Concord", "Richmond", "Pleasanton", "Walnut Creek", "Livermore", "Dublin", "Alameda", "San Leandro", "Antioch", "Pittsburg", "Martinez"]
)

housing_market = st.radio(
    "Housing Market Level Preference",
    ["Basic", "Average", "Premium"],
    key=f"housing_market_radio"
)

st.subheader("Household")

adults = st.slider(
    "Number of Adults",
    1,
    10,
    2
)

for i in range(adults):
    age = st.number_input(
        f"Adult {i+1} Age",
        min_value=18,
        max_value=150
    )

#add occupation tab later

for i in range(adults):
    with st.expander(f"Adult {i+1} Occupation"):
        occ = st.radio("Occupation", ["Not employed", "Student", "Retired", "Stay-at-home", "Employed part-time", "Employed full-time", "Self-employed"], key=f"occ_radio_{i}", label_visibility="collapsed")

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

st.subheader("Housing")

properties = st.slider(
    "Number of (Bay Area) Properties",
    0,
    5,
    1
)

for i in range(properties):
    with st.expander(f"Property {i+1} Ownership Status"):
        status = st.radio("Ownership", ["Owned", "Leased", "Rented"], key=f"property_radio_{i}", label_visibility="collapsed")

for i in range(properties):
    with st.expander(f"Property {i+1} Housing Type"):
        housing = st.radio("Housing", ["Single-Family Home", "Townhome", "Condo", "Apartment"], key=f"property_housing_{i}", label_visibility="collapsed")

for i in range(properties):
    with st.expander(f"Property {i+1} Number of Bedrooms"):
        bedrooms = st.slider(
            "Number of Bedrooms",
            0,
            8,
            1, key=f"property_bedrooms{i}"
        )

for i in range(properties):
    with st.expander(f"Property {i+1} Monthly HOA Fee (if applicable)"):
        hoa_fee = st.number_input("Monthly HOA Fee (if applicable)", placeholder="____", key=f"property_hoa_fee{i}")

st.subheader("Vehicles")

vehicles = st.slider(
    "Number of Vehicles",
    0,
    5,
    1
)

for i in range(vehicles):
    with st.expander(f"Vehicle {i+1} Ownership Status"):
        status = st.radio("Ownership", ["Owned", "Leased", "Rented"], key=f"vehicle_radio_{i}", label_visibility="collapsed")

st.subheader("Employment and Income")

st.subheader("Debt")

st.subheader("Savings Goals")

st.subheader("Lifestyle")

lifestyle = st.radio(
    "Overall Preferred Lifestyle Level",
    ["Stable", "Moderate", "Luxury"],
    key=f"lifestyle_radio"
)

st.space("medium")

st.subheader("Recommended Information")



st.space("medium")

st.subheader("Optional Information")


st.write("### Your Inputs")

st.write("City:", city)
#st.write("Income:", income)
st.write("Children:", children)
st.write("Vehicles:", vehicles)
