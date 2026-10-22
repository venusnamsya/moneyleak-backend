import streamlit as st

from database import create_user, authenticate_user


def go_to(page):
    st.session_state.page = page
    st.rerun()


def landing_page():

    st.markdown(
        """<div class="hero">
            <div class="hero-title">Money<span>Leak</span></div>
            <div class="hero-subtitle">
                Understand where your money goes.
                Turn transaction data into financial intelligence.
            </div>
        </div>""",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """<div class="money-card">
                <h3>📊 See the pattern</h3>
                <p class="small-text">Turn transaction statements into clear spending insights.</p>
            </div>""",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """<div class="money-card">
                <h3>🔎 Find the leaks</h3>
                <p class="small-text">Identify where your money is disappearing across categories.</p>
            </div>""",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """<div class="money-card">
                <h3>💡 Understand your money</h3>
                <p class="small-text">Build a clearer picture of your spending habits.</p>
            </div>""",
            unsafe_allow_html=True
        )

    st.write("")

    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        if st.button(
            "Get Started",
            type="primary",
            use_container_width=True
        ):
            go_to("register")

    st.divider()

    st.markdown(
        """<p style="text-align:center;">MoneyLeak · Personal Finance Intelligence</p>""",
        unsafe_allow_html=True
    )