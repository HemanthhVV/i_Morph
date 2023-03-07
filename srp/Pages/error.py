import streamlit as st
from streamlit_lottie import st_lottie
import requests

def loader(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return(r.json())
lott=loader("https://assets10.lottiefiles.com/packages/lf20_AYcZiy.json")
def success():
    st.markdown("<h1 style='text-align:center;colour:white;'>Error 404</h1>",unsafe_allow_html=True)
    st.write("##")
success()

col1, col2, col3 = st.columns(3)

with col1:
    pass
with col3:
    pass
with col2 :
    st_lottie(lott,height=180,width=200,key="img")
    st.write("##")
    st.write("<ul style='text-align:;colour:white;'>◍Try to use formal resumes</ul>",unsafe_allow_html=True)
    st.write("<ul style='text-align:;colour:white;'>◍Check the connectivity</ul>",unsafe_allow_html=True)


