import sys
import pandas as pd
from os import environ

import mysql.connector
import streamlit as st
from utils.utils import load_lottieurl
from streamlit_lottie import st_lottie
from dotenv import load_dotenv

load_dotenv()

try:
    db = mysql.connector.connect(
        host=environ.get("HOST"),
        user=environ.get("DB_USER"),
        password=environ.get("DB_PASSWORD"),
        database=environ.get("DB"),
    )

    if db.is_connected():
        print("DB Connected")
    else:
        print("DB Connection not successful")
        sys.exit(1)

    db_cursor = db.cursor()

except mysql.connector.Error as e:
    print(e)
    print("Error Code:", e.errno)
    print("SQLSTATE", e.sqlstate)
    print("Message", e.msg)
    sys.exit(1)

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

try:
    lottie_coding = load_lottieurl(
        # "https://assets10.lottiefiles.com/packages/lf20_KJzm1mEy8M.json"
        # "https://assets1.lottiefiles.com/packages/lf20_8Trbef.json"
        "https://assets7.lottiefiles.com/packages/lf20_vtiwaamr.json"
    )
    st_lottie(lottie_coding, height=100, key="coffee logo")
except Exception as e:
    st.error(e)

st.markdown(
    """<p style='text-align: center;font-size:40px;'>Execute <span class="highlight">SQL</span> Queries on the Database</p>""",
    unsafe_allow_html=True,
)

with st.form(key="query_input"):
    query = st.text_area("\t", placeholder="SELECT * FROM customer", height=20)
    submit_btn = st.form_submit_button("Execute")
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
        try:
            print(query)
            db_cursor.execute(query)
            result = db_cursor.fetchall()
            _,col_m,_ = st.columns([2.5,10,1])
            
            with col_m:
                st.markdown(f"#### Total Items - `{len(result)}`")
                df = pd.DataFrame(result, columns=[i[0] for i in db_cursor.description])
                df.index = [i + 1 for i in df.index]
                st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error(e)

db.close()
print("DB connection closed")
