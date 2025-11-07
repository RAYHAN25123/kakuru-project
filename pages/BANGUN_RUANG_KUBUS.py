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

st.header("VOLUME & LUAS PERMUKAAN")
sisi = st.number_input("Masukan Panjang Sisi:")
st.subheader("Luas Permukaan")
v = 6 * sisi **2
st.subheader(v)
st.header("Volume")
l = sisi **3
st.subheader(l)
