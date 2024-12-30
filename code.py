import streamlit as st
import pandas as pd
import numpy as np

# Branding & Navigation
st.set_page_config(page_title="GlucoTrack Dashboard", layout="wide")

# Header Section
st.markdown(
    """
    <style>
    .header {
        background-color: #f8f9fa;
        padding: 10px;
        border-bottom: 1px solid #e0e0e0;
    }
    .header h1 {
        font-family: Arial, sans-serif;
        color: #333333;
        display: inline;
        margin-right: 50px;
    }
    .header img {
        float: left;
        margin-right: 15px;
    }
    </style>
    <div class="header">
        <img src="https://via.placeholder.com/50" alt="Logo">
        <h1>GlucoTrack Innovations</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.title("Navigation")
navigation = st.sidebar.radio(
    "Go to:", ["Home", "Device Settings", "Data Insights", "Reports", "Settings", "Profile"]
)

# Device Status Section
if navigation == "Home":
    st.title("Device Status")
    st.write("Monitor your device's real-time performance and data.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Device Health")
        st.success("Device is functioning properly.")

    with col2:
        st.subheader("Battery Status")
        st.progress(80)

    with col3:
        st.subheader("Last Sync")
        st.write("Last Synced: 5 minutes ago")

# Glucose Monitoring Data Section
if navigation == "Data Insights":
    st.title("Glucose Monitoring")
    st.subheader("Real-Time Glucose Levels")

    # Simulating real-time glucose data
    glucose_level = np.random.randint(70, 150)
    st.metric("Current Blood Glucose", f"{glucose_level} mg/dL")

    # Trends
    st.subheader("Glucose Trends")
    date_range = pd.date_range(start="2024-12-01", periods=30, freq="D")
    glucose_trends = pd.DataFrame({
        "Date": date_range,
        "Glucose Level": np.random.randint(70, 180, size=(30,))
    }).set_index("Date")
    st.line_chart(glucose_trends)

    # Alerts
    st.subheader("Alerts")
    if glucose_level > 140:
        st.error("High Glucose Alert: Immediate action required!")
    elif glucose_level < 80:
        st.warning("Low Glucose Alert: Consider eating or adjusting medication.")
    else:
        st.success("Glucose levels are within the normal range.")

# Data Insights Section
if navigation == "Reports":
    st.title("Data Insights")
    st.subheader("Statistics and Recommendations")

    # Example data
    insights = {
        "Average Glucose Level": "110 mg/dL",
        "Lowest Level": "65 mg/dL",
        "Highest Level": "145 mg/dL",
    }
    for key, value in insights.items():
        st.write(f"**{key}**: {value}")

    st.subheader("Glucose Distribution")
    glucose_distribution = pd.DataFrame({
        "Category": ["Normal", "High", "Low"],
        "Percentage": [65, 25, 10]
    })
    st.bar_chart(glucose_distribution.set_index("Category"))

    # Recommendations
    st.subheader("Personalized Recommendations")
    st.write("Your glucose trend shows higher levels in the morning. Consider adjusting your diet or medication.")

# Settings Section
if navigation == "Settings":
    st.title("Settings")
    st.subheader("Device Preferences")
    st.checkbox("Enable Real-Time Monitoring")
    st.checkbox("Enable Notifications for High/Low Glucose")

    st.subheader("Profile Settings")
    name = st.text_input("Name", "John Doe")
    age = st.number_input("Age", 18, 100, 30)
    weight = st.number_input("Weight (kg)", 40, 150, 70)
    diabetes_type = st.selectbox("Diabetes Type", ["Type 1", "Type 2", "Gestational", "Other"])
    st.write(f"Profile updated for: {name}, Age: {age}, Weight: {weight} kg, Diabetes: {diabetes_type}")

# Footer
st.markdown(
    """
    <footer style='text-align: center; font-size: 0.9em; color: #555;'>
        © 2024 GlucoTrack Innovations | <a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a>
    </footer>
    """,
    unsafe_allow_html=True,
)
