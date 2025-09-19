import streamlit as st

st.title("SEGITIGA SAMA KAKI")
st.markdown("""
### RUMUS :
- s = Sisi
- a = Alas
- t = Tinggi
- K = Keliling
- L = Luas
### RUMUS MENCARI KELILING :
- K = 2 x sisi + alas
### RUMUS MENCARI LUAS :
- L = 1/2 x alas x tinggi
### RUMUS MENCARI TINGGI (Jika tidak ada tinggi) :
- t = √sisi2 - (a/2)2
""")

s1 = st.number_input("Masukan Panjang Sisi 1:")
s2 = st.number_input("Masukan Panjang Sisi 2:")
s3 = st.number_input("Masukan Panjang Sisi 3:")
st.header("KELILING")
k = s1 + s2 + s3
st.subheader(k)

a = st.number_input("Masukan Nilai Alas:")
t = st.number_input("Masukan Nilai Tinggi:")
st.header("LUAS")
l = 1 / 2 * a * t
st.subheader(l)
