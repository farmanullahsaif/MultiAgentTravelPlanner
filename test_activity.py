from agents.activity_agent import activity_agent


result = activity_agent(
    destination="Hunza, Pakistan",
    days=5,
    budget=80000,
    travel_style="Balanced"
)


print("\n")
print("=" * 60)
print("🎯 ACTIVITY AGENT RESULT")
print("=" * 60)

print(result)