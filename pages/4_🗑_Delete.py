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

        db_cursor.execute("select cid from customer")

        cid = st.selectbox(
            "cid",
            [int(i[0]) for i in db_cursor.fetchall()],
            label_visibility="hidden",
        )
        db_cursor.execute(f"select * from customer where cid={cid}")
        info = db_cursor.fetchone()

        c_btn = st.form_submit_button("DELETE")

        if info is None:
            st.error(f"Customer with customer ID {cid} not found")
        else:
            if c_btn:
                try:
                    q = "delete from customer where cid=%d" % cid
                    db_cursor.execute(q)
                    db.commit()
                    st.success(f"Customer {cid} deleted successfully")
                    st.write("---")
                    st.subheader("Deleted Information")
                    df = pd.DataFrame(
                        [info], columns=[i[0] for i in db_cursor.description]
                    )
                    df.index = [i + 1 for i in df.index]
                    st.dataframe(df, use_container_width=True)

                except Exception as e:
                    st.error(e)
else:
    with st.form(key="delete_form_resort"):
        st.subheader("Enter the Resort ID")

        db_cursor.execute("select resort_id from resort")

        resort_id = st.selectbox(
            "resort_id",
            [int(i[0]) for i in db_cursor.fetchall()],
            label_visibility="hidden",
        )
        db_cursor.execute(f"select * from resort where resort_id={resort_id}")
        info = db_cursor.fetchone()

        c_btn = st.form_submit_button("DELETE")

        if info is None:
            st.error(f"Resort with resort ID {resort_id} not found")
        else:
            if c_btn:
                try:

                    q = "delete from resort where resort_id=%d" % resort_id
                    db_cursor.execute(q)
                    st.success(f"Resort {resort_id} deleted successfully")
                    st.write("---")
                    st.subheader("Deleted Information")
                    df = pd.DataFrame(
                        [info],columns=["resort_id","resort_name","address","rating","price_per_day"]
                    )
                    df.index = [i + 1 for i in df.index]
                    st.dataframe(df, use_container_width=True)
                    db.commit()
                except Exception as e:
                    st.error(e)

                

db.close()
print("DB connection closed")
