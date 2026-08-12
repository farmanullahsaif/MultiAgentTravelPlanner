import streamlit as st

from coordinator import coordinator


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="TravelPilot",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #6b7280;
        margin-bottom: 2rem;
    }

    .section-title {
        font-size: 1.6rem;
        font-weight: 650;
        margin-top: 1rem;
    }

    .agent-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        margin-bottom: 15px;
    }

    .footer {
        text-align: center;
        color: #777;
        padding: 30px;
        margin-top: 40px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">✈️ TravelPilot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your Multi-Agent AI Travel Planning Assistant'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align:center;">
    Plan smarter trips with specialized AI agents for
    destinations, hotels, activities and budgets.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# SIDEBAR — TRIP DETAILS
# =========================================================

with st.sidebar:

    st.header("🌍 Trip Details")

    destination = st.text_input(
        "📍 Destination",
        placeholder="e.g. Hunza, Pakistan"
    )

    days = st.number_input(
        "📅 Number of Days",
        min_value=1,
        max_value=30,
        value=5
    )

    budget = st.number_input(
        "💰 Total Budget (PKR)",
        min_value=1000,
        value=80000,
        step=5000
    )

    travel_style = st.selectbox(
        "🎒 Travel Style",
        [
            "Budget",
            "Balanced",
            "Luxury"
        ]
    )

    st.divider()

    plan_trip = st.button(
        "✈️ Plan My Trip",
        use_container_width=True
    )

    st.caption(
        "TravelPilot uses multiple specialized AI agents "
        "to build your trip plan."
    )


# =========================================================
# LANDING MESSAGE
# =========================================================

if "trip_result" not in st.session_state:

    st.session_state.trip_result = None


if not plan_trip and st.session_state.trip_result is None:

    st.info(
        "👈 Enter your trip details in the sidebar "
        "and click **Plan My Trip** to get started."
    )

    st.markdown("## 🤖 How TravelPilot Works")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("### 🌍")
        st.markdown("**Destination Agent**")
        st.caption(
            "Analyzes the destination and creates "
            "a suitable travel plan."
        )

    with col2:
        st.markdown("### 🏨")
        st.markdown("**Hotel Agent**")
        st.caption(
            "Recommends accommodations based on "
            "your budget and travel style."
        )

    with col3:
        st.markdown("### 🎯")
        st.markdown("**Activity Agent**")
        st.caption(
            "Finds activities and experiences "
            "for each day of your trip."
        )

    with col4:
        st.markdown("### 💰")
        st.markdown("**Budget Agent**")
        st.caption(
            "Creates a practical budget breakdown "
            "for your journey."
        )


# =========================================================
# GENERATE TRIP
# =========================================================

if plan_trip:

    if not destination.strip():

        st.warning(
            "⚠️ Please enter a destination first."
        )

    else:

        with st.spinner(
            "🤖 Our AI travel agents are planning your trip..."
        ):

            try:

                result = coordinator(
                    destination=destination,
                    days=days,
                    budget=budget,
                    travel_style=travel_style
                )

                st.session_state.trip_result = result

            except Exception as e:

                st.error(
                    "❌ Something went wrong while generating "
                    "your trip."
                )

                st.exception(e)


# =========================================================
# DISPLAY RESULT
# =========================================================

if st.session_state.trip_result is not None:

    result = st.session_state.trip_result

    st.success(
        "🎉 Your personalized trip plan is ready!"
    )


    # -----------------------------------------------------
    # TRIP OVERVIEW
    # -----------------------------------------------------

    st.markdown("## 🧳 Trip Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📍 Destination",
            destination
        )

    with col2:
        st.metric(
            "📅 Duration",
            f"{days} Days"
        )

    with col3:
        st.metric(
            "💰 Budget",
            f"PKR {budget:,}"
        )

    with col4:
        st.metric(
            "🎒 Style",
            travel_style
        )


    st.divider()


    # =====================================================
    # TABS
    # =====================================================

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "🌍 Destination",
            "🏨 Hotels",
            "🎯 Activities",
            "💰 Budget"
        ]
    )


    # =====================================================
    # DESTINATION TAB
    # =====================================================

    with tab1:

        st.markdown(
            "## 🌍 Destination Recommendations"
        )

        st.markdown(
            '<div class="agent-card">',
            unsafe_allow_html=True
        )

        st.markdown(
            result.get(
                "destination",
                "No destination information available."
            )
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    # =====================================================
    # HOTEL TAB
    # =====================================================

    with tab2:

        st.markdown(
            "## 🏨 Hotel Recommendations"
        )

        st.caption(
            "Accommodation suggestions generated "
            "by the Hotel Agent."
        )

        st.markdown(
            '<div class="agent-card">',
            unsafe_allow_html=True
        )

        st.markdown(
            result.get(
                "hotels",
                "No hotel recommendations available."
            )
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    # =====================================================
    # ACTIVITY TAB
    # =====================================================

    with tab3:

        st.markdown(
            "## 🎯 Activities & Experiences"
        )

        st.caption(
            "Personalized experiences generated "
            "by the Activity Agent."
        )

        st.markdown(
            '<div class="agent-card">',
            unsafe_allow_html=True
        )

        st.markdown(
            result.get(
                "activities",
                "No activity recommendations available."
            )
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    # =====================================================
    # BUDGET TAB
    # =====================================================

    with tab4:

        st.markdown(
            "## 💰 Budget Summary"
        )

        st.caption(
            "Estimated costs generated by the Budget Agent."
        )

        st.markdown(
            '<div class="agent-card">',
            unsafe_allow_html=True
        )

        st.markdown(
            result.get(
                "budget",
                "No budget information available."
            )
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    # =====================================================
    # FOOTER
    # =====================================================

    st.divider()

    st.markdown(
        """
        <div class="footer">
        ✈️ <b>TravelPilot</b><br>
        Multi-Agent AI Travel Planner<br>
        <small>
        Destination • Hotels • Activities • Budget
        </small>
        </div>
        """,
        unsafe_allow_html=True
    )