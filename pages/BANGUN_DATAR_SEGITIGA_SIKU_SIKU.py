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

st.markdown("""
### RUMUS MENCARI KELILING :
- K = 2 x sisi + alas
### RUMUS MENCARI LUAS :
- L = 1/2 x alas x tinggi
### RUMUS MENCARI TINGGI (Jika tidak ada tinggi) :
- t = √sisi2 - (a/2)2
""")

st.header("KELILING")
s = st.number_input("Masukan Nilai Sisi:", key="sisi 1")
a = st.number_input("Masukan Nilai Alas:", key="alas 1")
st.header("Keliling")
k = 2 * s + a
st.subheader(k)

st.header("LUAS")
a1 = st.number_input("Masukan Nilai Alas:", key="alas 2")
t = st.number_input("Masukan Nilai Tinggi:", key="tinggi 1")
st.header("Luas")
l = 1 / 2 * a1 * t
st.subheader(l)

st.header("TINGGI")
s1 = st.number_input("Masukan Nilai Sisi:", key="sisi 2")
a2 = st.number_input("Masukan Nilai Alas:", key="alas 3")
t1 = s1 **2
t2 = (a2 /2) **2
t3 = t1 - t2
t4 = math.sqrt(t3)
st.header("Tinggi")
st.subheader(t4)
