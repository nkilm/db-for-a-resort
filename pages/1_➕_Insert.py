import sys
from os import environ
from random import randint
from datetime import date

import mysql.connector
import streamlit as st
from dotenv import load_dotenv
from streamlit_option_menu import option_menu

load_dotenv()
st.set_page_config(layout="centered")

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
    """<p style='text-align: center;font-size:40px;'>Insert into Database</p>""",
    unsafe_allow_html=True,
)

option = option_menu(
    menu_title=None,
    options=["Customer", "Resort"],
    orientation="horizontal",
    icons=["person", "house"],
)

if option == "Customer":
    with st.form(key="insert_form_cust"):
        col1, col2, col3 = st.columns(3)
        with col1:
            fname = st.text_input(
                "fname", placeholder="Enter your First Name", label_visibility="hidden"
            )
        with col2:
            minit = st.text_input(
                "minit", placeholder="Middle Name initials", label_visibility="hidden"
            )
        with col3:
            lname = st.text_input(
                "lname", placeholder="Enter your Last Name", label_visibility="hidden"
            )

        address = st.text_input(
            "address", placeholder="Enter your address", label_visibility="hidden"
        )

        col1, col2 = st.columns(2)
        with col1:
            email = st.text_input(
                "email",
                placeholder="Enter your Email",
                label_visibility="hidden",
                type="default",
            )
        with col2:
            pno = st.text_input(
                "pno", placeholder="Enter your Mobile number", label_visibility="hidden"
            )

        st.markdown(
            """<h4 style='text-align: center;'>Resort Info</h4>""",
            unsafe_allow_html=True,
        )

        resort_id = st.text_input(
            "resort_id", placeholder="Enter the resort id", label_visibility="hidden"
        )

        col1, col2 = st.columns(2)
        with col1:
            st.write("Check-In")
            check_in = st.date_input("check-in", label_visibility="hidden")
        with col2:
            st.write("Check-Out")
            check_out = st.date_input("check-out", label_visibility="hidden")

        st.write("#")
        submit_btn = st.form_submit_button("INSERT")
        if submit_btn:
            try:
                cid = randint(1000, 9999)
                q = (
                    """insert into customer values (%d,"%s","%s","%s","%s","%s",%s,NULL)"""
                    % (cid, fname, minit, lname, address, email, pno)
                )
                db_cursor.execute(q)
                print(q)
                db_cursor.execute(
                    f"select price_per_day from resort where resort_id={resort_id}"
                )

                price_per_day = int(db_cursor.fetchone()[0])
                print(price_per_day)
                amount = (check_out - check_in).days * price_per_day
                print(amount)

                q = """insert into reservation values(%d,%d,"%s","%s",%f)""" % (
                    cid,
                    int(resort_id),
                    check_in,
                    check_out,
                    amount,
                )
                print(q)
                db_cursor.execute(q)

                db.commit()

                st.success("Inserted Successfully")
                db.close()
            except Exception as e:
                st.error(e)

else:
    with st.form(key="insert_form_resort"):
        resort_name = st.text_input(
            "resort_name",
            placeholder="Enter the Resort name",
            label_visibility="hidden",
        )

        resort_address = st.text_input(
            "resort_address",
            placeholder="Enter the Resort Address",
            label_visibility="hidden",
        )

        price = st.text_input(
            "Price", placeholder="Enter the price", label_visibility="hidden"
        )

        ratings = st.slider("Enter the Ratings", 1.0, 5.0, value=4.5)

        st.write("#")

        submit_btn = st.form_submit_button("INSERT")
        if submit_btn:
            try:

                resort_id = randint(1000, 9999)
                q = """insert into resort values (%d,"%s","%s","%s","%s")""" % (
                    resort_id,
                    resort_name,
                    resort_address,
                    ratings,
                    price,
                )
                print(q)
                db_cursor.execute(q)
                db.commit()

                st.success("Inserted Successfully")
            except Exception as e:
                st.error(e)

db.close()
print("DB connection closed...")
