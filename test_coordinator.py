from coordinator import coordinator


result = coordinator(
    "Hunza",
    5,
    80000,
    "Balanced"
)


print("\n")
print("=" * 70)
print("✈️ FINAL TRAVEL PLAN")
print("=" * 70)
print("\n")

print(result["summary"])

print("\n")
print("=" * 70)
print("✅ TRAVEL PLAN COMPLETE")
print("=" * 70)