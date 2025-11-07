import streamliat as st

st.title("BANGUN DATAR SEGITIGA")
st.markdown("""
### Penjabaran :
- a = Alas
- t = Tinggi
- L = Luas
- K = Keliling
""")

st.header("KELILING")
a = st.number_input("Masukan Nilai Sisi a:")
b = st.number_input("Masukan Nilai Sisi b:")
c = st.number_input("Masukan Nilai Sisi c:")
k = a + b + c
st.header("Keliling")
st.subheader(k)

st.header("LUAS")
a = st.number_input("Masukan Nilai Alas:")
t= st.number_input("Masukan Nilai Tinggi:")
l = a * t / 2
st.header("Luas")
st.subheader(l)

st.header("TINGGI")
luas = st.number_input("Masukan Nilai Luas:")
alas = st.number_input("Masukan Nilai Alas:", key="Alas 1")
t1 = 2 * luas
t2 = t1 / alas
st.header("Tinggi")
st.subheader(t2)