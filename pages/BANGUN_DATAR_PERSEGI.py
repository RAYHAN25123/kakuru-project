import streamlit as st

st.title("PERSEGI")
st.markdown("""
### RUMUS :
- S = Sisi
- K = Keliling
- L = Luas
### RUMUS MENCARI KELILING :
- K = 4 x Sisi
### RUMUS MENCARI LUAS :
- L = Sisi √2
""")
sisi = st.number_input("Masukan Panjang Sisi:")
st.header("KELILING")
keliling = 4 * sisi
st.subheader(keliling)

st.header("LUAS")
luas = sisi**2
st.subheader(luas)


