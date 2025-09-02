import streamlit as st

st.title("PERSEGI")
st.subheader("Rumus :")
st.markdown("""
- K = Keliling
- L = Luas
""")
sisi = st.number_input("Masukan Panjang Sisi:")
st.header("KELILING")
keliling = sisi**2
st.subheader(keliling)

st.header("LUAS")
luas = 4 * sisi
st.subheader(luas)

