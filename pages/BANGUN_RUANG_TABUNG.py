import streamlit as st

st.title("TABUNG")
st.markdown("""
### Penjabaran :
- V = Volume
- r = Jari-jari
- t = tinggi
- π = 3,14 atau 22/7
### Rumus Mencari Volume :
- V = π x r^2 x t
### Rumus Mencari Luas Permukaan :
- LP = 2πr^2 + 2πrt
""")

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
















