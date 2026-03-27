import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Medical App Usage Predictor", layout="wide")

st.title("📊 Medical App Daily Check-ins Prediction")
st.write("Growth Modeling + Sensitivity Analysis + Peak Activity Modeling")

# -------------------------------
# Sidebar Controls
# -------------------------------

st.sidebar.header("Model Parameters")

K = st.sidebar.slider("Carrying Capacity (Max Users)", 10000, 500000, 100000, step=10000)
r = st.sidebar.slider("Growth Rate (r)", 0.01, 0.1, 0.03, step=0.01)
U0 = st.sidebar.slider("Initial Users (U0)", 100, 10000, 1000, step=100)
p = st.sidebar.slider("Active User Percentage (p)", 0.1, 1.0, 0.4, step=0.05)
c = st.sidebar.slider("Check-ins per Active User (c)", 1, 10, 3)

days = st.sidebar.slider("Number of Days to Simulate", 30, 365, 180)

# -------------------------------
# Growth Model
# -------------------------------

def logistic_growth(t, K, r, U0):
    A = (K - U0) / U0
    return K / (1 + A * np.exp(-r * t))

def daily_checkins(t, K, r, U0, p, c):
    users = logistic_growth(t, K, r, U0)
    dau = users * p
    return users, dau, dau * c

t = np.linspace(0, days, days)

users, dau, checkins = daily_checkins(t, K, r, U0, p, c)

# -------------------------------
# Plots (Compact Layout)
# -------------------------------

col1, col2 = st.columns(2)

# Plot 1: User Growth
with col1:
    st.subheader("User Growth")
    fig1, ax1 = plt.subplots(figsize=(4,3))
    ax1.plot(t, users)
    ax1.set_xlabel("Days")
    ax1.set_ylabel("Users")
    ax1.set_title("Growth")
    st.pyplot(fig1, use_container_width=False)

# Plot 2: Daily Check-ins
with col2:
    st.subheader("Daily Check-ins")
    fig2, ax2 = plt.subplots(figsize=(4,3))
    ax2.plot(t, checkins)
    ax2.set_xlabel("Days")
    ax2.set_ylabel("Check-ins")
    ax2.set_title("Usage")
    st.pyplot(fig2, use_container_width=False)

# -------------------------------
# Peak Activity Modeling
# -------------------------------

st.subheader("Peak Activity (Hourly)")

hours = np.arange(0, 24)

def peak_distribution(hours):
    morning = np.exp(-0.5 * (hours - 8)**2)
    evening = np.exp(-0.5 * (hours - 20)**2)
    distribution = morning + evening
    return distribution / sum(distribution)

hourly_factor = peak_distribution(hours)
hourly_checkins = hourly_factor * checkins[-1]

fig3, ax3 = plt.subplots(figsize=(5,3))
ax3.plot(hours, hourly_checkins)
ax3.set_xlabel("Hour")
ax3.set_ylabel("Check-ins")
ax3.set_title("Peak Pattern")
st.pyplot(fig3, use_container_width=False)

# -------------------------------
# Sensitivity Analysis
# -------------------------------

st.subheader("Sensitivity Analysis (Active Users %)")

p_values = [p - 0.1 if p > 0.2 else p, p, p + 0.1 if p < 0.9 else p]

fig4, ax4 = plt.subplots(figsize=(5,3))

for val in p_values:
    _, _, sens_checkins = daily_checkins(t, K, r, U0, val, c)
    ax4.plot(t, sens_checkins, label=f"p={round(val,2)}")

ax4.set_xlabel("Days")
ax4.set_ylabel("Check-ins")
ax4.legend()
st.pyplot(fig4, use_container_width=False)

# -------------------------------
# Summary Metrics
# -------------------------------

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Users", f"{int(users[-1]):,}")
col2.metric("Active Users", f"{int(dau[-1]):,}")
col3.metric("Daily Check-ins", f"{int(checkins[-1]):,}")

st.write("This model demonstrates how growth rate, engagement, and activity timing influence daily usage of a health monitoring app.")