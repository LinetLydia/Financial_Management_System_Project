import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Financial Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Load Data
# -------------------------------
@st.cache_data
def load_savings():
    return pd.read_csv("savings_progress.csv")

savings = load_savings()

# -------------------------------
# Page Layout
# -------------------------------
st.title("💰 Savings & Goals Dashboard")
st.markdown("Track savings goals, progress percentages, and timelines.")

st.sidebar.page_link("app.py", label="🏠 Dashboard")
st.sidebar.page_link("pages/01_User_Profile.py", label="👤 User Profile")
st.sidebar.page_link("pages/02_Transactions_Explorer.py", label="💳 Transactions Explorer")
st.sidebar.page_link("pages/03_Budget_Analysis.py", label="📊 Budget Analysis")
st.sidebar.page_link("pages/04_Savings_and_Goals.py", label="🎯 Savings & Goals")

# -------------------------------
# User Filter
# -------------------------------
users = savings["user_id"].unique()
selected_user = st.selectbox("Select User ID", users)

df = savings[savings["user_id"] == selected_user]

# -------------------------------
# KPI Section
# -------------------------------
st.subheader("📌 Key Savings Metrics")

col1, col2, col3 = st.columns(3)

total_target = df["target_amount"].sum()
total_current = df["current_amount"].sum()
avg_progress = df["progress_ratio"].mean() * 100

col1.metric("Total Savings Target", f"${total_target:,.0f}")
col2.metric("Current Savings", f"${total_current:,.0f}")
col3.metric("Avg Progress (%)", f"{avg_progress:.1f}%")

st.markdown("---")

# -------------------------------
# 1. Progress Bar Chart
# -------------------------------
st.subheader("📈 Savings Goal Progress")

fig1 = px.bar(
    df,
    x="progress_ratio",
    y="goal_name",
    orientation="h",
    labels={"progress_ratio": "Progress %"},
    color="progress_ratio",
    color_continuous_scale="Viridis"
)

st.plotly_chart(fig1, use_container_width=True)

# -------------------------------
# 2. Timeline (Start → Target Date)
# -------------------------------
st.subheader("📆 Savings Timeline")

fig2 = px.timeline(
    df,
    x_start="start_date",
    x_end="target_date",
    y="goal_name",
    color="goal_name"
)

fig2.update_yaxes(autorange="reversed")

st.plotly_chart(fig2, use_container_width=True)

# -------------------------------
# 3. On-track vs Behind
# -------------------------------
st.subheader("🚦 Goal Status (On Track vs Behind)")

status_counts = df["on_track"].value_counts()

fig3 = px.pie(
    values=status_counts.values,
    names=status_counts.index,
    color=status_counts.index,
    color_discrete_map={"On Track": "green", "Behind": "red"}
)

st.plotly_chart(fig3, use_container_width=True)
