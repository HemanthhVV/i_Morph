import streamlit as st
from streamlit_lottie import st_lottie
import requests
from streamlit_extras.switch_page_button import switch_page
# def dan():
def loader(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return(r.json())
lott=loader("https://assets5.lottiefiles.com/packages/lf20_lFDBUz2hls.json")

def success():
    st.markdown("<h1 style='text-align:center;colour:white;'>Sorry Pal!</h1>",unsafe_allow_html=True)
    # st.write("##")
success()

col1, col2, col3 = st.columns(3)

with col1:
    pass
with col3:
    pass
with col2 :
    st_lottie(lott,height=150,width=200,key="img")

st.write("<h5 style='text-align:center;colour:white;'>It's not over!</h5>",unsafe_allow_html=True)
st.write("<h6 style='text-align:center;colour:white;'>Keep Learn and improve your skills!</h6>",unsafe_allow_html=True)
st.write("##")
st.write("##")
st.write("##")

c1,c3=st.columns(2)

with c1:
    main=st.button("<<Go Back")
    if(main):
        switch_page("u5")

with c3:
    st.write("<sub style='text-align:right;colour:white;'>*All this result is depend on your resume,it may be vary</sub>",unsafe_allow_html=True)


























