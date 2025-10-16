import streamlit as st

st.title("BANGUN RUANG BALOK")
st.markdown("""
### RUMUS :
- p = Panjang
- l = Lebar
- t = Tinggi
- L = Luas
- V = Volume
### RUMUS MENCARI LUAS :
- L = 2 x (p x l) + (p x t) + (l x t)
### RUMUS MENCARI VOLUME :
- V = p x l x t
""")

p = st.number_input("Masukan Nilai Panjang")
l = st.number_input("Masukan Nilai Lebar")
t = st.number_input("Masukan Nilai Tinggi")

st.header("LUAS BALOK")
l1 = 2 * (p * l + p * t + l * t)
st.subheader(l1)
st.header("VOLUME BALOK")
v = p * l * t
st.subheader(v)
