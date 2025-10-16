import streamlit as st
import math

st.title("SEGITIGA SAMA KAKI")
st.image_url = "https://www.google.com/search?sca_esv=415e83c541284ed9&rlz=1C1GCEA_enID1178ID1178&sxsrf=AE3TifMrIp0aPW671ALM_WnVi6Oi0wb0Qw:1760595863192&udm=2&fbs=AIIjpHxgbM2h8Svo6qNug7XqS5BsfddAIs86QJoqf6s-CtEaq0j8ejD2V3ygKxRPty1SN0H5YSUP8xy1LPYJwQDIm5mIKRjMoy8d_PSOR0zjq1xXnX-YLxYKioJGCvsrZ9GnyAoXagQ1PyyQus8n-PlkCX_Xr_zxHgrL5H6labWG7Q6BUF2PDrYfQu4fo1U-ZbEQBwcdlg0uvHSavZ_k0jeXcVJBungzqQ&q=segitiga+sama+kaki&sa=X&sqi=2&ved=2ahUKEwjk5ZLYiqiQAxWtyzgGHatvOXoQtKgLegQIDhAB"
st.markdown("""
### RUMUS :
- s = Sisi
- a = Alas
- t = Tinggi
- K = Keliling
- L = Luas
### RUMUS MENCARI KELILING :
- K = 2 x sisi + alas
### RUMUS MENCARI LUAS :
- L = 1/2 x alas x tinggi
### RUMUS MENCARI TINGGI (Jika tidak ada tinggi) :
- t = √sisi2 - (a/2)2
""")

s = st.number_input("Masukan Sisi", key="sisi 1")
a = st.number_input("Masukan Alas", key="alas 1")
st.header("KELILING")
k = 2 * s + a
st.subheader(k)

a1 = st.number_input("Masukan Nilai Alas", key="alas 2")
t = st.number_input("Masukan Nilai Tinggi", key="tinggi 1")
st.header("LUAS")
l = 1 / 2 * a1 * t
st.subheader(l)

st.subheader("Rumus mencari Tinggi (Jika tidak ada)")
s1 = st.number_input("Masukan Sisi", key="sisi 2")
a2 = st.number_input("Masukan Alas", key="alas 3")
t1 = s1 **2
t2 = (a2 /2) **2
t3 = t1 - t2
t4 = math.sqrt(t3)
st.header("Tinggi")
st.subheader(t4)
