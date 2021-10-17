# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 22:47:51 2021

@author: acer
"""

import streamlit as st

st.write("""
# Testing Streamlit Web app
##### Finding Squared Number of User Interface with slider
         
    Hello...! This is a test of very first my streamlit web app
    မင်္ဂလာပါ ပထမဆုံး ဝက်ဘ်ဆိုဒ် စမ်းသပ်ခြင်းပါ...။
         """)
# ျ  = s
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
