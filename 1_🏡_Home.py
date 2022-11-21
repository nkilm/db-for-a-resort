import streamlit as st
from streamlit_lottie import st_lottie

from utils.utils import load_lottieurl

st.set_page_config(
    page_title="Mohite Resorts Pvt.Ltd",
    page_icon="./styles/favicon.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles/style.css")

lottie_coding = load_lottieurl(
    "https://assets10.lottiefiles.com/private_files/lf30_WjupkW.json"
)

st_lottie(lottie_coding, height=200, key="main logo")

st.markdown(
    "<h1 style='text-align: center;'><span style='border-bottom: 2px solid red'>Mohite Resorts Pvt.Ltd</span></h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center;font-size:20px'>Experience something new every moment!</p>",
    unsafe_allow_html=True,
)

st.write("---")
st.markdown(
    """<p style='text-align: center;font-size:25px'>Visit <a href="http://localhost:8501/Info">/Info</a> to get the <span class="highlight">Schema</span> related information</p>""",
    unsafe_allow_html=True,
)
