from agents.budget_agent import budget_agent


result = budget_agent(
    destination="Hunza, Pakistan",
    days=5,
    budget=80000,
    travel_style="Balanced"
)


print("\n")
print("=" * 60)
print("💰 BUDGET AGENT RESULT")
print("=" * 60)

print(result)