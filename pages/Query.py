import streamlit as st
from streamlit_lottie import st_lottie

from utils.utils import load_lottieurl


def handle_query_submit():
    pass


st.set_page_config(layout="wide", initial_sidebar_state="expanded")

lottie_coding = load_lottieurl(
    "https://assets10.lottiefiles.com/packages/lf20_KJzm1mEy8M.json"
)

st_lottie(lottie_coding, height=85, key="coffee logo")

st.markdown(
    """<p style='text-align: center;font-size:40px;'>Execute <span class="highlight">SQL</span> Queries on the Database</p>""",
    unsafe_allow_html=True,
)

with st.form(key="query_input"):
    query = st.text_area("\t", placeholder="SELECT * FROM customer", height=20)
    submit_btn = st.form_submit_button("Execute", on_click=handle_query_submit)
    if not submit_btn:
        st.markdown(
            """
        Example:
        ```sql
        SELECT * FROM customer LIMIT 5;
        ```
        """
        )
    else:
        st.write("Executing...")
