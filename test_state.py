from trip_state import TripState


trip = TripState(
    destination="Hunza, Pakistan",
    days=5,
    budget=80000,
    travel_style="Balanced"
)


print("=" * 50)
print("TRIP STATE TEST")
print("=" * 50)

print("Destination:", trip.destination)
print("Days:", trip.days)
print("Budget:", trip.budget)
print("Travel Style:", trip.travel_style)

print("=" * 50)