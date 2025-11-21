# Financial Management System (SQL + Python + Tableau)

This project demonstrates the end-to-end development of a Financial Management System (FMS) using SQLite (SQL), Python, and Tableau Public.  
The system stores income, expenses, budgets, and savings goals, and visualizes key financial insights through interactive dashboards.

---

## 1. Project Overview

The Financial Management System was designed to:

- Store and organize financial transactions  
- Track income and expenses across multiple categories  
- Monitor monthly budgets and identify overspending  
- Analyze spending trends and financial behavior  
- Evaluate progress toward savings goals  
- Generate visual financial summaries through Tableau

This project showcases skills in database design, SQL querying, Python-based data engineering, and Tableau dashboard development.

---

## 2. Technologies Used

- **Python:** sqlite3, pandas, datetime, random  
- **SQLite Database**  
- **Tableau Public** (interactive dashboards)  
- **Jupyter Notebook**  
- **Markdown** for documentation  

---

## 3. Database Schema (ER Diagram)

The Financial Management System uses six main tables:

1. **Users**  
2. **Accounts**  
3. **Categories**  
4. **Transactions**  
5. **Budgets**  
6. **SavingsGoals**  

These tables include primary keys, foreign keys, constraints, and appropriate relationships.

*ER Diagram to be added* (can be generated using dbdiagram.io, DrawSQL, or Lucidchart).

---

## 4. SQL & Python Pipeline

### 4.1 Schema Creation (Python + SQLite)

All database tables were created using Python’s sqlite3 module.

**Example — Users Table**  
***sql
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

### 4.2 Data Generation & Insertion

Python was used to generate realistic synthetic data for:

- Users  
- Accounts  
- Financial categories  
- Transactions (3,000+ entries)  
- Budgets  
- Savings goals  

**Example — Category Insertion**
***sql
INSERT INTO Categories (category_name, category_type)
VALUES 
("Salary", "Income"),
("Groceries", "Expense"),
("Rent", "Expense");

### 4.3 Feature Engineering (SQL Views)

Several SQL views were created to support analysis and simplify reporting.  
These views aggregate financial data and prepare it for Tableau visualization.

The main views include:

- **MonthlySummary**  
- **CategorySpending**  
- **BudgetVsActual**  
- **SavingsProgress**

**Example — Savings Progress View**
***sql
CREATE VIEW IF NOT EXISTS SavingsProgress AS
SELECT 
    user_id,
    goal_name,
    target_amount,
    current_amount,
    ROUND((current_amount * 100.0) / target_amount, 2) AS progress_percentage
FROM SavingsGoals;

### 4.4 Analytical SQL Queries

Python executed several SQL queries to generate financial insights, including:

- **Monthly income vs expenses**
- **Spending by category**
- **Budget utilization tracking**
- **Savings goal progress analysis**

These queries pulled data from both raw tables and SQL views created earlier.

**Example — Retrieve Monthly Summary**
***sql
SELECT *
FROM MonthlySummary
ORDER BY year_month;

## 5. Tableau Visualizations

An interactive Tableau dashboard was created to display key financial insights and trends.

**Live Dashboard:**  
https://public.tableau.com/authoring/FinancialManagementDashboardFinal/Dashboard1-FinancialPerformanceOverview#1

The dashboard includes the following visualizations:

- **Monthly Income vs Expenses** — Line Chart  
- **Spending by Category** — Bar Chart  
- **Budget Utilization** — Heatmap  
- **Savings Goal Progress** — Bar Chart  
- **Savings Timeline** — Gantt Chart  

These visualizations provide a comprehensive view of financial behavior, helping identify trends, overspending, and long-term progress toward goals.

## 6. Conclusion

This project demonstrates how **SQL**, **Python**, and **Tableau** can be integrated to build a complete financial analytics system.  
The Financial Management System supports:

- Expense tracking  
- Income analysis  
- Monthly budget monitoring  
- Savings goal evaluation  
- Visual and statistical financial insights  

It highlights strong skills in **data engineering**, **SQL analytics**, and **business intelligence**, resulting in a fully functional, end-to-end analytical solution.

## 7. Author

**Linet Lydia Kagundu**  
Data Science Student | Financial Data Analyst  
Nairobi, Kenya

