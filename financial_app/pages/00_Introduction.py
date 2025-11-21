import streamlit as st

st.set_page_config(
    page_title="Welcome",
    layout="wide",
)

# SAFE hiding of Streamlit's default page list
st.markdown("""
<style>
/* Hide only the inner list of pages */
section[data-testid="stSidebarNav"] ul {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# Custom Navigation
st.sidebar.page_link("app.py", label="🏠 Dashboard")
st.sidebar.page_link("pages/01_User_Profile.py", label="👤 User Profile")
st.sidebar.page_link("pages/02_Transactions_Explorer.py", label="💳 Transactions Explorer")
st.sidebar.page_link("pages/03_Budget_Analysis.py", label="📊 Budget Analysis")
st.sidebar.page_link("pages/04_Savings_and_Goals.py", label="🎯 Savings & Goals")

# Page Content
st.title("✨ Financial Management System")
st.markdown("""
Welcome to the **Financial Analytics & Personal Finance Intelligence System**.

---

## 🔍 What You Can Do Here
### 👤 User Profiles
Analyze individual financial behavior.

### 💳 Transactions Explorer
Search & filter detailed financial transactions.

### 📊 Budget Analysis
Track overspending, heatmaps, and monthly insights.

### 🎯 Savings & Goals
Visualize goals, progress % and target completion dates.

---

## 🚀 Start Exploring
""")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.page_link("app.py", label="➡️ Launch Dashboard")


