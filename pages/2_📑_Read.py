import sys
from os import environ
import pandas as pd

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
    sys.exit(1)

st.set_page_config(layout="wide")

st.markdown(
    """<h1 style='text-align: center;'>READ TABLE</h1>""",
    unsafe_allow_html=True,
)

st.markdown(
    """<p style='padding:0;margin:0;font-weight:600'>Select the table to view the contents</p>""",
    unsafe_allow_html=True,
)


def show_all(table: str):
    q = "select * from %s" % (table)
    db_cursor.execute(q)
    return db_cursor.fetchall()


table = st.selectbox(
    "table_type",
    (
        "customer",
        "bill",
        "food_item",
        "offers",
        "orders",
        "relatives",
        "reservation",
        "resort",
        "room",
        "room_service",
    ),
    label_visibility="hidden",
    key="customer",
)

try:
    r = show_all(table)
    st.markdown(f"#### Total Entries - `{len(r)}`")

    df = pd.DataFrame(r, columns=[i[0] for i in db_cursor.description])
    df.index = [i + 1 for i in df.index]
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(e)

db.close()
print("DB connection closed")
