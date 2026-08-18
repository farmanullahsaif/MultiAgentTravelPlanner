import base64
import os
from datetime import datetime

import streamlit as st

from coordinator import coordinator


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="TravelPilot",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# HERO BACKGROUND HELPER
# ---------------------------------------------------------
# Drop a real destination photo at assets/hero.jpg and this
# will use it automatically. Until then, it falls back to a
# CSS gradient + mountain silhouette so the hero never breaks.
# =========================================================

def get_hero_background_css():
    hero_path = os.path.join(os.path.dirname(__file__), "assets", "hero.jpg")

    if os.path.exists(hero_path):
        with open(hero_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        return f"linear-gradient(180deg, rgba(30,26,18,0.35), rgba(30,26,18,0.75)), url(data:image/jpg;base64,{encoded})"

    mountain_svg = (
        "data:image/svg+xml;utf8,"
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1600 500' preserveAspectRatio='none'>"
        "<polygon points='0,500 0,320 220,140 420,320 560,180 780,320 950,120 1150,320 1300,220 1600,340 1600,500' fill='%233d3222'/>"
        "<polygon points='0,500 0,380 300,260 520,380 700,240 900,380 1100,260 1350,380 1600,300 1600,500' fill='%232b2419' opacity='0.85'/>"
        "</svg>"
    )
    return (
        f"linear-gradient(180deg, #e8b975 0%, #d99a63 35%, #c17f52 60%, #3d3222 100%), "
        f"url(\"{mountain_svg}\")"
    )


HERO_BG = get_hero_background_css()


# =========================================================
# CUSTOM CSS — warm / editorial travel-brand theme + motion
# =========================================================

st.markdown(
    f"""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800;900&family=Inter:wght@400;500;600;700&display=swap');

    :root {{
        --tp-cream: #faf3e6;
        --tp-cream-2: #f3e9d8;
        --tp-olive: #3d3222;
        --tp-olive-2: #2b2419;
        --tp-green: #2f8f5b;
        --tp-green-dark: #23703f;
        --tp-terracotta: #c17f52;
        --tp-text-muted: #7a6f5c;
    }}

    html {{ scroll-behavior: smooth; }}

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}

    h1, h2, h3, .tp-hero-title, .section-title {{
        font-family: 'Poppins', sans-serif;
    }}

    /* Hide Streamlit dev toolbar for a finished, deployed look */
    #MainMenu, header[data-testid="stHeader"], .stDeployButton,
    [data-testid="stToolbar"], [data-testid="stStatusWidget"] {{
        visibility: hidden;
        height: 0;
    }}

    .stApp {{
        background: var(--tp-cream);
        color: #2b2419 !important;
    }}

    /* Nuclear override: force ALL text in the main content area to dark */
    .stApp .stMainBlockContainer,
    .stApp .stMainBlockContainer *,
    .stApp .block-container,
    .stApp .block-container *,
    .stApp [data-testid="stAppViewContainer"],
    .stApp [data-testid="stAppViewContainer"] * {{
        color: #2b2419 !important;
    }}

    /* Re-allow white text in sidebar */
    section[data-testid="stSidebar"],
    section[data-testid="stSidebar"] * {{
        color: var(--tp-cream) !important;
    }}

    /* Re-allow light text in hero and footer (dark backgrounds) */
    .tp-hero, .tp-hero * {{
        color: #fffaf2 !important;
    }}
    .tp-hero .tp-hero-title span {{
        color: #a9e6c2 !important;
    }}
    .tp-footer, .tp-footer * {{
        color: var(--tp-cream-2) !important;
    }}
    .tp-footer small, .tp-footer small * {{
        color: var(--tp-text-muted) !important;
    }}

    .block-container {{
        padding-top: 0 !important;
        max-width: 1200px;
    }}

    /* -------------------- MOTION SYSTEM -------------------- */

    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(22px); }}
        to   {{ opacity: 1; transform: translateY(0); }}
    }}

    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to   {{ opacity: 1; }}
    }}

    @keyframes popIn {{
        0%   {{ opacity: 0; transform: scale(0.92) translateY(8px); }}
        70%  {{ opacity: 1; transform: scale(1.02) translateY(0); }}
        100% {{ transform: scale(1) translateY(0); }}
    }}

    @keyframes floatPlane {{
        0%, 100% {{ transform: translate(0,0) rotate(-8deg); }}
        50%      {{ transform: translate(12px,-14px) rotate(-3deg); }}
    }}

    @keyframes heroGlow {{
        0%, 100% {{ opacity: 0.5; transform: scale(1) translate(0,0); }}
        50%      {{ opacity: 0.8; transform: scale(1.1) translate(-12px,10px); }}
    }}

    @keyframes shine {{
        from {{ transform: translateX(-140%) skewX(-20deg); }}
        to   {{ transform: translateX(240%) skewX(-20deg); }}
    }}

    @keyframes bounceChevron {{
        0%, 100% {{ transform: translateY(0); opacity: 0.55; }}
        50%      {{ transform: translateY(8px); opacity: 1; }}
    }}

    @keyframes pulseRing {{
        0%   {{ box-shadow: 0 0 0 0 rgba(47,143,91,0.45); }}
        70%  {{ box-shadow: 0 0 0 16px rgba(47,143,91,0); }}
        100% {{ box-shadow: 0 0 0 0 rgba(47,143,91,0); }}
    }}

    @media (prefers-reduced-motion: reduce) {{
        *, *::before, *::after {{
            animation: none !important;
            transition: none !important;
        }}
    }}

    /* -------------------- FULL-BLEED HELPER -------------------- */

    .tp-bleed {{
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
    }}

    /* -------------------- HERO -------------------- */

    .tp-hero {{
        position: relative;
        overflow: hidden;
        background: {HERO_BG};
        background-size: cover;
        background-position: center;
        min-height: 460px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 3rem 1.5rem;
        margin-bottom: 2.5rem;
    }}

    .tp-hero::before {{
        content: "";
        position: absolute;
        top: -10%;
        left: 60%;
        width: 420px;
        height: 420px;
        background: radial-gradient(circle, rgba(169,230,194,0.55), transparent 70%);
        animation: heroGlow 7s ease-in-out infinite;
        pointer-events: none;
        z-index: 1;
    }}

    .tp-hero-plane {{
        position: absolute;
        top: 18%;
        right: 14%;
        font-size: 2.1rem;
        opacity: 0.9;
        animation: floatPlane 5s ease-in-out infinite;
        filter: drop-shadow(0 4px 10px rgba(0,0,0,0.25));
        z-index: 2;
    }}

    .tp-hero-badge, .tp-hero-title, .tp-hero-desc, .tp-hero-cta {{
        position: relative;
        z-index: 2;
        animation: fadeInUp 0.8s ease both;
    }}

    .tp-hero-badge {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255,255,255,0.15);
        border: 1px solid rgba(255,255,255,0.4);
        color: #fff;
        padding: 6px 16px;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 1.2rem;
        backdrop-filter: blur(4px);
        animation-delay: 0s;
    }}

    .tp-hero-title {{
        font-size: 3.2rem;
        font-weight: 800;
        color: #fffaf2;
        line-height: 1.15;
        max-width: 780px;
        text-shadow: 0 2px 18px rgba(0,0,0,0.35);
        margin-bottom: 0.6rem;
        animation-delay: 0.15s;
    }}

    .tp-hero-title span {{
        color: #a9e6c2;
    }}

    .tp-hero-desc {{
        font-size: 1.1rem;
        font-weight: 500;
        color: #f3ead9;
        max-width: 560px;
        margin-bottom: 1.6rem;
        text-shadow: 0 1px 10px rgba(0,0,0,0.3);
        animation-delay: 0.3s;
    }}

    .tp-hero-cta {{
        display: inline-block;
        position: relative;
        overflow: hidden;
        background: var(--tp-green);
        color: white !important;
        font-weight: 700;
        padding: 0.85rem 2.2rem;
        border-radius: 999px;
        text-decoration: none;
        font-size: 0.95rem;
        letter-spacing: 0.02em;
        box-shadow: 0 8px 24px rgba(47,143,91,0.4);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
        animation: fadeInUp 0.8s ease both, pulseRing 2.6s ease-in-out infinite 1s;
    }}

    .tp-hero-cta::before {{
        content: "";
        position: absolute;
        top: 0; left: -140%;
        width: 60%; height: 100%;
        background: linear-gradient(120deg, transparent, rgba(255,255,255,0.55), transparent);
    }}

    .tp-hero-cta:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 28px rgba(47,143,91,0.5);
    }}

    .tp-hero-cta:hover::before {{
        animation: shine 0.9s ease forwards;
    }}

    .tp-scroll-cue {{
        position: absolute;
        bottom: 18px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 2;
        color: #fff;
        font-size: 1.6rem;
        text-decoration: none;
        animation: bounceChevron 1.8s ease-in-out infinite;
    }}

    /* -------------------- SECTION TITLES -------------------- */

    .section-title {{
        font-size: 1.6rem;
        font-weight: 700;
        margin-top: 0.5rem;
        margin-bottom: 1rem;
        color: var(--tp-olive);
    }}

    .section-subtitle {{
        color: var(--tp-text-muted);
        font-size: 0.95rem;
        margin-top: -0.6rem;
        margin-bottom: 1.2rem;
    }}

    /* -------------------- HOW IT WORKS CARDS -------------------- */

    .tp-how-card {{
        background: white;
        border-radius: 16px;
        padding: 24px 20px;
        text-align: center;
        border: 1px solid rgba(61,50,34,0.08);
        box-shadow: 0 6px 20px rgba(61,50,34,0.06);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        min-height: 180px;
        animation: fadeInUp 0.6s ease both;
    }}

    .tp-how-card:hover {{
        transform: translateY(-6px);
        box-shadow: 0 14px 30px rgba(61,50,34,0.14);
    }}

    .tp-how-icon {{
        width: 52px;
        height: 52px;
        border-radius: 50%;
        background: linear-gradient(135deg, var(--tp-green), var(--tp-terracotta));
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        margin: 0 auto 12px auto;
        transition: transform 0.2s ease;
    }}

    .tp-how-card:hover .tp-how-icon {{
        transform: scale(1.1) rotate(-4deg);
    }}

    .tp-how-title {{
        font-weight: 700;
        color: var(--tp-olive);
        margin-bottom: 6px;
        font-family: 'Poppins', sans-serif;
    }}

    .tp-how-desc {{
        color: var(--tp-text-muted);
        font-size: 0.85rem;
        line-height: 1.4;
    }}

    /* -------------------- METRIC / OVERVIEW CARDS -------------------- */

    .tp-metric-row {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        margin-bottom: 1rem;
    }}

    .tp-metric-card {{
        background: white;
        border: 1px solid rgba(61,50,34,0.08);
        border-left: 4px solid var(--tp-green);
        border-radius: 12px;
        padding: 16px 20px;
        box-shadow: 0 4px 14px rgba(61,50,34,0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        animation: fadeInUp 0.55s ease both;
    }}

    .tp-metric-card:hover {{
        transform: translateY(-3px);
        box-shadow: 0 10px 22px rgba(61,50,34,0.1);
    }}

    .tp-metric-label {{
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: var(--tp-text-muted);
        font-weight: 700;
        margin-bottom: 6px;
    }}

    .tp-metric-value {{
        font-size: 1.4rem;
        font-weight: 800;
        color: var(--tp-olive);
        font-family: 'Poppins', sans-serif;
    }}

    /* -------------------- SUCCESS BANNER -------------------- */

    .tp-success-banner {{
        background: linear-gradient(90deg, rgba(47,143,91,0.16), rgba(47,143,91,0.04));
        border: 1px solid rgba(47,143,91,0.35);
        color: var(--tp-green-dark);
        padding: 16px 22px;
        border-radius: 12px;
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        animation: popIn 0.6s cubic-bezier(.34,1.56,.64,1) both;
    }}

    /* -------------------- AGENT / RESULT CARDS -------------------- */

    .agent-card {{
        background: white;
        padding: 24px 26px;
        border-radius: 16px;
        border: 1px solid rgba(61,50,34,0.08);
        margin-bottom: 15px;
        box-shadow: 0 6px 20px rgba(61,50,34,0.06);
        color: #2b2419 !important;
        animation: fadeInUp 0.5s ease both;
    }}

    /* Keep all AI-generated Markdown readable inside result cards */
    .agent-card *,
    .agent-card p,
    .agent-card li,
    .agent-card h1,
    .agent-card h2,
    .agent-card h3,
    .agent-card h4,
    .agent-card strong,
    .agent-card em,
    .agent-card td,
    .agent-card th {{
        color: #2b2419 !important;
    }}

    .agent-card table {{
        width: 100%;
        color: #2b2419 !important;
        background: white !important;
    }}

    .agent-card th {{
        background: #f3e9d8 !important;
        color: #2b2419 !important;
    }}

    .agent-card td {{
        background: white !important;
        color: #2b2419 !important;
    }}

    /* IMPORTANT: Streamlit renders each st.markdown() call in a
       separate container, so the .agent-card wrapper cannot reliably
       style the following AI Markdown. Scope readable text to the tab
       panels where the generated results actually appear. */
    .stTabs [data-baseweb="tab-panel"] {{
        color: #2b2419 !important;
    }}

    .stTabs [data-baseweb="tab-panel"] div[data-testid="stMarkdownContainer"] p,
    .stTabs [data-baseweb="tab-panel"] div[data-testid="stMarkdownContainer"] li,
    .stTabs [data-baseweb="tab-panel"] div[data-testid="stMarkdownContainer"] h1,
    .stTabs [data-baseweb="tab-panel"] div[data-testid="stMarkdownContainer"] h2,
    .stTabs [data-baseweb="tab-panel"] div[data-testid="stMarkdownContainer"] h3,
    .stTabs [data-baseweb="tab-panel"] div[data-testid="stMarkdownContainer"] h4,
    .stTabs [data-baseweb="tab-panel"] div[data-testid="stMarkdownContainer"] strong,
    .stTabs [data-baseweb="tab-panel"] div[data-testid="stMarkdownContainer"] em,
    .stTabs [data-baseweb="tab-panel"] div[data-testid="stMarkdownContainer"] td,
    .stTabs [data-baseweb="tab-panel"] div[data-testid="stMarkdownContainer"] th,
    .stTabs [data-baseweb="tab-panel"] div[data-testid="stMarkdownContainer"] span,
    .stTabs [data-baseweb="tab-panel"] div[data-testid="stMarkdownContainer"] a {{
        color: #2b2419 !important;
    }}

    .stTabs [data-baseweb="tab-panel"] div[data-testid="stCaptionContainer"] {{
        color: #7a6f5c !important;
    }}

    .stTabs [data-baseweb="tab-panel"] div[data-testid="stCaptionContainer"] * {{
        color: #7a6f5c !important;
    }}

    .stTabs [data-baseweb="tab-panel"] table {{
        background: white !important;
        color: #2b2419 !important;
        width: 100%;
        border-collapse: collapse;
    }}

    .stTabs [data-baseweb="tab-panel"] th {{
        background: #f3e9d8 !important;
        color: #2b2419 !important;
        font-weight: 700 !important;
    }}

    .stTabs [data-baseweb="tab-panel"] td {{
        background: white !important;
        color: #2b2419 !important;
    }}

    /* -------------------- WORKFLOW CARDS -------------------- */

    .tp-workflow-card {{
        background: white;
        border: 1px solid rgba(61,50,34,0.08);
        border-radius: 12px;
        text-align: center;
        padding: 12px 8px;
        color: var(--tp-olive);
        box-shadow: 0 4px 14px rgba(61,50,34,0.05);
        font-size: 0.85rem;
    }}

    .tp-workflow-card span {{
        color: var(--tp-green-dark);
        font-size: 0.78rem;
    }}

    /* -------------------- TABS -------------------- */

    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
        border-bottom: 2px solid rgba(61,50,34,0.08);
    }}

    .stTabs [data-baseweb="tab"] {{
        height: 44px;
        border-radius: 999px 999px 0 0;
        padding: 0 20px;
        font-weight: 700;
        color: var(--tp-text-muted);
        transition: color 0.15s ease, background 0.15s ease;
    }}

    .stTabs [aria-selected="true"] {{
        color: white !important;
        background: var(--tp-green);
        border-radius: 999px 999px 0 0;
    }}

    .stTabs [data-baseweb="tab-panel"] {{
        animation: fadeIn 0.4s ease both;
    }}

    /* -------------------- SIDEBAR -------------------- */

    section[data-testid="stSidebar"] {{
        background: var(--tp-olive);
    }}

    section[data-testid="stSidebar"] * {{
        color: var(--tp-cream) !important;
    }}

    section[data-testid="stSidebar"] input,
    section[data-testid="stSidebar"] select,
    section[data-testid="stSidebar"] textarea {{
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        border-radius: 8px !important;
        transition: border-color 0.15s ease, background 0.15s ease;
    }}

    section[data-testid="stSidebar"] input:focus,
    section[data-testid="stSidebar"] select:focus {{
        border-color: var(--tp-green) !important;
        background: rgba(47,143,91,0.12) !important;
    }}

    /* -------------------- BUTTONS -------------------- */

    .stButton > button {{
        background: var(--tp-green);
        color: white !important;
        font-weight: 700;
        border: none;
        border-radius: 999px;
        padding: 0.7rem 1.2rem;
        transition: background 0.15s ease, transform 0.15s ease, box-shadow 0.15s ease;
    }}

    .stButton > button:hover {{
        background: var(--tp-green-dark);
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(47,143,91,0.35);
    }}

    .stButton > button:active {{
        transform: translateY(0);
    }}

    /* -------------------- ALERTS (info / warning / error) -------------------- */

    [data-testid="stAlert"] {{
        animation: fadeInUp 0.5s ease both;
        border-radius: 12px !important;
    }}

    /* -------------------- SPINNER -------------------- */

    [data-testid="stSpinner"] div {{
        border-top-color: var(--tp-green) !important;
    }}

    /* -------------------- MAIN AI RESULT TEXT -------------------- */

    /* Force Streamlit markdown inside the main page to use dark text.
       This is intentionally scoped to the main content so the dark sidebar
       and hero text keep their original colors. */
    section.main div[data-testid="stMarkdownContainer"],
    section.main div[data-testid="stMarkdownContainer"] p,
    section.main div[data-testid="stMarkdownContainer"] li,
    section.main div[data-testid="stMarkdownContainer"] h1,
    section.main div[data-testid="stMarkdownContainer"] h2,
    section.main div[data-testid="stMarkdownContainer"] h3,
    section.main div[data-testid="stMarkdownContainer"] h4,
    section.main div[data-testid="stMarkdownContainer"] h5,
    section.main div[data-testid="stMarkdownContainer"] strong,
    section.main div[data-testid="stMarkdownContainer"] em,
    section.main div[data-testid="stMarkdownContainer"] span,
    section.main div[data-testid="stMarkdownContainer"] td,
    section.main div[data-testid="stMarkdownContainer"] th,
    section.main div[data-testid="stMarkdownContainer"] a {{
        color: #2b2419 !important;
    }}

    /* Keep captions readable but slightly muted. */
    section.main div[data-testid="stCaptionContainer"],
    section.main div[data-testid="stCaptionContainer"] * {{
        color: #7a6f5c !important;
    }}

    /* -------------------- FOOTER -------------------- */

    .tp-footer {{
        background: var(--tp-olive);
        color: var(--tp-cream-2);
        text-align: center;
        padding: 40px 20px;
        margin-top: 50px;
        font-size: 0.9rem;
        animation: fadeIn 0.8s ease both;
    }}

    .tp-footer b {{
        font-family: 'Poppins', sans-serif;
        font-size: 1.1rem;
    }}

    .tp-footer small {{
        color: var(--tp-text-muted);
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HERO
# =========================================================

st.markdown(
    """
    <div class="tp-hero tp-bleed">
        <div class="tp-hero-plane">✈️</div>
        <div class="tp-hero-badge">🌿 AI-Powered Trip Planning</div>
        <div class="tp-hero-title">Time for your next <span>sustainable</span> adventure</div>
        <div class="tp-hero-desc">
            TravelPilot's AI agents plan your destination, hotels, activities
            and budget — so you can just start packing.
        </div>
        <a href="#trip-details" class="tp-hero-cta">👈 Start Planning</a>
        <a href="#trip-details" class="tp-scroll-cue">⌄</a>
    </div>
    """,
    unsafe_allow_html=True
)


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

    st.markdown('<div class="section-title" id="trip-details">🤖 How TravelPilot Works</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Five specialized agents work together to build your itinerary.</div>', unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    how_it_works = [
        ("🌍", "Destination Agent", "Analyzes the destination and creates a suitable travel plan."),
        ("🏨", "Hotel Agent", "Recommends accommodations based on your budget and travel style."),
        ("🎯", "Activity Agent", "Finds activities and experiences for each day of your trip."),
        ("💰", "Budget Agent", "Creates a practical budget breakdown for your journey."),
        ("📋", "Summary Agent", "Combines all agent outputs into one final trip plan."),
    ]

    for i, (col, (icon, title, desc)) in enumerate(zip([col1, col2, col3, col4, col5], how_it_works)):
        with col:
            st.markdown(
                f"""
                <div class="tp-how-card" style="animation-delay:{i * 0.12}s;">
                    <div class="tp-how-icon">{icon}</div>
                    <div class="tp-how-title">{title}</div>
                    <div class="tp-how-desc">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("👈 Enter your trip details in the sidebar and click **Plan My Trip** to get started.")


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
                st.session_state.trip_generated_at = datetime.now().strftime("%d %b %Y, %I:%M %p")

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

    st.markdown(
        '<div class="tp-success-banner">🎉 Your personalized trip plan is ready!</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # TRIP OVERVIEW (custom cards instead of st.metric)
    # -----------------------------------------------------

    st.markdown('<div class="section-title">🧳 Trip Overview</div>', unsafe_allow_html=True)

    overview_items = [
        ("📍 Destination", destination),
        ("📅 Duration", f"{days} Days"),
        ("💰 Budget", f"PKR {budget:,}"),
        ("🎒 Style", travel_style),
    ]

    cards_html = '<div class="tp-metric-row">'

    for i, (label, value) in enumerate(overview_items):
        cards_html += (
            f'<div class="tp-metric-card" '
            f'style="animation-delay:{i * 0.1}s;">'
            f'<div class="tp-metric-label">{label}</div>'
            f'<div class="tp-metric-value">{value}</div>'
            f'</div>'
        )

    cards_html += '</div>'

    st.markdown(
        cards_html,
        unsafe_allow_html=True
    )

    st.divider()


    # =====================================================
    # TABS
    # =====================================================

    tab0, tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📋 Final Plan",
            "🌍 Destination",
            "🏨 Hotels",
            "🎯 Activities",
            "💰 Budget"
        ]
    )


    # =====================================================
    # FINAL PLAN TAB
    # =====================================================

    with tab0:

        st.markdown(
            '<div class="section-title">📋 Your Final Travel Plan</div>',
            unsafe_allow_html=True
        )
        st.caption(
            f"Generated by the Summary Agent • {st.session_state.get('trip_generated_at', 'Just now')}"
        )

        summary = result.get(
            "summary",
            "No final summary is available yet."
        )

        st.markdown(
            '<div class="agent-card">',
            unsafe_allow_html=True
        )
        st.markdown(summary)
        st.markdown('</div>', unsafe_allow_html=True)

        combined_plan = f"""# TravelPilot — {destination}\n\n## Trip Overview\n- Destination: {destination}\n- Duration: {days} days\n- Budget: PKR {budget:,}\n- Travel Style: {travel_style}\n\n## Final Travel Plan\n{summary}\n\n## Destination Recommendations\n{result.get('destination', '')}\n\n## Hotel Recommendations\n{result.get('hotels', '')}\n\n## Activities & Experiences\n{result.get('activities', '')}\n\n## Budget Summary\n{result.get('budget', '')}\n"""

        st.download_button(
            label="⬇️ Download Complete Trip Plan",
            data=combined_plan,
            file_name=f"TravelPilot_{destination.replace(' ', '_')}.md",
            mime="text/markdown",
            use_container_width=True
        )

        # Quick workflow health check — no extra AI calls
        st.markdown('<div class="section-title">🤖 Agent Workflow</div>', unsafe_allow_html=True)
        status_cols = st.columns(5)
        workflow = [
            ("🌍", "Destination", bool(result.get("destination"))),
            ("🏨", "Hotels", bool(result.get("hotels"))),
            ("🎯", "Activities", bool(result.get("activities"))),
            ("💰", "Budget", bool(result.get("budget"))),
            ("📋", "Summary", bool(result.get("summary"))),
        ]
        for col, (icon, label, ok) in zip(status_cols, workflow):
            with col:
                st.markdown(
                    f'<div class="tp-workflow-card">{icon}<br><b>{label}</b><br><span>{"✅ Ready" if ok else "⚠️ Missing"}</span></div>',
                    unsafe_allow_html=True
                )


    # =====================================================
    # DESTINATION TAB
    # =====================================================

    with tab1:

        st.markdown('<div class="section-title">🌍 Destination Recommendations</div>', unsafe_allow_html=True)
        st.caption("Destination insights generated by the Destination Agent.")

        st.markdown('<div class="agent-card">', unsafe_allow_html=True)
        st.markdown(result.get("destination", "No destination information available."))
        st.markdown("</div>", unsafe_allow_html=True)


    # =====================================================
    # HOTEL TAB
    # =====================================================

    with tab2:

        st.markdown('<div class="section-title">🏨 Hotel Recommendations</div>', unsafe_allow_html=True)
        st.caption("Accommodation suggestions generated by the Hotel Agent.")

        st.markdown('<div class="agent-card">', unsafe_allow_html=True)
        st.markdown(result.get("hotels", "No hotel recommendations available."))
        st.markdown("</div>", unsafe_allow_html=True)


    # =====================================================
    # ACTIVITY TAB
    # =====================================================

    with tab3:

        st.markdown('<div class="section-title">🎯 Activities & Experiences</div>', unsafe_allow_html=True)
        st.caption("Personalized experiences generated by the Activity Agent.")

        st.markdown('<div class="agent-card">', unsafe_allow_html=True)
        st.markdown(result.get("activities", "No activity recommendations available."))
        st.markdown("</div>", unsafe_allow_html=True)


    # =====================================================
    # BUDGET TAB
    # =====================================================

    with tab4:

        st.markdown('<div class="section-title">💰 Budget Summary</div>', unsafe_allow_html=True)
        st.caption("Estimated costs generated by the Budget Agent.")

        st.markdown('<div class="agent-card">', unsafe_allow_html=True)
        st.markdown(result.get("budget", "No budget information available."))
        st.markdown("</div>", unsafe_allow_html=True)


    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown(
        """
        <div class="tp-footer tp-bleed">
        🌿 <b>TravelPilot</b><br>
        Multi-Agent AI Travel Planner<br>
        <small>Destination • Hotels • Activities • Budget</small>
        </div>
        """,
        unsafe_allow_html=True
    )