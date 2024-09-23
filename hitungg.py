def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    print("Program Konversi Suhu")
    print("1: Celsius ke Fahrenheit")
    print("2: Fahrenheit ke Celsius")
    print("3: Celsius ke Kelvin")
    print("4: Kelvin ke Celsius")
    print("5: Fahrenheit ke Kelvin")
    print("6: Kelvin ke Fahrenheit")

    pilihan = input("Masukkan pilihan (1-6): ")

    if pilihan == '1':
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        print(f"Suhu dalam Fahrenheit: {celsius_to_fahrenheit(celsius)}")
    elif pilihan == '2':
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        print(f"Suhu dalam Celsius: {fahrenheit_to_celsius(fahrenheit)}")
    elif pilihan == '3':
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        print(f"Suhu dalam Kelvin: {celsius_to_kelvin(celsius)}")
    elif pilihan == '4':
        kelvin = float(input("Masukkan suhu dalam Kelvin: "))
        print(f"Suhu dalam Celsius: {kelvin_to_celsius(kelvin)}")
    elif pilihan == '5':
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        print(f"Suhu dalam Kelvin: {fahrenheit_to_kelvin(fahrenheit)}")
    elif pilihan == '6':
        kelvin = float(input("Masukkan suhu dalam Kelvin: "))
        print(f"Suhu dalam Fahrenheit: {kelvin_to_fahrenheit(kelvin)}")
    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
