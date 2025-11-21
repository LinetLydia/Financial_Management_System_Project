import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_transactions():
    # Load the CSV that holds all raw transactions
    return pd.read_csv("C:/Users/hp/projects/Financial_Management_System/financial_app/transactions_full.csv")

# Helper to guess common column names safely
def pick_column(cols, candidates):
    for c in candidates:
        if c in cols:
            return c
    # try fuzzy match (e.g. "transaction_date", "date")
    lower = {c.lower(): c for c in cols}
    for cand in candidates:
        for col_lower, original in lower.items():
            if cand in col_lower:
                return original
    return None


def main():
    st.title("📂 Transactions Explorer")
    st.markdown(
        "Drill down into individual transactions with filters, tables and charts."
    )

    # Load data
    df = load_transactions()
    cols = df.columns

    st.caption(f"Loaded **{len(df):,}** transactions with columns: `{list(cols)}`")

    # Try to identify key columns
    user_col = pick_column(cols, ["user_id"])
    date_col = pick_column(cols, ["transaction_date", "date"])
    cat_col = pick_column(cols, ["category_name", "category"])
    type_col = pick_column(cols, ["transaction_type", "type"])
    amount_col = pick_column(cols, ["amount", "transaction_amount", "value"])

    # Sidebar filters
    st.sidebar.header("Filters")

    # User filter (if column exists)
    if user_col:
        users = sorted(df[user_col].unique())
        selected_user = st.sidebar.selectbox("Select User ID", users)
        df = df[df[user_col] == selected_user]

    # Date filter (if column exists)
    if date_col:
        # Convert to datetime once
        df[date_col] = pd.to_datetime(df[date_col])

        min_date = df[date_col].min()
        max_date = df[date_col].max()

        start_date, end_date = st.sidebar.date_input(
            "Date range",
            value=[min_date, max_date],
            min_value=min_date,
            max_value=max_date,
        )

        # Make sure we got a range
        if isinstance(start_date, pd.Timestamp):
            start_date = start_date.date()
        if isinstance(end_date, pd.Timestamp):
            end_date = end_date.date()

        df = df[
            (df[date_col].dt.date >= start_date)
            & (df[date_col].dt.date <= end_date)
        ]

    # Category filter (if column exists)
    if cat_col:
        categories = sorted(df[cat_col].unique())
        chosen_cats = st.sidebar.multiselect(
            "Filter by category", options=categories, default=categories
        )
        df = df[df[cat_col].isin(chosen_cats)]

    # Transaction type filter (Income / Expense) if available
    if type_col:
        types = sorted(df[type_col].unique())
        chosen_types = st.sidebar.multiselect(
            "Filter by type", options=types, default=types
        )
        df = df[df[type_col].isin(chosen_types)]

    st.markdown("### 🔍 Filtered Transactions")

    st.caption(f"Showing **{len(df):,}** matching rows.")
    st.dataframe(df, use_container_width=True)

    # Summary + charts only if we have amount column
    if amount_col:
        st.markdown("### 📊 Summary Charts")

        col1, col2 = st.columns(2)

        # Spending by category
        with col1:
            if cat_col:
                cat_summary = (
                    df.groupby(cat_col)[amount_col]
                    .sum()
                    .reset_index()
                    .sort_values(amount_col, ascending=False)
                )
                fig_cat = px.bar(
                    cat_summary,
                    x=amount_col,
                    y=cat_col,
                    orientation="h",
                    title="Total Amount by Category",
                )
                st.plotly_chart(fig_cat, use_container_width=True)
            else:
                st.info("No category column found – cannot plot category spending.")

        # Time series
        with col2:
            if date_col:
                time_summary = (
                    df.groupby(date_col)[amount_col]
                    .sum()
                    .reset_index()
                    .sort_values(date_col)
                )
                fig_time = px.line(
                    time_summary,
                    x=date_col,
                    y=amount_col,
                    markers=True,
                    title="Amount Over Time",
                )
                st.plotly_chart(fig_time, use_container_width=True)
            else:
                st.info("No date column found – cannot plot time series.")
    else:
        st.warning(
            "No amount-like column found (`amount`, `transaction_amount`, or `value`). "
            "Charts are disabled but the raw table is available above."
        )


if __name__ == "__main__":
    main()
