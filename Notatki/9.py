def calculate_electricity_cost(hours_spend: float, consumption: float, price: float = 0.617):
    return hours_spend * consumption * price
