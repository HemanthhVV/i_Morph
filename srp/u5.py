#!/usr/bin/env python
# coding: utf-8
#converted ipynb to py in jupyter
# In[1]:


import streamlit as st
from Model_5 import fun
from streamlit_extras.switch_page_button import switch_page


# In[2]:


st.markdown("<h1 style='text-align:center;colour:white;'>Simple Resume Prediction</h1>",unsafe_allow_html=True)
st.write(" ---")
st.write("<p style='text-align:center;colour:white;'>It extracts the entities from your resume and predicts the chances of your placement</p>",unsafe_allow_html=True)
st.text("")
uploaded_file=st.file_uploader("Choose Your File[PDF]:",type="pdf")
st.text("")
if uploaded_file is not None:
    df=fun(uploaded_file)
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
    border: 1px solid white;
    height:35px;
}
div.stButton > button:hover {
    background-color: #008000;
    color:#ffffff;
    }
</style>""", unsafe_allow_html=True)

col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.button('Upload')
    if(center_button):
        if(int(df)==0):
            switch_page('danger')
        if(int(df)==1):
            switch_page('success')
        st.exception(switch_page('error'))






