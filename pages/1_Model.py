import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# -------------------------------
# DARK THEME CSS (Same as others)
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
st.title("📈 Model Simulation")

# -------------------------------
# Inputs
# -------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    K = st.sidebar.slider("Max Users (K)", 10000, 200000, 100000)

with col2:
    r = st.sidebar.slider("Growth Rate (r)", 0.01, 0.1, 0.03)

with col3:
    U0 = st.sidebar.slider("Initial Users (U0)", 100, 5000, 1000)

p = st.sidebar.slider("Active User % (p)", 0.1, 1.0, 0.4)
c = st.sidebar.slider("Check-ins per User (c)", 1, 10, 3)

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
# GRAPH + EXPLANATION
# -------------------------------
col_graph, col_text = st.columns([2, 1])

with col_graph:
    fig, ax = plt.subplots()
    ax.plot(t, checkins)
    ax.set_title("Daily Check-ins")
    ax.set_xlabel("Days")
    ax.set_ylabel("Check-ins")
    st.pyplot(fig)

with col_text:
    st.markdown("""
    <div class="card">
    <h4>📊 Model Insight</h4>
    <p>
    This graph shows how daily check-ins increase over time based on user growth and engagement.
    As the number of users rises and more users remain active, the total check-ins grow rapidly.
    </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# Key Insight
# -------------------------------
st.markdown("---")

st.success("💡 Insight: Daily check-ins are directly influenced by both user growth and engagement levels (p and c).")