import streamlit as st

st.title("BANGUN RUANG BALOK")
st.markdown("""
- p = Panjang
- l = Lebar
- t = Tinggi
- V = Volume
- LP = Luas Permukaan
""")
st.image("https://static.cdntap.com/tap-assets-prod/wp-content/uploads/sites/24/2022/05/Rumus-Volume-Dan-Luas-Permukaan-Balok.jpg", caption="Gambar ini diambil dari internet", use_container_width=True)

st.header("VOLUME & LUAS PERMUKAAN")
p = st.number_input("Masukan Nilai Panjang:")
l = st.number_input("Masukan Nilai Lebar:")
t = st.number_input("Masukan Nilai Tinggi:")
st.header("Luas Permukaan")
l1 = 2 * (p * l + p * t + l * t)
st.subheader(l1)
st.header("Volume")
v = p * l * t
st.subheader(v)
