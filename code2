import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set up the app title and layout
st.set_page_config(page_title="GlucoTrack Innovations", layout="wide")

# Company Branding & Header
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>GlucoTrack Innovations</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #34495e;'>Revolutionizing Non-Invasive Glucose Monitoring</h4>", unsafe_allow_html=True)

# Navigation Menu
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Device Status", "Glucose Monitoring Data", "Data Insights", "Remote Monitoring", "Settings & Profile"],
    index=0
)

# Dummy Data for Testing
np.random.seed(42)
dates = pd.date_range(end=datetime.today(), periods=30)
glucose_levels = np.random.randint(70, 180, size=len(dates))
glucose_data = pd.DataFrame({"Date": dates, "Glucose Level (mg/dL)": glucose_levels})

# Home Page
if menu == "Home":
    st.subheader("Welcome to GlucoTrack Innovations Dashboard")
    st.markdown("""
    - **Real-Time Glucose Monitoring**: Stay on top of your glucose levels with real-time data.
    - **Advanced Analytics**: Get insights and trends to better manage your health.
    - **IoT-Enabled**: Seamlessly connect your device to track data anytime, anywhere.
    """)
    st.image("https://via.placeholder.com/800x400?text=GlucoTrack+Innovations+Dashboard", caption="Innovative Health Monitoring")

# Device Status Section
if menu == "Device Status":
    st.subheader("Device Status")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Device Health", "Operational", delta="Stable", delta_color="normal")
    with col2:
        st.metric("Battery Status", "85%", delta="-5% since last sync", delta_color="inverse")
    with col3:
        st.metric("Last Sync", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Glucose Monitoring Data Section
if menu == "Glucose Monitoring Data":
    st.subheader("Real-Time Glucose Monitoring")
    current_glucose = np.random.randint(80, 150)
    st.metric("Current Glucose Level", f"{current_glucose} mg/dL", delta="Normal Range")

    st.subheader("Glucose Trends (Last 7 Days)")
    weekly_data = glucose_data.tail(7)
    st.line_chart(weekly_data.set_index("Date"))

    st.subheader("Alerts")
    if current_glucose < 70:
        st.error("Low Glucose Alert! Take immediate action.")
    elif current_glucose > 180:
        st.error("High Glucose Alert! Please monitor your diet or medication.")
    else:
        st.success("Glucose levels are stable.")

# Data Insights Section
if menu == "Data Insights":
    st.subheader("Statistics & Insights")
    avg_glucose = glucose_data["Glucose Level (mg/dL)"].mean()
    st.metric("Average Glucose Level", f"{avg_glucose:.2f} mg/dL")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### Glucose Level Distribution")
        distribution = pd.DataFrame({
            "Category": ["Normal", "High", "Low"],
            "Count": [np.sum((glucose_data["Glucose Level (mg/dL)"] >= 70) & (glucose_data["Glucose Level (mg/dL)"] <= 140)),
                      np.sum(glucose_data["Glucose Level (mg/dL)"] > 140),
                      np.sum(glucose_data["Glucose Level (mg/dL)"] < 70)]
        })
        st.bar_chart(distribution.set_index("Category"))
    with col2:
        st.write("### Personalized Recommendations")
        st.markdown("""
        - **Morning Glucose Trends**: Consider adjusting breakfast to manage spikes.
        - **Exercise**: Regular physical activity can help stabilize your levels.
        - **Diet Tips**: Focus on low-GI foods to reduce fluctuations.
        """)

# Remote Monitoring Section
if menu == "Remote Monitoring":
    st.subheader("Doctor's View")
    st.markdown("Allow healthcare providers to remotely monitor your glucose data.")
    st.write("### 30-Day Glucose Trends")
    st.line_chart(glucose_data.set_index("Date"))

# Settings & Profile Section
if menu == "Settings & Profile":
    st.subheader("User Profile & Device Settings")
    st.text_input("Name", "Aditya Chourasia")
    st.number_input("Age", value=30, min_value=1)
    st.selectbox("Diabetes Type", ["Type 1", "Type 2", "Gestational"])
    st.slider("Notification Thresholds (mg/dL)", 50, 300, (70, 180))

    st.write("### Device Preferences")
    st.checkbox("Enable Real-Time Data Sync")
    st.checkbox("Send Alerts to Healthcare Provider")

    st.write("### Connectivity Settings")
    st.radio("Connection Type", ["Wi-Fi", "Bluetooth", "Mobile Data"])

st.sidebar.info("GlucoTrack Innovations © 2024")
