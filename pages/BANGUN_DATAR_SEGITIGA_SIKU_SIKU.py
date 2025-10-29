import streamlit as st
import math

st.title("SEGITIGA SIKU-SIKU")
st.markdown("""
### RUMUS :
- s = Sisi
- a = Alas
- t = Tinggi
- K = Keliling
- L = Luas
""")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXlzctGkQxXU1ITdLE5sxX1Pl3EbnVOGDNpw&s", caption="Gambar ini diambil dari internet", use_container_width=True)
st.markdown("""
### RUMUS MENCARI KELILING :
- K = 2 x sisi + alas
### RUMUS MENCARI LUAS :
- L = 1/2 x alas x tinggi
### RUMUS MENCARI TINGGI (Jika tidak ada tinggi) :
- t = √sisi2 - (a/2)2
""")
