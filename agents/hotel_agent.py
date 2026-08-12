from llm_config import llm


# ---------------------------------------
# Load Environment Variables
# ---------------------------------------



# ---------------------------------------
# Create LLM
# ---------------------------------------




# ---------------------------------------
# Hotel Agent
# ---------------------------------------

def hotel_agent(
    destination,
    budget,
    days,
    travel_style,
    destination_plan=""
):

    prompt = f"""
You are a professional hotel recommendation expert.

The user is planning a trip with the following requirements:

Destination: {destination}
Budget: PKR {budget:,}
Number of Days: {days}
Travel Style: {travel_style}


---------------------------------------
DESTINATION AGENT'S ANALYSIS
---------------------------------------

The Destination Agent has already analyzed the destination.

Use this information to make better hotel recommendations:

{destination_plan}


---------------------------------------
HOTEL RECOMMENDATIONS
---------------------------------------

Suggest 3 suitable accommodations.

For each accommodation provide:

1. Name
2. Approximate nightly price
3. Estimated total cost for the trip
4. Important features
5. Location
6. Why it fits the travel style

Consider:

- The user's total budget
- Number of days
- Travel style
- Important areas and attractions mentioned
  by the Destination Agent
- Convenience and accessibility
- Value for money

Keep recommendations realistic.

IMPORTANT:
- Prices must be clearly labeled as approximate.
- Do not claim live availability.
- Do not invent confirmed bookings.
- Do not assume the user has already booked anything.

Return the answer in clean Markdown format.
"""


    # ---------------------------------------
    # Generate Response
    # ---------------------------------------

    response = llm.invoke(prompt)

    return response.content