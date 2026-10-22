import streamlit as st
import pandas as pd

from database import get_transactions


def analytics_page():

    st.markdown(
        "<div class='section-title'>Analytics</div>",
        unsafe_allow_html=True
    )

    transactions = get_transactions(
        st.session_state.user["id"]
    )

    if not transactions:

        st.info(
            "Import transactions to see financial analytics."
        )

        return

    df = pd.DataFrame(transactions)

    # Make sure amounts are numbers
    df["amount"] = pd.to_numeric(
        df["amount"],
        errors="coerce"
    )

    # Convert dates
    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    # Remove invalid amounts
    df = df.dropna(
        subset=["amount"]
    )

    if df.empty:

        st.info(
            "There is not enough transaction data to display analytics."
        )

        return

    # ========================================================
    # SUMMARY
    # ========================================================

    total_spending = df["amount"].sum()

    average_transaction = df["amount"].mean()

    transaction_count = len(df)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""<div class="money-card">
                <div class="metric-label">Total Spending</div>
                <div class="metric-value">KES {total_spending:,.2f}</div>
            </div>""", 
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""<div class="money-card">
                <div class="metric-label">Average Transaction</div>
                <div class="metric-value">KES {average_transaction:,.2f}</div>
            </div>""", 
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""<div class="money-card">
                <div class="metric-label">Transactions</div>
                <div class="metric-value">{transaction_count}</div>
            </div>""", 
            unsafe_allow_html=True
        )

    st.write("")

    # ========================================================
    # SPENDING BY CATEGORY
    # ========================================================

    st.subheader("Spending by Category")

    category_data = (
        df.groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    if not category_data.empty:

        st.bar_chart(
            category_data
        )

    # ========================================================
    # SPENDING OVER TIME
    # ========================================================

    st.subheader("Spending Over Time")

    dated_transactions = df.dropna(
        subset=["date"]
    )

    if not dated_transactions.empty:

        monthly = (
            dated_transactions
            .set_index("date")
            .resample("ME")["amount"]
            .sum()
        )

        if not monthly.empty:

            st.line_chart(
                monthly
            )

        else:

            st.info(
                "Not enough dated transactions to show a timeline."
            )

    else:

        st.info(
            "No valid dates available for the spending timeline."
        )

    # ========================================================
    # TOP SPENDING AREAS
    # ========================================================

    st.subheader("Top Spending Areas")

    top_categories = category_data.head(5)

    if top_categories.empty:

        st.info(
            "No category data available."
        )

        return

    for category, amount in top_categories.items():
        st.markdown(
            f"""<div class="money-card" style="margin-bottom:10px;">
                <strong>{category}</strong>
                <div class="metric-value" style="font-size:22px;">KES {amount:,.2f}</div>
            </div>""", 
            unsafe_allow_html=True
        )