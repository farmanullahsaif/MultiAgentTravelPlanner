from dataclasses import dataclass


@dataclass
class TripState:

    # User's trip requirements
    destination: str
    days: int
    budget: int
    travel_style: str

    # Agent results
    destination_plan: str = ""
    hotel_recommendations: str = ""
    activities: str = ""
    budget_plan: str = ""