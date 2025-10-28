import streamlit as st
import math

t.image("https://www.google.com/imgres?q=rumus%20segitiga%20sama%20kaki&imgurl=https%3A%2F%2Fawsimages.detik.net.id%2Fcommunity%2Fmedia%2Fvisual%2F2023%2F01%2F30%2Fcontoh-soal-segitiga-sama-kaki-2_169.png%3Fw%3D620&imgrefurl=https%3A%2F%2Fwww.detik.com%2Fbali%2Fberita%2Fd-6542283%2Fketahui-rumus-segitiga-sama-kaki-luas-keliling-dan-contoh-soal&docid=aNboYuW2rAjICM&tbnid=asD7IU7hW_OF8M&vet=12ahUKEwiJwYWV18aQAxU53jgGHdz7NIUQM3oECBUQAA..i&w=620&h=347&hcb=2&ved=2ahUKEwiJwYWV18aQAxU53jgGHdz7NIUQM3oECBUQAA", caption="Gambar ini diambil dari internet", use_column_width=True)
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
