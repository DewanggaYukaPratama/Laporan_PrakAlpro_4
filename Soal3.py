# Fungsi konversi Celcius ke Fahrenheit
celsius_to_fahrenheit = lambda C: (9/5) * C + 32

# Fungsi konversi Celcius ke Reamur
celsius_to_reamur = lambda C: 0.8 * C

def konversi_suhu():
    print("Pilih jenis konversi suhu:")
    print("1. Celcius ke Fahrenheit")
    print("2. Celcius ke Reamur")
    pilihan = int(input("Masukkan pilihan (1/2): "))

    if pilihan == 1:
        celcius = float(input("Masukkan suhu dalam Celcius: "))
        farenheit = celsius_to_fahrenheit(celcius)
        print(f"Input C = {celcius}. Output F = {farenheit}.")
    elif pilihan == 2:
        celcius = float(input("Masukkan suhu dalam Celcius: "))
        reamur = celsius_to_reamur(celcius)
        print(f"Input C = {celcius}. Output R = {reamur}.")
    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

# Memanggil fungsi konversi_suhu
konversi_suhu()
