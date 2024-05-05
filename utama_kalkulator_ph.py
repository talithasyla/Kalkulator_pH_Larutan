import streamlit as st
st.title("Kalkulator pH Larutan")

from st_pages import show_pages_from_config

if st.pages("Kalkulator pH Larutan Asam"):
  st.show_page("https://kalkulatorphlarutan-c3ewuknkoryyvwbvxuu4g4.streamlit.app/", ":home:")
