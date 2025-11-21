import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------
# Load Data
# ----------------------------------------
@st.cache_data
def load_savings():
    return pd.read_csv("savings_progress.csv")

savings = load_savings()

# ----------------------------------------
# Page Layout
# ----------------------------------------
st.set_page_config(page_title="User Profile", layout="wide")

st.title("👤 User Profile Overview")

st.sidebar.page_link("app.py", label="🏠 Dashboard")
st.sidebar.page_link("pages/01_User_Profile.py", label="👤 User Profile")
st.sidebar.page_link("pages/02_Transactions_Explorer.py", label="💳 Transactions Explorer")
st.sidebar.page_link("pages/03_Budget_Analysis.py", label="📊 Budget Analysis")
st.sidebar.page_link("pages/04_Savings_and_Goals.py", label="🎯 Savings & Goals")

# Sidebar user selector
st.sidebar.header("Select User")
users = savings["user_id"].unique()
selected_user = st.sidebar.selectbox("User ID", users)

# Filter data for selected user
user_data = savings[savings["user_id"] == selected_user].iloc[0]

# ----------------------------------------
# Basic Information
# ----------------------------------------
st.subheader("📌 Basic Information")

col1, col2, col3 = st.columns(3)
col1.metric("User ID", selected_user)
col2.metric("Occupation", user_data["occupation"])
col3.metric("City", user_data["city"])

annual_income = user_data["annual_income"]

st.markdown(
    f"""
    ### 💼 Annual Income  
    **${annual_income:,.0f}**
    """
)

st.markdown("---")

# ----------------------------------------
# Savings Goals
# ----------------------------------------
st.subheader("🎯 Savings Goals")

goals = savings[savings["user_id"] == selected_user][["goal_name", "current_amount", "target_amount", "progress_ratio"]]

for idx, row in goals.iterrows():
    st.write(f"**{row['goal_name']}**")
    st.progress(min(row["progress_ratio"], 1.0))  # progress bar max is 1.0
    st.write(f"${row['current_amount']:,.0f} of ${row['target_amount']:,.0f}")
    st.write("")

st.markdown("---")

# ----------------------------------------
# Priority & Status Visualization
# ----------------------------------------
st.subheader("📊 Goal Priority & Status")

fig_priority = px.bar(
    goals,
    x="goal_name",
    y="progress_ratio",
    color="progress_ratio",
    color_continuous_scale="Blues",
    labels={"progress_ratio": "Progress"},
    height=400,
)

st.plotly_chart(fig_priority, use_container_width=True)

st.markdown("---")

# ----------------------------------------
# Insights Section
# ----------------------------------------
st.subheader("💡 Personalized Insights")

# On track or behind
on_track_goals = savings[(savings["user_id"] == selected_user) & (savings["on_track"] == 1)]
off_track_goals = savings[(savings["user_id"] == selected_user) & (savings["on_track"] == 0)]

if len(on_track_goals) > 0:
    st.success(f"👍 {len(on_track_goals)} goals are on track!")

if len(off_track_goals) > 0:
    st.error(f"⚠ {len(off_track_goals)} goals are falling behind. Review budget allocation.")

# Priority warnings
high_priority = goals[goals["target_amount"] > annual_income * 0.5]
if len(high_priority) > 0:
    st.warning("🔥 High priority savings goals detected. Consider adjusting monthly contributions.")

st.info("This page provides a user-level financial summary ideal for FP&A, strategic finance, and personal budgeting systems.")
