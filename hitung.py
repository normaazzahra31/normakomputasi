import streamlit as st

x = st.number_input("Masukkan angka")
sx = st.text_input("Satuan", "C")
st.write ("Anda memasukkan", x, ' ', sx)
sy = st.text_input("Dikonversi ke", "C")
y = 0
if (sx == 'C'):
  if (sy == 'C'):
    y = x
  elif(sy == 'F'):

# Fungsi konversi
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Input dari pengguna
x = st.number_input("Masukkan angka")
sx = st.text_input("Satuan", "C").upper()
sy = st.text_input("Dikonversi ke", "C").upper()

st.write("Anda memasukkan", x, 'dalam', sx)

y = 0
if sx == 'C':
    if sy == 'C':
        y = x
    elif sy == 'F':
        y = celsius_to_fahrenheit(x)
elif sx == 'F':
    if sy == 'C':
        y = fahrenheit_to_celsius(x)
    elif sy == 'F':
        y = x

# Menampilkan hasil
st.write(f"{x} {sx} = {y} {sy}")



