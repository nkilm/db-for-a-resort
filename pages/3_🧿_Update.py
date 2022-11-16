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
    st.error(e)

st.markdown(
    """<h1 style='text-align: center;'>UPDATION</h1>""",
    unsafe_allow_html=True,
)


st.subheader("Select/Enter the Customer ID")

db_cursor.execute("select cid from customer")

cid = st.selectbox(
    "cid",
    [int(i[0]) for i in db_cursor.fetchall()],
    label_visibility="hidden",
)

st.write("---")

try:
    db_cursor.execute(f"select * from customer where cid={cid}")
    cid, fname, minit, lname, addr, mail, pno, waiter_id = db_cursor.fetchone()

    with st.form(key="update_form_cust"):
        st.subheader("Update Form")

        col1, col2, col3 = st.columns(3)
        with col1:
            fname = st.text_input(
                "fname",
                fname,
                placeholder="Enter your First Name",
                label_visibility="hidden",
            )
        with col2:
            minit = st.text_input(
                "minit",
                minit,
                placeholder="Middle Name initials",
                label_visibility="hidden",
            )
        with col3:
            lname = st.text_input(
                "lname",
                lname,
                placeholder="Enter your Last Name",
                label_visibility="hidden",
            )

        address = st.text_input(
            "address",
            addr,
            placeholder="Enter your address",
            label_visibility="hidden",
        )

        col1, col2 = st.columns(2)
        with col1:
            email = st.text_input(
                "email",
                mail,
                placeholder="Enter your Email",
                label_visibility="hidden",
                type="default",
            )
        with col2:
            pno = st.text_input(
                "pno",
                pno,
                placeholder="Enter your Mobile number",
                label_visibility="hidden",
            )

        update_btn = st.form_submit_button("UPDATE")
        if update_btn:
            q = f"""
            update customer set fname="{fname}", minit="{minit}", lname="{lname}", address="{address}", email="{mail}", contactNo="{pno}", waiter_id="{waiter_id}" where cid={cid}
            """
            db_cursor.execute(q)
            db.commit()
            st.success(f"Info updated successfully for Customer with {cid}")

except Exception as e:
    st.error(e)


db.close()
print("DB connection closed")
