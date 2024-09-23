import streamlit as st

# Input dari pengguna
x = st.number_input("Masukkan angka")
sx = st.selectbox("Satuan", ("C", "F", "K", "R"), key='sx')
st.write("Anda memasukkan", x, ' ', sx)
sy = st.selectbox("Dikonversi ke", ("C", "F", "K", "R"), key='sy')

# Inisialisasi variabel hasil konversi
y = 0

# Logika konversi suhu
if (sx == 'C'):  # Dari Celcius
    if (sy == 'C'):
        y = x
    elif (sy == 'F'):
        y = (x * 9/5) + 32
    elif (sy == 'K'):
        y = x + 273.15
    elif (sy == 'R'):
        y = x * 4/5

elif (sx == 'F'):  # Dari Fahrenheit
    if (sy == 'C'):
        y = (x - 32) * 5/9
    elif (sy == 'F'):
        y = x
    elif (sy == 'K'):
        y = (x - 32) * 5/9 + 273.15
    elif (sy == 'R'):
        y = (x - 32) * 4/9

elif (sx == 'K'):  # Dari Kelvin
    if (sy == 'C'):
        y = x - 273.15
    elif (sy == 'F'):
        y = (x - 273.15) * 9/5 + 32
    elif (sy == 'K'):
        y = x
    elif (sy == 'R'):
        y = (x - 273.15) * 4/5

elif (sx == 'R'):  # Dari Réaumur
    if (sy == 'C'):
        y = x * 5/4
    elif (sy == 'F'):
        y = (x * 9/4) + 32
    elif (sy == 'K'):
        y = (x * 5/4) + 273.15
    elif (sy == 'R'):
        y = x

# Output hasil konversi
st.write(x, ' ', sx, ' = ', y, ' ', sy)
