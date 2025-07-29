#Streamlit Script
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Life Support Training Dashboard", layout="wide")

#Load data
df = pd.read_csv("life_support_summary.csv")

#---KPI Metrics---
total_sessions = df["total_number_sessions"].sum()
total_learners = df["learners_attended"].sum()
max_enrollment = df["max_enrollment"].sum()
course_openings = df["course_openings"].sum()
no_shows = df["total_no_shows"].sum()

attendance_rate = total_learners / max_enrollment if max_enrollment else 0
utilization_rate = total_learners / course_openings if course_openings else 0
no_show_rate = no_shows / course_openings if course_openings else 0

#---Streamlit UI---
st.title("FY24 Life Support Training Dashboard")

#KPI Section
col1, col2, col3, col4, col5 = st.columns(3)
col1.metric("Learners Attended", total_learners)
col2.metric("Sessions Run", total_sessions)
col3.metric("Attendance Rate", f"{attendance_rate:.1%}")
col4.metric("Utilization Rate", f"{utilization_rate:.1%}")
col5.metric("No Show Rate", f"{no_show_rate:.1%}")

st.divider()

#---Visualizations---
st.subheader("Learners Attended per Course")
st.bar_chart(df.set_index("course_name")["learners_attended"])

st.subheader("Attendance Rate per Course")
df["attendance_rate"] = df["learners_attended"] / df["max_enrollment"]
st.bar_chart(df.set_index("course_name")["attendance_rate"])

st.subheader("No-Shows per Course")
st.bar_chart(df.set_index("course_name")["total_no_shows"])
