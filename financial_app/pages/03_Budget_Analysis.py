import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Financial Dashboard",
    layout="wide",
)

# HIDE STREAMLIT DEFAULT MULTIPAGE SIDEBAR
st.markdown("""
    <style>
        section[data-testid="stSidebarNav"] {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Load Data
# -------------------------------
@st.cache_data
def load_budget():
    return pd.read_csv("budget_vs_actual.csv")

budget = load_budget()

# -------------------------------
# Page Layout
# -------------------------------
st.title("📊 Budget Analysis Dashboard")
st.markdown("Compare **budgeted spending** vs **actual spending** and detect overspending risks.")

st.sidebar.page_link("app.py", label="🏠 Dashboard")
st.sidebar.page_link("pages/01_User_Profile.py", label="👤 User Profile")
st.sidebar.page_link("pages/02_Transactions_Explorer.py", label="💳 Transactions Explorer")
st.sidebar.page_link("pages/03_Budget_Analysis.py", label="📊 Budget Analysis")
st.sidebar.page_link("pages/04_Savings_and_Goals.py", label="🎯 Savings & Goals")

# -------------------------------
# User Filter
# -------------------------------
users = budget["user_id"].unique()
selected_user = st.selectbox("Select User ID", users)

df = budget[budget["user_id"] == selected_user]

# -------------------------------
# KPI Section
# -------------------------------
st.subheader("📌 Key Budget Metrics")

col1, col2, col3 = st.columns(3)

total_budget = df["budget_amount"].sum()
total_actual = df["actual_spent"].sum()
avg_util = df["utilization"].mean()

col1.metric("Total Budget", f"${total_budget:,.0f}")
col2.metric("Total Actual Spending", f"${total_actual:,.0f}")
col3.metric("Avg Utilization (%)", f"{avg_util:.1f}%")

st.markdown("---")

# -------------------------------
# 1. Budget vs Actual Bar Chart
# -------------------------------
st.subheader("📉 Budget vs Actual Spending per Category")

fig1 = px.bar(
    df,
    x="category_name",
    y=["budget_amount", "actual_spent"],
    barmode="group",
    labels={"value": "Amount", "category_name": "Category"},
    color_discrete_sequence=["#4C9AFF", "#FF4C4C"]
)

st.plotly_chart(fig1, use_container_width=True)

# -------------------------------
# 2. Utilization Heatmap
# -------------------------------
st.subheader("🔥 Budget Utilization Heatmap")

pivot = df.pivot_table(
    index="category_name",
    columns="month",
    values="utilization"
)

fig2 = px.imshow(
    pivot,
    aspect="auto",
    color_continuous_scale="RdYlGn_r",
    labels=dict(x="Month", y="Category", color="Utilization %"),
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------------
# Overspending Alerts
# -------------------------------
st.subheader("⚠️ Overspending Alerts")

alerts = df[df["utilization"] > 100]

if alerts.empty:
    st.success("No overspending detected. All categories are within budget.")
else:
    st.error("Overspending detected in the following categories:")
    st.dataframe(alerts[["month", "category_name", "utilization"]])
