# data.py

# Monthly rent estimate by city + housing market level (1-bed apartment baseline)
RENT_BY_CITY = {
    "San Francisco": {"Basic": 2200, "Average": 3200, "Premium": 4500},
    "Oakland":       {"Basic": 1600, "Average": 2400, "Premium": 3200},
    "San Jose":      {"Basic": 1800, "Average": 2600, "Premium": 3500},
    # add more cities or use a default
}

DEFAULT_RENT = {"Basic": 1500, "Average": 2200, "Premium": 3000}

# Per-person monthly costs (food, utilities share, etc.)
BASE_COST_PER_ADULT = 800
BASE_COST_PER_CHILD = 400

# Lifestyle multipliers on discretionary spending
LIFESTYLE_MULTIPLIER = {
    "Stable": 1.0,
    "Moderate": 1.3,
    "Luxury": 1.7,
}

# Vehicle monthly cost by ownership type (insurance, gas, maintenance)
VEHICLE_COST = {
    "Owned": 400,
    "Leased": 550,
    "Rented": 600,
}

HOUSING_TYPE_MULTIPLIER = {
    "Apartment": 1.0,
    "Condo": 1.1,
    "Townhome": 1.2,
    "Single-Family Home": 1.4,
}

BEDROOM_MULTIPLIER = {0: 0.8, 1: 1.0, 2: 1.2, 3: 1.4}  # per bedroom above 1