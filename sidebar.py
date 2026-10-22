import streamlit as st

from settings import logout


def go_to(page):

    st.session_state.page = page
    st.rerun()


def sidebar():

    with st.sidebar:

        st.markdown(
            """
            <div class="sidebar-brand">
                Money<span>Leak</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.caption(
            f"Welcome, {st.session_state.user['name']}"
        )

        st.divider()

        if st.button(
            "📊 Dashboard",
            use_container_width=True
        ):
            go_to("dashboard")

        if st.button(
            "💳 Transactions",
            use_container_width=True
        ):
            go_to("transactions")

        if st.button(
            "📈 Analytics",
            use_container_width=True
        ):
            go_to("analytics")

        if st.button(
            "📥 Import Statement",
            use_container_width=True
        ):
            go_to("import")

        if st.button(
            "⚙️ Settings",
            use_container_width=True
        ):
            go_to("settings")

        st.divider()

        st.caption("Appearance")

        current_theme = st.session_state.theme

        if current_theme == "dark":

            if st.button(
                "☀️ Switch to Light Mode",
                use_container_width=True
            ):

                st.session_state.theme = "light"
                st.rerun()

        else:

            if st.button(
                "🌙 Switch to Dark Mode",
                use_container_width=True
            ):

                st.session_state.theme = "dark"
                st.rerun()

        st.divider()

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            logout()