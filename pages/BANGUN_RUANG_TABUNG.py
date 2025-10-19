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
""")

r = st.number_input("Masukan Jari-jari")
t = st.number_input("Masukan Tinggi")
v = 3.14 * r **2 * t
st.header("Volume (3,14)")
st.subheader(v)
v1 = 22/7 * r **2 * t
st.header("Volume (22/7)")
st.subheader(v1)


