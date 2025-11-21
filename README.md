# Financial Management System (SQL + Python + Tableau)

This project demonstrates the end-to-end development of a Financial Management System (FMS) using SQLite (SQL), Python, and Tableau Public.  
The system stores income, expenses, budgets, and savings goals and visualizes key financial insights through interactive dashboards.

---

## 1. Project Overview

The Financial Management System was designed to:

- Store and organize personal financial transactions  
- Track income and expenses across multiple categories  
- Monitor monthly budgets and detect overspending  
- Analyze financial behavior and trends over time  
- Evaluate progress toward savings goals  
- Generate visual insights through dashboards (Tableau)

This project showcases skills in **database design**, **SQL querying**, **Python-based data engineering**, and **Tableau dashboard development**.

---

## 2. Technologies Used

- **Python** (sqlite3, pandas, datetime, random)  
- **SQLite Database**  
- **Tableau Public** (interactive dashboards)  
- **Jupyter Notebook**  
- **Markdown** for project documentation  

---

## 3. Database Schema (ER Diagram)

The system uses six core tables:

1. **Users**  
2. **Accounts**  
3. **Categories**  
4. **Transactions**  
5. **Budgets**  
6. **SavingsGoals**  

These tables include primary keys, foreign keys, constraints, and relationships supporting a fully normalized structure.

*ER Diagram (to be added)* — can be generated using dbdiagram.io, DrawSQL, or Lucidchart.

---

## 4. SQL & Python Pipeline

### 4.1 Schema Creation (Python + SQLite)

All tables were created programmatically using Python’s `sqlite3` package.

**Example — Users Table:**
```sql
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

### 4.2 Sample Data Generation & Insertion

Python scripts were used to generate **realistic Kenyan-style financial data**, including:

- Users  
- Accounts  
- Categories  
- Transactions (3000+ records)  
- Budgets (monthly per category)  
- Savings Goals  

Below is an example of inserting sample categories into the database:

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



