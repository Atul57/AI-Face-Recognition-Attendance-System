import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="AI Attendance Dashboard",
    page_icon="🎓",
    layout="wide"
)

# ---------------------------
# AUTO REFRESH EVERY 5 SECONDS
# ---------------------------
st_autorefresh(interval=5000, key="attendance_refresh")

# ---------------------------
# CUSTOM STYLING (EPIC UI)
# ---------------------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

h1 {
    text-align: center;
}

.metric-card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# DATABASE CONNECTION
# ---------------------------
@st.cache_data
def get_data():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Atul",
        database="attendance_system"
    )

    query = "SELECT * FROM attendance"

    df = pd.read_sql(query, conn)

    conn.close()

    return df




df = get_data()

# ---------------------------
# TITLE
# ---------------------------
st.title("🎓 AI Face Recognition Attendance Dashboard")

st.markdown("---")

# ---------------------------
# METRICS SECTION
# ---------------------------
col1, col2, col3 = st.columns(3)

total_students = df["student_name"].nunique()

today = pd.Timestamp.today().strftime("%Y-%m-%d")

today_attendance = df[df["date"] == today].shape[0]

total_records = df.shape[0]

col1.metric("👨‍🎓 Total Students", total_students)
col2.metric("📅 Today's Attendance", today_attendance)
col3.metric("📊 Total Records", total_records)

st.markdown("---")

# ---------------------------
# ATTENDANCE TABLE
# ---------------------------
st.subheader("📋 Attendance Records")

df_sorted = df.sort_values(by="date", ascending=False)

st.dataframe(df_sorted, width="stretch")

st.markdown("---")

# ---------------------------
# CHART 1 : ATTENDANCE PER STUDENT
# ---------------------------
st.subheader("📊 Attendance Distribution")

attendance_count = df["student_name"].value_counts().reset_index()

attendance_count.columns = ["Student", "Count"]

fig = px.bar(
    attendance_count,
    x="Student",
    y="Count",
    color="Student",
    title="Attendance Per Student"
)

st.plotly_chart(fig, width="stretch")

st.markdown("---")

# ---------------------------
# CHART 2 : DAILY ATTENDANCE
# ---------------------------
st.subheader("📅 Attendance Over Time")

attendance_time = df.groupby("date").size().reset_index(name="count")

fig2 = px.line(
    attendance_time,
    x="date",
    y="count",
    markers=True,
    title="Daily Attendance Trend"
)

st.plotly_chart(fig2, width="stretch")

st.markdown("---")

# ---------------------------
# STUDENT SEARCH
# ---------------------------
st.subheader("🔍 Search Student Attendance")

student = st.selectbox(
    "Select Student",
    df["student_name"].unique()
)

student_df = df[df["student_name"] == student]

st.dataframe(student_df, width="stretch")

st.markdown("---")

# ---------------------------
# FOOTER
# ---------------------------
st.caption("AI Attendance System • Auto-refresh every 5 seconds")

# streamlit run dashboard.py
