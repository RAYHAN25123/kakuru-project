import streamlit as st
import math

st.title("SEGITIGA SAMA KAKI")
image_url = "https://images.unsplash.com/photo-1548247738-4e3a9d201a07"
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

s = st.number_input("Masukan Sisi", key="sisi 1")
a = st.number_input("Masukan Alas", key="alas 1")
st.header("KELILING")
k = 2 * s + a
st.subheader(k)

a1 = st.number_input("Masukan Nilai Alas", key="alas 2")
t = st.number_input("Masukan Nilai Tinggi", key="tinggi 1")
st.header("LUAS")
l = 1 / 2 * a1 * t
st.subheader(l)

st.subheader("Rumus mencari Tinggi (Jika tidak ada)")
s1 = st.number_input("Masukan Sisi", key="sisi 2")
a2 = st.number_input("Masukan Alas", key="alas 3")
t1 = s1 **2
t2 = (a2 /2) **2
t3 = t1 - t2
t4 = math.sqrt(t3)
st.header("Tinggi")
st.subheader(t4)
