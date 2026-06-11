# calculations.py
from data import (
    RENT_BY_CITY, DEFAULT_RENT, BASE_COST_PER_ADULT, BASE_COST_PER_CHILD,
    LIFESTYLE_MULTIPLIER, VEHICLE_COST, HOUSING_TYPE_MULTIPLIER, BEDROOM_MULTIPLIER,
)

def calc_housing(city, housing_market, properties):
  """Monthly housing cost."""
    total = 0
    for prop in properties:
        if prop["ownership"] == "Owned":
            # user-entered mortgage goes in home_debt instead
            total += prop["hoa_fee"]
        else:
            base = RENT_BY_CITY.get(city, DEFAULT_RENT)[housing_market]
            type_mult = HOUSING_TYPE_MULTIPLIER.get(prop["housing_type"], 1.0)
            bed_mult = BEDROOM_MULTIPLIER.get(prop["bedrooms"], 1.0 + 0.1 * prop["bedrooms"])
            total += base * type_mult * bed_mult + prop["hoa_fee"]
    return total

def calc_transportation(vehicles, vehicle_statuses, transit_cost):
    vehicle_total = sum(VEHICLE_COST.get(s, 400) for s in vehicle_statuses)
    return vehicle_total + transit_cost

def calc_living_expenses(adults, children, lifestyle):
    base = adults * BASE_COST_PER_ADULT + children * BASE_COST_PER_CHILD
    return base * LIFESTYLE_MULTIPLIER[lifestyle]

def calc_monthly_budget(inputs):
    """Main function — takes one dict of all inputs, returns breakdown."""
    housing = calc_housing(inputs["city"], inputs["housing_market"], inputs["properties"])
    transport = calc_transportation(
        inputs["vehicles"], inputs["vehicle_statuses"], inputs["transit_cost"]
    )
    living = calc_living_expenses(inputs["adults"], inputs["children"], inputs["lifestyle"])

    essentials = housing + transport + living
    debt = inputs["total_debt"]
    savings = inputs["total_savings"]

    monthly_need = essentials + debt + savings

    return {
        "housing": housing,
        "transportation": transport,
        "living": living,
        "debt": debt,
        "savings": savings,
        "monthly_total": monthly_need,
        "annual_total": monthly_need * 12,
    }