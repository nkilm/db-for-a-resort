import streamlit as st
from streamlit_lottie import st_lottie

from utils.utils import load_lottieurl

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

lottie_coding = load_lottieurl(
    "https://assets10.lottiefiles.com/packages/lf20_KJzm1mEy8M.json"
)

st_lottie(lottie_coding, height=85, key="coffee logo")

st.title("Execute `SQL` Queries on the Database")

query = st.text_area("", placeholder="SELECT * FROM customer", height=20)

st.markdown(
    """
Example:
```sql
SELECT * FROM customer LIMIT 5;
```
"""
)
