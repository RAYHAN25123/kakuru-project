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

st.subheader("Mencari Volume:")
r = st.number_input("Masukan Jari-jari")
t = st.number_input("Masukan Tinggi")
v = 3.14 * r **2 * t
st.header("Volume")
st.subheader(v)
v1 = 22/7 * r **2 * t
st.header("Volume (22/7)")
st.subheader(v1)
v2 = 2 * 3.14 * r **2
v3 = r + t
v4 = v2 + v3
st.header("Luas Permukaan (3,14)")
st.subheader(v4)
v5 = 2 * 22/7 * r **2
v6 = r + t
v7 = v5 + v6
st.header("Luas Permukaan (22/7)")
st.subheader(v7)






