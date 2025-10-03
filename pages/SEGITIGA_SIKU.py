import streamlit as st

st.title("SEGITIGA SIKU-SIKU")

#Mencari Keliling
st.header("KELILING")
a = st.number_input("Masukan Panjang sisi 1")
b = st.number_input("Masukan Panjang sisi 2")
c = st.number_input("Masukan Panjang sisi 3")
k = a + b + c
st.header("Keliling")
st.subheader(k)
#Mencari Luas
st.header("LUAS")
alas = st.number_input("Masukan panjang Alas")
tinggi = st.number_input("Masukan Tinggi")
l = alas * tinggi * 1 / 2
st.subheader(l)
#Mencari Alas
st.header("MENCARI ALAS")
kll = st.number_input("Masukan Keliling:")
tinggi1 = st.number_input("Masukan Tinggi", key= "tinggi 1")
als = kll / 3
als2 = als x tinggi1
st.subheader(als2)

#Mencari tinggi
st.header("MENCARI TINGGI")
ls = st.number_input("Masukan Nilai luas")
t = ls * 1 / 2
st.header(t)




