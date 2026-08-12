from llm_config import llm

# ---------------------------------------
# Load Environment Variables
# ---------------------------------------

# ---------------------------------------
# Create LLM
# ---------------------------------------



# ---------------------------------------
# Summary Agent
# ---------------------------------------

def summary_agent(
    destination,
    days,
    budget,
    travel_style,
    destination_plan,
    hotel_recommendations,
    activities,
    budget_plan
):
    """
    Create a final, organized travel plan
    from all agent recommendations.
    """

    prompt = f"""
You are the final travel planning coordinator.

Create a professional and easy-to-read final
travel plan using the information provided by
the specialized travel agents.

TRIP DETAILS
------------

Destination: {destination}
Number of Days: {days}
Available Budget: PKR {budget:,}
Travel Style: {travel_style}


DESTINATION AGENT
-----------------

{destination_plan}


HOTEL AGENT
-----------

{hotel_recommendations}


ACTIVITY AGENT
--------------

{activities}


BUDGET AGENT
------------

{budget_plan}


FINAL TRIP PLAN
---------------

Create one coherent travel plan.

Organize it using these sections:

# ✈️ {destination} Travel Plan

## 📋 Trip Overview

Include:

- Destination
- Number of days
- Travel style
- Available budget

## 🏨 Recommended Stay

Summarize the best accommodation option
from the hotel recommendations.

Explain why it is suitable.

## 🗓️ Day-by-Day Itinerary

Create a practical itinerary for each day.

For every day include:

- Morning
- Afternoon
- Evening

Avoid overcrowding the schedule.

## 🎯 Recommended Experiences

Highlight the most important activities
from the Activity Agent.

## 💰 Budget Summary

Summarize the Budget Agent's estimated costs.

Clearly show whether the trip is:

- Within budget
- Close to budget
- Over budget

## 💡 Travel Tips

Provide useful practical tips based on
the recommendations.

IMPORTANT:

- Use only information provided by the agents.
- Do not invent bookings.
- Do not claim live availability.
- Keep prices clearly labeled as estimates.
- Do not introduce attractions that were not
  mentioned by the agents.
- Keep the itinerary realistic.
- Keep the total budget consistent.
- Use clean Markdown.
- Make the final answer easy for a normal
  traveler to understand.

Return ONLY the final travel plan.
"""

    response = llm.invoke(prompt)

    return response.content