import sys
import pandas as pd
from os import environ

import mysql.connector
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

try:
    db = mysql.connector.connect(
        host=environ.get("HOST"),
        user=environ.get("DB_USER"),
        password=environ.get("DB_PASSWORD"),
        database=environ.get("DB"),
    )

    db_cursor = db.cursor()

except mysql.connector.Error as e:
    print(e)
    print("Error Code:", e.errno)
    print("SQLSTATE", e.sqlstate)
    print("Message", e.msg)
    st.error(e)

st.markdown(
    """<h1 style='text-align: center;'>DELETION</h1>""",
    unsafe_allow_html=True,
)

table = st.selectbox("delete_table", ("Customer", "Resort"), label_visibility="hidden")
if table == "Customer":
    with st.form(key="delete_form_cust"):
        st.subheader("Enter the Customer ID")
        cid = st.number_input(
            "cid", min_value=1000, max_value=9999, label_visibility="hidden"
        )

        c_btn = st.form_submit_button("DELETE")

        if c_btn:
            try:

                q = "delete from customer where cid=%d" % cid
                db_cursor.execute(q)
                db.commit()
                st.success(f"Customer {cid} deleted successfully")
            except Exception as e:
                st.error(e)
else:
    with st.form(key="delete_form_resort"):
        st.subheader("Enter the Resort ID")
        resort_id = st.number_input(
            "resort_id", min_value=1000, max_value=9999, label_visibility="hidden"
        )

        c_btn = st.form_submit_button("DELETE")

        if c_btn:
            try:
                q = f"delete from resort where resort_id={resort_id}"
                db_cursor.execute(q)
                db.commit()
                st.success(f"Resort {resort_id} deleted successfully")

            except Exception as e:
                st.error(e)

db.close()
print("DB connection closed")
