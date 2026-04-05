import streamlit as st

st.set_page_config(page_title="Medical App Predictor", layout="wide")

# -------------------------------
# Custom CSS Styling
# -------------------------------
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: #e2e8f0;
}

/* Title */
.main-title {
    font-size: 42px;
    font-weight: bold;
    color: #38bdf8;
}

/* Subtitle */
.sub-text {
    font-size: 18px;
    color: #cbd5f5;
}

/* Cards */
.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.6);
    margin-bottom: 20px;
    border: 1px solid #334155;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

/* Hover Effect */
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 8px 25px rgba(56,189,248,0.3);
}

/* Highlight Box */
.highlight {
    background: linear-gradient(90deg, #0369a1, #0ea5e9);
    padding: 15px;
    border-radius: 10px;
    font-weight: bold;
    color: white;
}

/* Section Headers */
h2, h3, h4 {
    color: #7dd3fc;
}

/* Divider */
hr {
    border: 1px solid #334155;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* Sidebar Background */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #0f172a);
    border-right: 1px solid #1e293b;
}

/* Sidebar Title */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #38bdf8;
}

/* Sidebar Text */
section[data-testid="stSidebar"] {
    color: #e2e8f0;
}

/* Slider Labels */
section[data-testid="stSidebar"] label {
    color: #cbd5f5 !important;
    font-weight: 500;
}

/* Slider */
section[data-testid="stSidebar"] .stSlider > div {
    color: #38bdf8;
}

/* Buttons (if any) */
section[data-testid="stSidebar"] button {
    background-color: #1e293b;
    color: #e2e8f0;
    border-radius: 8px;
    border: 1px solid #334155;
}

/* Button Hover */
section[data-testid="stSidebar"] button:hover {
    background-color: #0ea5e9;
    color: white;
}

/* Divider */
section[data-testid="stSidebar"] hr {
    border: 1px solid #334155;
}

/* Sidebar Padding */
section[data-testid="stSidebar"] .css-1d391kg {
    padding-top: 20px;
}

</style>
""", unsafe_allow_html=True)
# -------------------------------
# Header Section
# -------------------------------
st.markdown('<div class="main-title">🏥 Medical App Usage Prediction System</div>', unsafe_allow_html=True)

st.markdown('<div class="sub-text">Predict and analyze daily usage of a health monitoring app using mathematical modeling.</div>', unsafe_allow_html=True)

st.markdown("---")

# -------------------------------
# Cards Layout
# -------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h4>📈 Growth Modeling</h4>
    <p>Simulates how users increase over time using logistic growth.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h4>📊 Engagement Analysis</h4>
    <p>Analyzes active users and their daily check-in behavior.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h4>⏱ Peak Activity</h4>
    <p>Identifies when users are most active during the day.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# How it Works Section
# -------------------------------
st.markdown("## ⚙️ How It Works")

col4, col5 = st.columns(2)

with col4:
    st.markdown("""
    <div class="card">
    <ul>
        <li>User growth is modeled using a logistic function</li>
        <li>Only a fraction of users are active daily</li>
        <li>Active users perform health check-ins</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="card">
    <ul>
        <li>Usage varies across different times of the day</li>
        <li>Morning and evening peaks are identified</li>
        <li>Sensitivity analysis shows parameter impact</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# Key Insight Highlight
# -------------------------------
st.markdown("""
<div class="highlight">
💡 Key Insight: Increasing active users has a greater impact on app usage than simply increasing total users.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# -------------------------------
# Navigation Section
# -------------------------------
st.markdown("## 📂 Explore the App")

col6, col7, col8 = st.columns(3)

with col6:
    st.markdown("""
    <div class="card">
    <h4>📈 Model Page</h4>
    <p>Run simulations and adjust parameters.</p>
    </div>
    """, unsafe_allow_html=True)

with col7:
    st.markdown("""
    <div class="card">
    <h4>📊 Analysis Page</h4>
    <p>View graphs and trends of the model.</p>
    </div>
    """, unsafe_allow_html=True)

with col8:
    st.markdown("""
    <div class="card">
    <h4>🔍 Sensitivity Page</h4>
    <p>Understand how parameter changes affect results.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.success("👉 Use the sidebar to navigate between different sections of the app.")