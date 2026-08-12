from agents.destination_agent import destination_agent


result = destination_agent(
    destination="Hunza, Pakistan",
    days=5,
    budget=80000,
    travel_style="Balanced"
)


print("\n")
print("=" * 60)
print("DESTINATION AGENT RESULT")
print("=" * 60)
print(result)