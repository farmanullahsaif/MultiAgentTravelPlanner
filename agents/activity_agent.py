from llm_config import llm


# Load environment variables



# Create LLM

    


# ---------------------------------------
# Activity Agent
# ---------------------------------------

def activity_agent(
    destination,
    days,
    budget,
    travel_style,
    destination_plan="",
    hotel_recommendations=""
):
    """
    Recommend activities and experiences
    using information from the Destination
    and Hotel Agents.
    """

    prompt = f"""
You are a professional travel activity expert.

Create activity recommendations for:

Destination: {destination}
Number of days: {days}
Total trip budget: PKR {budget:,}
Travel style: {travel_style}


---------------------------------------
DESTINATION AGENT'S ANALYSIS
---------------------------------------

Here is the analysis created by the Destination Agent:

{destination_plan}


---------------------------------------
HOTEL AGENT'S RECOMMENDATIONS
---------------------------------------

Here are the accommodations recommended by
the Hotel Agent:

{hotel_recommendations}


---------------------------------------
ACTIVITY PLANNING
---------------------------------------

Using the information above, create a practical
activity plan for the trip.

Recommend the best activities and experiences.

For each activity provide:

1. Activity name
2. Suggested day
3. Why it is worth doing
4. Approximate cost
5. Recommended duration

Consider:

- Number of available days
- Travel style
- Overall budget
- Hotel locations
- Important attractions mentioned by the Destination Agent
- Travel time between locations
- Variety of experiences
- Practical daily scheduling

Avoid scheduling too many activities in one day.

IMPORTANT:

- Do not invent exact prices.
- Clearly label costs as approximate.
- Do not claim live availability.
- Do not claim that activities are booked.
- Avoid unrealistic travel times.
- If an activity requires special permits or seasonal
  access, clearly mention that it should be verified.

Return the answer in clean Markdown format.
"""

    response = llm.invoke(prompt)

    return response.content