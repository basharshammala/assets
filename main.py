import streamlit as st

st.set_page_config(page_title='assets', layout='wide')

home_page = st.Page('home.py', title='Home', default=True)

nav = st.navigation([home_page], position='hidden')
nav.run()





















