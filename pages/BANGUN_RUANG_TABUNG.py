import streamlit as st

st.title("TABUNG")
st.markdown("""
### Penjabaran :
- V = Volume
- Lp = Luas Permukaan
- r = Jari-jari
- t = tinggi
- π = 3,14 atau 22/7
### Rumus:
""")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1b1AoXpyLYFZtb1ByV2kxBAvjLt4hkTmR3g&s", caption="Gambar ini diambil dari internet", use_container_width=True)

st.header("VOLUME & LUAS PERMUKAAN")
r = st.number_input("Masukan Jari-jari")
t = st.number_input("Masukan Tinggi")
v = (3.14 * r) * r * t
st.header("Volume (3,14)")
st.subheader(v)
v1 = (22/7 * r) * r * t
st.header("Volume (22/7)")
st.subheader(v1)
lp = 2 * (3.14 * r) * (r + t)
st.header("Luas Permukaan (3,14)")
st.subheader(lp)
lp1 = 2 * (22/7 * r) * (r + t)
st.header("Luas Permukaan (22/7)")
st.subheader(lp1)
