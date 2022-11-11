import pandas as pd

import streamlit as st
from db import cursor

st.set_page_config(layout="wide")

st.markdown(
    """<p style='text-align: center;font-size:40px;'>Select the table to view the contents</p>""",
    unsafe_allow_html=True,
)


def show_all(table: str):
    q = "select * from %s" % (table)
    cursor.execute(q)
    return cursor.fetchall()


table = st.selectbox(
    "table_type",
    (
        "bill",
        "customer",
        "food_item",
        "offers",
        "orders",
        "relatives",
        "reservation",
        "resort",
        "room",
        "room_service",
    ),
    label_visibility="hidden"
)

try:
    r = show_all(table)
    st.dataframe(pd.DataFrame(r,columns=[i[0] for i in cursor.description]))
except Exception as e:
    st.error(e)
