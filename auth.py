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


def register_page():

    st.markdown(
        """<div class="hero-title" style="font-size:42px;text-align:center;">Create your MoneyLeak account</div>""",
        unsafe_allow_html=True
    )

    st.markdown(
        """<p style="text-align:center;">Start understanding your money.</p>""",
        unsafe_allow_html=True
    )

    with st.form("register_form"):

        name = st.text_input("Full name")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm password",
            type="password"
        )

        submitted = st.form_submit_button(
            "Create account",
            type="primary",
            use_container_width=True
        )

        if submitted:

            if not name or not email or not password:

                st.error(
                    "Please complete all fields."
                )

            elif password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

            elif len(password) < 6:

                st.error(
                    "Password must be at least 6 characters."
                )

            else:

                user_id = create_user(
                    name,
                    email,
                    password
                )

                if user_id:

                    st.success(
                        "Account created successfully."
                    )

                    st.session_state.page = "login"

                    st.rerun()

                else:

                    st.error(
                        "An account with that email already exists."
                    )

    st.write("")

    if st.button(
        "Already have an account? Login"
    ):
        go_to("login")

    if st.button("← Back"):
        go_to("landing")


def login_page():

    st.markdown(
        """<div class="hero-title" style="font-size:42px;text-align:center;">Welcome <span>back</span></div>""",
        unsafe_allow_html=True
    )

    st.markdown(
        """<p style="text-align:center;">Sign in to your MoneyLeak dashboard.</p>""",
        unsafe_allow_html=True
    )

    with st.form("login_form"):

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        submitted = st.form_submit_button(
            "Login",
            type="primary",
            use_container_width=True
        )

        if submitted:

            user = authenticate_user(
                email,
                password
            )

            if user:

                st.session_state.user = user
                st.session_state.page = "dashboard"

                st.rerun()

            else:

                st.error(
                    "Invalid email or password."
                )

    st.write("")

    if st.button("Create an account"):
        go_to("register")

    if st.button("← Back"):
        go_to("landing")