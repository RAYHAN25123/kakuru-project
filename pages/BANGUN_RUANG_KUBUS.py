import streamlit as st

st.title("KUBUS")
st.markdown("""
### RUMUS :
- p = Panjang
- l = Lebar
- t = Tinggi
- s = Sisi
- K = Keliling
- V = Volume
- LP = Luas Permukaan
### RUMUS MENCARI KELILING :
- K = 4 x sisi
### RUMUS MENCARI VOLUME :
- V = sisi³
### RUMUS MENCARI LUAS PERMUKAAN :
- LP = 6 × sisi²
""")

st.header("VOLUME, KELILING, & LUAS PERMUKAAN")
sisi = st.number_input("Masukan Panjang Sisi:")
st.header("KELILING")
k = 4 * sisi
st.subheader(k)
st.header("VOLUME")
l = sisi **3
st.subheader(l)
st.subheader("LUAS PERMUKAAN")
v = 6 * sisi **2
st.subheader(v)
