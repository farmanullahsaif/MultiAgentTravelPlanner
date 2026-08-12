from agents.hotel_agent import hotel_agent

result = hotel_agent(
    destination="Hunza",
    budget=80000,
    days=5,
    travel_style="Balanced"
)

print(result)
