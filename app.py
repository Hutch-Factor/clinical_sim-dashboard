#Streamlit Script
import streamlit as st
import pandas as pd

#Load data
df = pd.read_csv("life_support_summary.csv")

#Title
st.title("🩺 Clinical Simulation Dashboard")
st.subheader("Life Support Training Overview (FY24)")

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

#KPI Section
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Learners Attended", total_learners)
col2.metric("Sessions Run", total_sessions)
col3.metric("Attendance Rate", f"{attendance_rate:.1%}")
col4.metric("Utilization Rate", f"{utilization_rate:.1%}")
col5.metric("No Show Rate", f"{no_show_rate:.1%}")

st.divider()

#---Visualizations---

#Attendance per Course
st.subheader("Learners Attended per Course")
st.bar_chart(df.set_index("course_name")["learners_attended"])

#Attendance Rate
st.subheader("Attendance Rate per Course")
df["attendance_rate"] = df["learners_attended"] / df["max_enrollment"]
st.bar_chart(df.set_index("course_name")["attendance_rate"])

#No Show Rate
st.subheader("No-Shows per Course")
st.bar_chart(df.set_index("course_name")["total_no_shows"])

#Raw Data Toggle
with st.expander("🔍 Show Raw Data Table"):
  st.dataframe(df)

st.caption("FY24 Clinical Simulation Summary - Created by Ray Hutchinson")

st.caption("FY24 Clinical Simulation Summary - Created by Ray Hutchinson")
