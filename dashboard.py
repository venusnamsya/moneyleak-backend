import streamlit as st
import pandas as pd

from database import get_transactions


def get_user_transactions():

    if not st.session_state.user:
        return []

    return get_transactions(
        st.session_state.user["id"]
    )


def dashboard():

    transactions = get_user_transactions()

    df = pd.DataFrame(transactions)

    st.markdown(
        "<div class='section-title'>Dashboard</div>",
        unsafe_allow_html=True
    )

    st.caption(
        "Your personal financial overview."
    )

    if df.empty:

        st.info(
            "You don't have any transactions yet. "
            "Import a statement to get started."
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(
                """<div class="money-card">
                    <div class="metric-label">Total Spending</div>
                    <div class="metric-value">KES 0</div>
                </div>""",
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                """<div class="money-card">
                    <div class="metric-label">Transactions</div>
                    <div class="metric-value">0</div>
                </div>""",
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                """<div class="money-card">
                    <div class="metric-label">Categories</div>
                    <div class="metric-value">0</div>
                </div>""",
                unsafe_allow_html=True
            )

        return

    df["amount"] = pd.to_numeric(
        df["amount"],
        errors="coerce"
    )

    total = df["amount"].sum()

    transaction_count = len(df)

    category_count = df["category"].nunique()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""<div class="money-card">
                <div class="metric-label">Total Spending</div>
                <div class="metric-value">KES {total:,.2f}</div>
            </div>""",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""<div class="money-card">
                <div class="metric-label">Transactions</div>
                <div class="metric-value">{transaction_count}</div>
            </div>""",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""<div class="money-card">
                <div class="metric-label">Categories</div>
                <div class="metric-value">{category_count}</div>
            </div>""",
            unsafe_allow_html=True
        )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Spending by Category")

        category_data = (
            df.groupby("category")["amount"]
            .sum()
            .sort_values(ascending=False)
        )

        st.bar_chart(
            category_data
        )

    with col2:

        st.subheader("Recent Transactions")

        recent = df.head(8)

        for _, row in recent.iterrows():
            st.markdown(
                f"""<div class="transaction-row">
                    <strong>{row['description']}</strong><br>
                    <span class="small-text">{row['date']} · {row['category']}</span><br>
                    <strong class="gold">KES {row['amount']:,.2f}</strong>
                </div>""",
                unsafe_allow_html=True
            )