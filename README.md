# **Financial Analytics Dashboard — SQL + Python + Streamlit**

This repository contains an end-to-end **Financial Analytics System** designed to transform raw financial records into **clean, structured, and decision-ready insights**.  
It integrates **data modeling**, **financial metric engineering**, **automated reporting**, and **interactive dashboards** across:

- A **Jupyter Notebook** for data preparation and modeling  
- A **Streamlit multi-page application** for interactive analytics  
- A **Tableau dashboard** for high-level executive summaries  

The project demonstrates a complete workflow used in modern Finance Data teams:  
**collect → clean → model → analyze → visualize → report**.

---

## **1. Overview**

This system provides a unified analytical experience for:

- **Transforming raw financial datasets** into structured tables  
- **Modeling user-level and category-level financial metrics**  
- **Analyzing budgets, spending behavior, and utilization**  
- **Generating automated visual reports**  
- **Tracking savings progress and financial goal timelines**  

The architecture is optimized for **transparency, speed, reproducibility, and auditability**, reflecting real-world FP&A, finance engineering, and BI workflows.

---

# **2. Project Components (Notebook + App + Tableau)**

## **2.1 Jupyter Notebook — Data Processing & Metric Engineering**  
`index.ipynb`

The notebook acts as the **data engineering backbone** of the project. It:

- Cleans and validates raw transaction, budget, and savings datasets  
- Performs SQL-style transformations using Pandas  
- Computes key financial metrics (income, expenses, savings, utilization, goal progress)  
- Standardizes date formats, categories, and classifications  
- Produces analytics-ready CSV outputs consumed by the Streamlit app  
- Documents each transformation step for traceability and reproducibility  

This ensures the project has a **clear, auditable data pipeline**, similar to production financial data workflows.

---

## **2.2 Streamlit Application — Interactive Financial Dashboard**  
`app.py` + `pages/`

The Streamlit app is the primary **interactive analytics interface**.  
Built with a **modular multi-page architecture**, it covers:

### **• User Profile Intelligence (pages/01_User_Profile.py)**  
- User-level metadata (occupation, city, annual income)  
- Savings goal summaries  
- On-track vs behind status scoring  

### **• Transactions Explorer (pages/02_Transactions_Explorer.py)**  
- SQL-like filtering and exploration (user → date → category → type)  
- Time-series trend analysis  
- Category-level aggregation  
- Full raw table view for auditability  

### **• Budget Analysis (pages/03_Budget_Analysis.py)**  
- Budget vs actual comparisons  
- Utilization rate calculations  
- Category/month heatmaps  
- Overspending alerts  
- FP&A-style budgeting view  

### **• Savings & Goals (pages/04_Savings_and_Goals.py)**  
- Progress ratio charts  
- Timeline visualizations (start → target date)  
- Goal performance segmentation  
- Savings KPIs  

This component provides a **flexible, data-driven interface** for financial exploration.

---

## **2.3 Tableau Dashboard — Executive Overview**

Live Dashboard: https://public.tableau.com/app/profile/linet.lydia/viz/FinancialManagementSystemFMS/Dashboard1-FinancialPerformanceOverview https://public.tableau.com/app/profile/linet.lydia/viz/FinancialManagementSystemFMS-D2/Dashboard2-Savinggoalsoverview?publish=yes

The accompanying Tableau dashboard provides:

- High-level summaries  
- Trend analysis  
- Interactive filters  
- Presentation-ready visuals  

While the Streamlit app supports **detailed investigation**,  
the Tableau dashboard supplies **board-level snapshots**, ideal for stakeholders.

All modules share:

- **Cache-optimized data loading (`@st.cache_data`)**  
- **Reusable pipelines**  
- **Consistent metrics and formatting**  

The system can scale to warehouse-backed pipelines (PostgreSQL, BigQuery, Snowflake, dbt).

---

# **3. Technologies Used**

### **Core Stack**
- **Python 3.10+**  
- **Streamlit 1.51.0**  
- **Pandas 2.3.3**  
- **Plotly Express 5.18.0**  
- **NumPy**  
- **Tableau Public**  

### **Dependencies (requirements.txt)**
- **streamlit==1.51.0**
- **pandas==2.3.3**
- **plotly==5.18.0**
- **numpy**


---

# **4. Data Model & Key Metrics**

The system models several financial dimensions:

---

### **User-Level Metrics**
- Annual income  
- City / occupation metadata  
- Priority-weighted goals  
- User financial profiling  

---

### **Transaction Metrics**
- Income / expense classification  
- Category-level summaries  
- Daily and monthly trends  
- Time-series patterns  

---

### **Budget Metrics**
- Budget vs actual variance  
- Utilization % by category & month  
- Overspending alerts  
- Risk identification  

---

### **Savings Metrics**
- Progress ratio (current / target)  
- Timeline tracking  
- On-track vs behind classification  
- Goal prioritization  

---

These metrics mirror real FP&A workflows where **auditable models**,  
**structured datasets**, and **clean documentation** support forecasting and strategic decision-making.

---

# **5. Streamlit Dashboard Modules (Detailed)**

## **5.1 Homepage (`app.py`)**
- Income, expenses, net savings KPIs  
- Monthly income vs expenses line charts  
- Category-level spending analysis  
- Savings goal progress  
- Budget utilization heatmap  

## **5.2 Transactions Explorer**
- SQL-style filtering tools  
- Category comparisons  
- Time-series visualizations  
- Full transactional table  

## **5.3 Budget Analysis**
- Grouped bar charts  
- Utilization heatmaps  
- Overspending warning panel  
- User-specific category breakdowns  

## **5.4 Savings & Goals**
- Horizontal bar progress visualization  
- Gantt-style timelines  
- Goal segmentation charts  
- Key savings performance numbers  

---

# **6. Installation & Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-repo-url.git
cd Financial_Analytics_Dashboard
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Launch the Streamlit Dashboard**
```bash
streamlit run app.py
```
OR

```bash
python -m streamlit run app.py
```

### **4. Open in Browser**
https://linetlydia-financial-management-system--financial-appapp-eqyngs.streamlit.app/

# **8. Use Cases**

This project supports workflows such as:

- **Financial operations & variance monitoring**

- **Budget planning and forecast preparation**

- **Expense reconciliation and classification**

- **Building internal finance data tools**

- **Modeling user-level financial behavior**

- **FP&A-driven reporting automation**

- **Personal finance analysis**

Possible extensions include:

- **Warehouse integration + dbt modeling**

- **AI-enhanced forecasting**

- **ARR, LTV, CAC modeling for SaaS finance**

- **Compensation automation workflows**

- **BI tool integrations**

# **9. Future Enhancements**

- PostgreSQL / BigQuery migration

- dbt transformation layer

- ML models for spending/savings forecasting

- PDF reporting automation

- Authentication & user roles

- Cloud storage ingestion

- Real-time data sync

# **10. Author**

**Linet Lydia Kagundu**
Finance & Data Analyst | SQL | Python | BI & Analytics
Focused on building **data-driven financial systems,**
scalable analytics workflows, and intelligent decision-support tools.
