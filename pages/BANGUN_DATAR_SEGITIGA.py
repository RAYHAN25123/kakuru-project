import streamliat as st

st.title("BANGUN DATAR SEGITIGA")
st.markdown("""
### Penjabaran :
- a = Alas
- t = Tinggi
- L = Luas
""")

a = st.number_input("Masukan nilai alas")
t= st.number_input("Masukan nilai tinggi")
l = a * t / 2
st.header("Luas")
st.subheader(l)