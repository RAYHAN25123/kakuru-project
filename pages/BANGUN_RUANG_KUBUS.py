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
st.image("https://www.google.com/imgres?q=rumus%20kubus&imgurl=https%3A%2F%2Fi.pinimg.com%2F736x%2F35%2F75%2F24%2F35752466dd7e291d1aa3d8cc5969f19e.jpg&imgrefurl=https%3A%2F%2Fid.pinterest.com%2Fpin%2Fcara-menghitung-volume-dan-luas-permukaan-kubus--520658406937201872%2F&docid=JM1QILQIsxly_M&tbnid=Q0Kcd65lnybvdM&vet=12ahUKEwjUgMnmneCQAxUnxTgGHRu3JEoQM3oECBoQAA..i&w=736&h=414&hcb=2&ved=2ahUKEwjUgMnmneCQAxUnxTgGHRu3JEoQM3oECBoQAA", caption="Gambar ini diambil dari internet", use_container_width=True)

st.header("VOLUME & LUAS PERMUKAAN")
sisi = st.number_input("Masukan Panjang Sisi:")
st.subheader("Luas Permukaan")
v = 6 * sisi **2
st.subheader(v)
st.header("Volume")
l = sisi **3
st.subheader(l)