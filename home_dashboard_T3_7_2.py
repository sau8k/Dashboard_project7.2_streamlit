import streamlit as st
import plotly.express as px
import numpy as np 
import time

with st.sidebar:
    st.button("Home"):
        st.switch_page("home_dashboard_T3_7_2.py")
    st.button("Details"):
        st.switch_page("details_dashboard_T3_7_2.py")


