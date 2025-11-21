import streamlit as st

# Page config
st.set_page_config(
    page_title="Welcome",
    layout="wide",
)

# ✨ HIDE STREAMLIT DEFAULT MULTIPAGE SIDEBAR
st.markdown("""
    <style>
        section[data-testid="stSidebarNav"] {display: none !important;}
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Custom Sidebar Navigation
# ----------------------------
st.sidebar.page_link("app.py", label="🏠 Dashboard")
st.sidebar.page_link("pages/01_User_Profile.py", label="👤 User Profile")
st.sidebar.page_link("pages/02_Transactions_Explorer.py", label="💳 Transactions Explorer")
st.sidebar.page_link("pages/03_Budget_Analysis.py", label="📊 Budget Analysis")
st.sidebar.page_link("pages/04_Savings_and_Goals.py", label="🎯 Savings & Goals")

# ----------------------------
# Page Content
# ----------------------------
st.title("✨ Financial Management System")

st.markdown("""
Welcome to the **Financial Analytics & Personal Finance Intelligence System**.  
This application integrates *data science, analytics, and interactive dashboards* to provide a full 360° view of an individual's financial activity.

--- 
## 🔍 What You Can Do Here
This system allows you to explore:

### **👤 User Profiles**
Understand individual financial behavior and income/expense patterns.

### **💳 Transactions Explorer**
Filter, search, and analyze detailed transaction records.

### **📊 Budget Analysis**
Track budget vs actual spending, overspending alerts, and heatmaps.

### **🎯 Savings & Goals**
Visualize savings targets, progress percentages, timelines, and prioritization.

---

## 📈 Technologies Used
This project showcases your skills in:

- **Python**
- **Pandas**
- **Plotly Express**
- **Streamlit**
- **Data Cleaning & Transformation**
- **Financial Analytics**
- **Interactive Dashboards**

---

## 🚀 Start Exploring
Choose a section from the sidebar to begin your analysis.

Or jump straight into the main dashboard:
""")

# Centered dashboard button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.page_link("app.py", label="➡️ Launch Dashboard")
