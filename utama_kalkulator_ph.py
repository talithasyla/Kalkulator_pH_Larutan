import streamlit as st

st.title("KALKULATOR PERHITUNGAN pH")

st.write("Pilih opsi yang akan dihitung!")
if st.button("Larutan Asam"):
    st.switch_page("https://kalkulatorphlarutan-c3ewuknkoryyvwbvxuu4g4.streamlit.app/")
if st.button("Larutan Basa"):
    st.switch_page("pages/page_1.py")
if st.button("Massa dan Volume Larutan Asam"):
    st.switch_page("pages/page_2.py")
if st.button("Massa dan Volume Larutan Basa"):
    st.switch_page("pages/page_3.py")