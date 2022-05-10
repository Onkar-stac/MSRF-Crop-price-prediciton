import streamlit as st
from predict_page import predict

with open('style.css') as f :
    st.markdown(f'<style> {f.read()} </style>', unsafe_allow_html = True)
predict()