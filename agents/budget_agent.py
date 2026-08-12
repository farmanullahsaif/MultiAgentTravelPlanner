from llm_config import llm


# ---------------------------------------
# Load Environment Variables
# ---------------------------------------



# ---------------------------------------
# Create LLM
# ------------------------------------


# ---------------------------------------
# Budget Agent
# ---------------------------------------

def budget_agent(
    destination,
    days,
    budget,
    travel_style,
    destination_plan="",
    hotel_recommendations="",
    activities=""
):
    """
    Create a practical travel budget breakdown
    using recommendations from other agents.
    """

    prompt = f"""
You are a professional travel budget planner.

Create a realistic estimated budget for a trip with:

Destination: {destination}
Number of days: {days}
Total available budget: PKR {budget:,}
Travel style: {travel_style}


---------------------------------------
DESTINATION AGENT
---------------------------------------

Destination analysis:

{destination_plan}


---------------------------------------
HOTEL AGENT
---------------------------------------

Hotel recommendations:

{hotel_recommendations}


---------------------------------------
ACTIVITY AGENT
---------------------------------------

Activity recommendations:

{activities}


---------------------------------------
BUDGET PLANNING
---------------------------------------

Now create a realistic budget based on the
actual recommendations provided above.

Break the budget into these categories:

1. Accommodation
2. Food
3. Local transportation
4. Activities and attractions
5. Miscellaneous/emergency buffer


For each category provide:

- Estimated minimum cost
- Estimated maximum cost
- Short explanation


Then provide:

## Total Estimated Cost

Give a realistic estimated range.

## Budget Status

Clearly state whether the planned trip is:

- Within budget
- Close to budget
- Over budget


## Money-Saving Tips

Give 3-5 practical ways to reduce costs.


IMPORTANT:

- Use PKR.
- Keep the total consistent with the user's
  available budget where possible.
- Clearly label all prices as estimates.
- Do not claim exact prices unless they are known.
- Do not invent bookings or guarantees.
- Consider the number of days and travel style.
- Consider the actual hotel recommendations.
- Consider the actual activity recommendations.
- Avoid double-counting costs.
- If the recommendations appear to exceed the
  available budget, clearly explain where the
  excess comes from and suggest adjustments.

Return the answer in clean Markdown format.
"""

    # ---------------------------------------
    # Generate Response
    # ---------------------------------------

    response = llm.invoke(prompt)

    return response.content