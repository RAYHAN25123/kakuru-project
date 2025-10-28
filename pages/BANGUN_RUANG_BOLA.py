import streamlit as st

st.title("BANGUN RUANG BOLA")
st.subheader("Rumus:")
st.markdown("""
- π = 3,14 atau 22/7
- r = Jari -jari
- d = Diameter
- V = Volume
- LP = Luas Permukaan
""")
st.image("https://blogger.googleusercontent.com/img/a/AVvXsEgJDx1K4-agq6_eRg5V5cE5ycvCa8Neg8A_Vfe3MdZpyaMZQepROZ9sGercldT7Hg-5y7mpwZXImqoWeOx4YMzWSIdijI7rTPjfXyfmSz1CBAF4B1IN7MBnfgtrRbc1-mtIMwXYtuEZhRUohj3EGfFJ3JjtivfWS4KBfF9oOl46iXoM0A4Y2YO3CV9vIg", caption="Gambar diambil dari internet", use_container_width=True)

st.subheader("Mencari Jari - jari")
d = st.number_input("Masukan nilai Diameter")
r = d /2
st.header("Jari - jari")
st.subheader(r)
st.subheader("Mencari Volume & Luas Permukaan")
r1 = st.number_input("Masukan nilai r")
v = 4/3 * 3.14 * r1 **3
v1 = 4/3 * 22/7 * r1 **3
st.header("Volume (3,14)")
st.subheader(v)
st.header("Volume (22/7)")
st.subheader(v1)
lp = 4 * (3.14 * r1 **2)
lp1 = 4 * (3.14 * r1 **2)
st.header("Luas Permukaan (3,14)")
st.subheader(lp)
st.header("Luas Permukaan (22/7)")
st.subheader(lp1)