import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Function to simulate glucose data
def generate_glucose_data():
    # Simulate glucose levels for the past 7 days
    times = [datetime.now() - timedelta(days=i) for i in range(7)]
    glucose_levels = np.random.normal(loc=100, scale=15, size=7)  # Simulated glucose levels
    glucose_data = pd.DataFrame({
        'Timestamp': times,
        'Glucose Level (mg/dL)': glucose_levels
    })
    return glucose_data

# Sidebar for User Profile
def user_profile():
    st.sidebar.header("User Profile")
    st.sidebar.text("Name: John Doe")
    st.sidebar.text("Age: 45")
    st.sidebar.text("Diabetes Type: Type 2")
    st.sidebar.text("Target Glucose Range: 70 - 130 mg/dL")

# Sidebar for Alerts
def glucose_alerts(glucose_data):
    st.sidebar.header("Alerts")
    latest_glucose = glucose_data['Glucose Level (mg/dL)'].iloc[-1]
    
    if latest_glucose > 180:
        st.sidebar.warning(f"High glucose alert: {latest_glucose:.2f} mg/dL")
    elif latest_glucose < 70:
        st.sidebar.warning(f"Low glucose alert: {latest_glucose:.2f} mg/dL")
    else:
        st.sidebar.success(f"Current glucose level: {latest_glucose:.2f} mg/dL - Normal")

# Main Dashboard
def main_dashboard():
    # Title and introduction
    st.title("GlucoTrack Innovations Dashboard")
    st.subheader("Real-time Glucose Monitoring and Insights")
    st.markdown("""
    Welcome to the GlucoTrack Innovations dashboard. This dashboard provides you with real-time glucose level monitoring, trends, and personalized insights.
    """)
    
    # Generate glucose data (for demo purposes)
    glucose_data = generate_glucose_data()
    
    # Display Real-time Glucose Level
    latest_glucose = glucose_data['Glucose Level (mg/dL)'].iloc[-1]
    st.metric(label="Current Glucose Level", value=f"{latest_glucose:.2f} mg/dL", delta="0.5 mg/dL")
    
    # Display Real-time Data Graph
    st.subheader("Glucose Level Trend (Last 7 Days)")
    fig, ax = plt.subplots()
    ax.plot(glucose_data['Timestamp'], glucose_data['Glucose Level (mg/dL)'], marker='o', linestyle='-', color='blue')
    ax.set_title("Glucose Levels Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Glucose Level (mg/dL)")
    ax.axhline(y=130, color='green', linestyle='--', label="Upper Target Limit")
    ax.axhline(y=70, color='red', linestyle='--', label="Lower Target Limit")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    # Display Data Insights
    st.subheader("Personalized Insights")
    avg_glucose = glucose_data['Glucose Level (mg/dL)'].mean()
    st.write(f"Your average glucose level over the last 7 days is: {avg_glucose:.2f} mg/dL.")
    
    # Recommendations
    if latest_glucose > 180:
        st.write("Consider reviewing your insulin dosage or meal plan.")
    elif latest_glucose < 70:
        st.write("Consider having a quick snack or consulting your healthcare provider.")
    else:
        st.write("Your glucose levels are within the target range. Keep up the good work!")
    
    # Footer with Contact Information
    st.markdown("""
    ---
    **Contact Information**  
    Email: support@glucotrack.com  
    Phone: +123 456 7890
    """)

# Page Layout and User Interaction
def main():
    # Sidebar setup
    user_profile()
    glucose_alerts(generate_glucose_data())
    
    # Main Dashboard Content
    main_dashboard()

# Run the application
if __name__ == "__main__":
    main()
