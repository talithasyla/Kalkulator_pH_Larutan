import streamlit as st
import math

st.title('Kalkulator pH Larutan Basa')

konsentrasi = st.number_input('Masukkan Konsentrasi',)
st.write("Konsentrasi = ", konsentrasi)
valensi = st.number_input('Masukkan Valensi', 0)
st.write("a = ", valensi)
hitung = st.button('Hitung pH')

if hitung:
    basa = konsentrasi * valensi
    st.write('[H+] = ', basa)
    log = math.log10(basa)
    pH = log * -1
    st.write('pH = ', pH)
    st.success(f'pH Basa adalah {pH:.2f}')
