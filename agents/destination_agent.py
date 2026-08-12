from llm_config import llm


def destination_agent(
    destination,
    days,
    budget,
    travel_style
):
    """
    Generate destination recommendations.
    """

    prompt = f"""
You are a professional travel destination expert.

Plan the destination part of a trip.

Destination: {destination}
Number of days: {days}
Budget: PKR {budget:,}
Travel style: {travel_style}

Recommend the best places and activities for this trip.

For each recommendation provide:

1. Place/activity name
2. Why it is worth visiting
3. Suggested day
4. Estimated cost if relevant

Important:

- Keep recommendations realistic.
- Consider the number of days.
- Consider the user's budget.
- Do not invent exact hotel or flight prices.
- Clearly state when costs are approximate.

Return the answer in a clean, organized format.
"""

    response = llm.invoke(prompt)

    return response.content