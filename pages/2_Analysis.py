import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# -------------------------------
# DARK THEME CSS
# -------------------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: #e2e8f0;
}

/* Card */
.card {
    background-color: #1e293b;
    padding: 18px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.6);
    border: 1px solid #334155;
    margin-bottom: 20px;
}

/* Titles */
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
# Title
# -------------------------------
st.title("📊 Analysis & Visualization Dashboard")

# -------------------------------
# Inputs
# -------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    K = st.sidebar.slider("Max Users", 10000, 200000, 100000)

with col2:
    r = st.sidebar.slider("Growth Rate", 0.01, 0.1, 0.03)

with col3:
    U0 = st.sidebar.slider("Initial Users", 100, 5000, 1000)

p = st.sidebar.slider("Active %", 0.1, 1.0, 0.4)
c = st.sidebar.slider("Check-ins per User", 1, 10, 3)

t = np.linspace(0, 180, 180)

# -------------------------------
# Model
# -------------------------------
def logistic(t):
    A = (K - U0) / U0
    return K / (1 + A * np.exp(-r * t))

users = logistic(t)
checkins = users * p * c

# -------------------------------
# GRAPH 1: USER GROWTH
# -------------------------------
col_g1, col_g1_text = st.columns([2, 1])

with col_g1:
    fig1, ax1 = plt.subplots()
    ax1.plot(t, users)
    ax1.set_title("User Growth Over Time")
    ax1.set_xlabel("Days")
    ax1.set_ylabel("Users")
    st.pyplot(fig1)

with col_g1_text:
    st.markdown("""
    <div class="card">
    <h4>📈 Growth Insight</h4>
    <p>
    This graph shows how the number of users increases over time following a logistic growth pattern.
    Growth is slow initially, accelerates in the middle phase, and gradually stabilizes as it reaches capacity.
    </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -------------------------------
# GRAPH 2: DAILY APP USAGE
# -------------------------------
col_g2, col_g2_text = st.columns([2, 1])

with col_g2:
    fig2, ax2 = plt.subplots()
    ax2.plot(t, checkins)
    ax2.set_title("Daily App Usage")
    ax2.set_xlabel("Days")
    ax2.set_ylabel("Check-ins")
    st.pyplot(fig2)

with col_g2_text:
    st.markdown("""
    <div class="card">
    <h4>📊 Usage Insight</h4>
    <p>
    This graph represents total daily check-ins based on user growth and engagement levels.
    As more users become active and perform check-ins, the overall app usage increases significantly.
    </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -------------------------------
# GRAPH 3: PEAK ACTIVITY
# -------------------------------
hours = np.arange(0, 24)

def peak_distribution(hours):
    morning = np.exp(-0.5 * (hours - 8)**2)
    evening = np.exp(-0.5 * (hours - 20)**2)
    dist = morning + evening
    return dist / sum(dist)

hourly = peak_distribution(hours)
hourly_usage = hourly * checkins[-1]

col_g3, col_g3_text = st.columns([2, 1])

with col_g3:
    fig3, ax3 = plt.subplots()
    ax3.plot(hours, hourly_usage)
    ax3.set_title("Peak Activity Distribution")
    ax3.set_xlabel("Hour")
    ax3.set_ylabel("Check-ins")
    st.pyplot(fig3)

with col_g3_text:
    st.markdown("""
    <div class="card">
    <h4>⏱ Peak Insight</h4>
    <p>
    This graph shows how user activity varies throughout the day.
    Two clear peaks indicate higher engagement during morning and evening routines.
    </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# Final Insight
# -------------------------------
st.markdown("---")

st.success("💡 Insight: User engagement (active users and check-ins) has a stronger impact on usage than growth alone.")