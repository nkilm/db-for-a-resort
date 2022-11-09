import streamlit as st
from streamlit_option_menu import option_menu


def handle_insert():
    pass


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

        st.text_input(
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
            st.date_input("check-in", label_visibility="hidden")
        with col2:
            st.write("Check-Out")
            st.date_input("check-out", label_visibility="hidden")

        st.write("#")
        submit_btn = st.form_submit_button("INSERT", on_click=handle_insert)
        if submit_btn:
            st.success("Insert Query submitted!")
else:
    with st.form(key="insert_form_resort", clear_on_submit=True):
        st.text_input(
            "resort_name",
            placeholder="Enter the Resort name",
            label_visibility="hidden",
        )

        col1, col2 = st.columns(2)
        with col1:
            st.number_input("Room Number")
        with col2:
            st.number_input("Floor")

        room_type = st.selectbox("room_type", ("Single", "Suite", "Double"))

        price = st.text_input("Price", placeholder="Enter the price")

        st.write("#")
        submit_btn = st.form_submit_button("INSERT", on_click=handle_insert)
