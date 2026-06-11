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

st.subheader("Transportation")

vehicles = st.slider(
    "Number of Private Vehicles",
    0,
    5,
    1
)

for i in range(vehicles):
    with st.expander(f"Vehicle {i+1} Ownership Status"):
        status = st.radio("Ownership", ["Owned", "Leased", "Rented"], key=f"vehicle_radio_{i}", label_visibility="collapsed")

with st.expander("Public Transit"):
    transit_usage = st.radio(
        "Transit usage",
        ["None", "Occasional", "Regular commuter"],
        key="transit_usage",
        horizontal=True,
    )

    if transit_usage == "None":
        transit_cost = 0
    else:
        default_cost = 81 if transit_usage == "Regular commuter" else 20
        transit_cost = st.number_input(
            "Monthly public transit cost ($)",
            min_value=0,
            value=default_cost,
            step=5,
            key="transit_monthly_cost",
            help="Include passes, Clipper loads, BART/Muni/Caltrain, etc.",
        )

st.subheader("Employment and Income")



st.subheader("Household Debt")

stu_debt = st.number_input("Monthly Student Loan Debt", placeholder="____", key=f"stu_debt")
car_debt = st.number_input("Monthly Auto Loan Debt", placeholder="____", key=f"car_debt")
home_debt = st.number_input("Monthly Home Loan Debt", placeholder="____", key=f"home_debt")
credit_card_debt = st.number_input("Monthly Credit Card Debt", placeholder="____", key=f"credit_card_debt")
other_debt = st.number_input("Monthly Other Debt", placeholder="____", key=f"other_debt")

total_debt = stu_debt + car_debt + home_debt + credit_card_debt + other_debt

st.subheader("Savings Goals")

emergency_fund_savings = st.number_input("Monthly Emergency Fund Savings", placeholder="____", key=f"emergency_fund_savings")
with st.expander(f"Months in Emergency Fund Goal"):
    months = st.number_input("Months", min_value=1, max_value=100, value=3, key=f"emergency_fund_months")
college_savings = st.number_input("Monthly College Savings", placeholder="____", key=f"savings_goal")
investment_savings = st.number_input("Monthly Investment Savings", placeholder="____", key=f"investment_savings")
retirement_savings = st.number_input("Monthly Retirement Savings", placeholder="____", key=f"retirement_savings")
other_savings = st.number_input("Monthly Other Savings", placeholder="____", key=f"other_savings")

total_savings = college_savings + investment_savings + retirement_savings + emergency_fund_savings + other_savings

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

from calculations import calc_monthly_budget

# ... all your widgets above ...

inputs = {
    "city": city,
    "housing_market": housing_market,
    "adults": adults,
    "children": children,
    "properties": property_details,
    "vehicles": vehicles,
    "vehicle_statuses": vehicle_statuses,
    "transit_cost": transit_cost,
    "lifestyle": lifestyle,
    "total_debt": stu_debt + car_debt + home_debt + credit_card_debt + other_debt,
    "total_savings": total_savings,
}

st.divider()
st.subheader("Estimated Monthly Budget")

if st.button("Calculate"):
    results = calc_monthly_budget(inputs)

    col1, col2, col3 = st.columns(3)
    col1.metric("Monthly need", f"${results['monthly_total']:,.0f}")
    col2.metric("Annual need", f"${results['annual_total']:,.0f}")
    col3.metric("Housing", f"${results['housing']:,.0f}")

    st.bar_chart({
        "Housing": results["housing"],
        "Transportation": results["transportation"],
        "Living": results["living"],
        "Debt": results["debt"],
        "Savings": results["savings"],
    })
