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
### RUMUS MENCARI TINGGI :
- 2 x L / (a + b)
""")
st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fidschool.net%2Fsd%2Fcara-menghitung-tinggi-trapesium%2F&psig=AOvVaw0NGUZjWTw4HpfDOgrVRENV&ust=1762609450964000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCKiUvaGW4JADFQAAAAAdAAAAABAE", caption="Gambar ini diambil dari internet", use_container_width=True)

st.header("KELILING")
a = st.number_input("Masukan nilai sisi A:")
b = st.number_input("Masukan nilai sisi B:")
c = st.number_input("Masukan nilai sisi C:")
d = st.number_input("Masukan nilai sisi D:")
k = a + b + c + d
st.header("Keliling")
st.subheader(k)

st.header("LUAS")
alsa = st.number_input("Masukan Nilai Alas A:", key="alas 1")
alsb = st.number_input("Masukan Nilai Alas B:", key="alas 2")
t = st.number_input("Masukan Nilai Tinggi:")
l = 1 / 2 * (alsa + alsb) * t
st.header("Luas")
st.subheader(l)

st.header("TINGGI")
alsl = st.number_input("Masukan Nilai Luas:")
alsa1 = st.number_input("Masukan Nilai Alas A:", key="alas 3")
alsb2 = st.number_input("Masukan Nilai Alas B:", key="alas 4")
t1 = 2 * alsl
t2 = alsa1 + alsa2
t3 = t1 / t2
st.header("Tinggi")
st.subheader(t3)