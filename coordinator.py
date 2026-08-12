from agents.destination_agent import destination_agent
from agents.hotel_agent import hotel_agent
from agents.activity_agent import activity_agent
from agents.budget_agent import budget_agent
from agents.summary_agent import summary_agent
from trip_state import TripState


def coordinator(
    destination,
    days,
    budget,
    travel_style
):
    """
    Coordinate all travel agents using shared TripState.
    """

    # ---------------------------------------
    # Create shared trip state
    # ---------------------------------------

    state = TripState(
        destination=destination,
        days=days,
        budget=budget,
        travel_style=travel_style
    )

    # ---------------------------------------
    # 1. Destination Agent
    # ---------------------------------------

    state.destination_plan = destination_agent(
        destination=state.destination,
        days=state.days,
        budget=state.budget,
        travel_style=state.travel_style
    )

    # ---------------------------------------
    # 2. Hotel Agent
    # ---------------------------------------

    state.hotel_recommendations = hotel_agent(
        destination=state.destination,
        budget=state.budget,
        days=state.days,
        travel_style=state.travel_style,
        destination_plan=state.destination_plan
    )

    # ---------------------------------------
    # 3. Activity Agent
    # ---------------------------------------

    state.activities = activity_agent(
        destination=state.destination,
        days=state.days,
        budget=state.budget,
        travel_style=state.travel_style,
        destination_plan=state.destination_plan,
        hotel_recommendations=state.hotel_recommendations
    )

    # ---------------------------------------
    # 4. Budget Agent
    # ---------------------------------------

    state.budget_plan = budget_agent(
        destination=state.destination,
        days=state.days,
        budget=state.budget,
        travel_style=state.travel_style,
        destination_plan=state.destination_plan,
        hotel_recommendations=state.hotel_recommendations,
        activities=state.activities
    )

    # ---------------------------------------
    # 5. Summary Agent
    # ---------------------------------------

    final_summary = summary_agent(
        destination=state.destination,
        days=state.days,
        budget=state.budget,
        travel_style=state.travel_style,
        destination_plan=state.destination_plan,
        hotel_recommendations=state.hotel_recommendations,
        activities=state.activities,
        budget_plan=state.budget_plan
    )

    # ---------------------------------------
    # Return Results
    # ---------------------------------------

    return {
        "destination": state.destination_plan,
        "hotels": state.hotel_recommendations,
        "activities": state.activities,
        "budget": state.budget_plan,
        "summary": final_summary
    }