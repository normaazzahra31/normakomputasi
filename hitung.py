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

    # suhu_converter.py

def celsius_to_fahrenheit(celsius):
    """Konversi suhu dari Celcius ke Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Konversi suhu dari Fahrenheit ke Celcius."""
    return (fahrenheit - 32) * 5/9

def main():
    print("Konversi Suhu")
    print("1. Celcius ke Fahrenheit")
    print("2. Fahrenheit ke Celcius")
    
    choice = input("Pilih opsi (1/2): ")
    
    if choice == '1':
        celsius = float(input("Masukkan suhu dalam Celcius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {fahrenheit}°F")
    elif choice == '2':
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {celsius}°C")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()

    
st.write (x, ' ', sx, '=...' sy)
