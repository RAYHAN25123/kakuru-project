import streamlit as st 

st.title("TRAPESIUM")
st.markdown("""
### Penjabaran :
- a = Panjang sisi sejajar atas
- b = Panjang sisi sejajar bawah
- t = Tinggi
- L = Luas
### RUMUS KELILING :
- a/2 x (a + b) x t
### RUMUS LUAS :
- a + b + c + d
""")

st.header("KELILING")
a = st.number_input("Masukan nilai sisi A")
b = st.number_input("Masukan nilai sisi B")
c = st.number_input("Masukan nilai sisi C")
d = st.number_input("Masukan nilai sisi D")
k = a + b + c + d
st.subheader(k)

st.header("LUAS")
alsa = st.number_input("Masukan Nilai Alas A:")
alsb = st.number_input("Masukan Nilai Alas B:")
t = st.number_input("Masukan Nilai Tinggi:")
l = 1 / 2 * (alsa + alsb) * t
st.subheader(l)