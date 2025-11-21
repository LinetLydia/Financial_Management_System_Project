import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    monthly = pd.read_csv("monthly_summary.csv")
    category = pd.read_csv("category_spending.csv")
    savings = pd.read_csv("savings_progress.csv")
    budget = pd.read_csv("budget_vs_actual.csv")
    return monthly, category, savings, budget


# Load CSV data
monthly, category, savings, budget = load_data()


# --------------------------
# Streamlit Layout
# --------------------------
st.set_page_config(page_title="Financial Analytics Dashboard", layout="wide")
st.title("💰 Financial Analytics Dashboard")
st.markdown("Interactive analytics powered by **Python + Streamlit**")


# --------------------------
# Sidebar Filters
# --------------------------
st.sidebar.header("Filters")
users = monthly["user_id"].unique()
selected_user = st.sidebar.selectbox("Select User ID", users)

monthly = monthly[monthly["user_id"] == selected_user]
category = category[category["user_id"] == selected_user]
savings = savings[savings["user_id"] == selected_user]
budget = budget[budget["user_id"] == selected_user]


# --------------------------
# KPIs
# --------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)
total_income = monthly["total_income"].sum()
total_expenses = monthly["total_expenses"].sum()
total_savings = total_income - total_expenses

col1.metric("Total Income", f"${total_income:,.0f}")
col2.metric("Total Expenses", f"${total_expenses:,.0f}")
col3.metric("Net Savings", f"${total_savings:,.0f}")

st.markdown("---")


# --------------------------
# Income vs Expenses Trend
# --------------------------
st.subheader("📈 Monthly Income vs Expenses")

fig1 = px.line(
    monthly,
    x="month",
    y=["total_income", "total_expenses"],
    markers=True,
    labels={"value": "Amount", "month": "Month"},
)

st.plotly_chart(fig1, use_container_width=True)


# --------------------------
# Spending by Category
# --------------------------
st.subheader("🛒 Spending by Category")

fig2 = px.bar(
    category.sort_values("total_spent", ascending=True),
    x="total_spent",
    y="category_name",
    orientation="h",
    color="total_spent",
    color_continuous_scale="Blues",
)

st.plotly_chart(fig2, use_container_width=True)


# --------------------------
# Savings Progress
# --------------------------
st.subheader("💡 Savings Goal Progress")

fig3 = px.bar(
    savings,
    x="progress_ratio",
    y="goal_name",
    orientation="h",
    color="progress_ratio",
    color_continuous_scale="Viridis",
    labels={"progress_ratio": "Progress (%)"}
)

st.plotly_chart(fig3, use_container_width=True)

# --------------------------
# Budget Utilization Heatmap
# --------------------------
st.subheader("🔥 Budget Utilization (Monthly)")

pivot = budget.pivot_table(
    index="category_name",
    columns="month",
    values="utilization"
)

fig4 = px.imshow(
    pivot,
    aspect="auto",
    color_continuous_scale="RdYlGn_r",
    labels=dict(x="Month", y="Category Name", color="Utilization %"),
)

st.plotly_chart(fig4, use_container_width=True)

