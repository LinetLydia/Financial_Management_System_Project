# **Financial Management System (SQL + Python + Tableau)**

This project demonstrates the end-to-end development of a **Financial Management System (FMS)** using SQL (SQLite), Python, and Tableau.  
The system tracks **income, expenses, budgets, and savings goals**, and visualizes financial insights through an interactive Tableau dashboard.

---

# **1. Project Overview**
The Financial Management System was built to:

- Store and organize personal financial transactions  
- Track income and expenses  
- Monitor monthly budgets  
- Analyze financial trends  
- Evaluate progress toward savings goals  
- Generate visual summaries of spending and savings  

This project showcases skills in **database design**, **SQL querying**, **Python data engineering**, and **Tableau visualization**.

---

# **2. Technologies Used**
- **Python** (sqlite3, pandas)  
- **SQLite Database**  
- **Tableau Public** (Interactive dashboard)  
- **Jupyter Notebook**  
- **Markdown**

---

# **3. Database Schema (ER Diagram)**
The system uses six core tables:

- `Users`  
- `Accounts`  
- `Categories`  
- `Transactions`  
- `Budgets`  
- `SavingsGoals`

**ER Diagram (to add later):**  
*You can generate it using dbdiagram.io, DrawSQL, or Lucidchart.*

---

# **4. SQL & Python Pipeline**

## **4.1 Data Preparation (Schema Creation)**  
All tables were created in Python using `sqlite3`:

```python
# Example: Users Table
cur.execute("""
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
""")
```

The full schema includes primary keys, foreign keys, and constraints for data integrity.

---

## **4.2 Sample Data Insertion**
Python was used to insert sample:

- Users  
- Accounts  
- Categories  
- Transactions  
- Budgets  
- Savings Goals  

Example insertion:

```python
cur.executemany("""
INSERT INTO Categories (category_name, category_type)
VALUES (?, ?);
""", [
    ("Salary", "Income"),
    ("Groceries", "Expense"),
    ("Rent", "Expense"),
    ("Utilities", "Expense"),
    ("Freelance", "Income")
])
```

---

## **4.3 Feature Engineering (SQL Views)**  
These SQL Views were created:

- `IncomeExpenseSummary`  
- `CategorySpending`  
- `MonthlySummary`  
- `SavingsProgress`  

Example:

```sql
CREATE VIEW IF NOT EXISTS SavingsProgress AS
SELECT 
    user_id,
    goal_name,
    target_amount,
    current_amount,
    ROUND((current_amount * 100.0) / target_amount, 2) AS progress_percentage
FROM SavingsGoals;
```

---

## **4.4 Analytical SQL Queries**
Python executed analysis queries such as:

- Monthly income vs expenses  
- Category spending  
- Savings goal progress  
- Monthly savings trends  

Example:

```sql
SELECT *
FROM MonthlySummary
ORDER BY year_month;
```

---

# **5. Tableau Visualizations**

## **Interactive Dashboard**
View the live dashboard here:

**https://public.tableau.com/app/profile/linet.lydia/viz/financemanagementsystemdashboard/Dashboard2**

---

## **Dashboard Preview**
Below is the static screenshot of the final dashboard:

![Financial Dashboard](/mnt/data/f6cceee1-ac32-4a79-b743-1c08ce8fc717.png)

The dashboard includes:

### ✔ Category Spending (Bar Chart)  
Shows how money is distributed across expense categories.

### ✔ Monthly Line Chart  
Displays income, expenses, and savings over time.

### ✔ Savings Progress (Bar Chart)  
Shows percentage completion toward savings goals.

---

# **7. Conclusion**
This project demonstrates how SQL, Python, and Tableau can be combined to build a complete **financial analytics system**.  
The system successfully performs:

- Expense tracking  
- Income analysis  
- Budget monitoring  
- Savings evaluation  
- Data visualization  

It provides meaningful financial insights both numerically (SQL) and visually (Tableau).

---

# **8. Author**
**Linet Lydia Kagundu**  
Data Science Student | Financial Data Analyst  
Nairobi, Kenya


