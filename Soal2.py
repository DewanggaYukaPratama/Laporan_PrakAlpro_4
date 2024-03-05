def cek_digit_belakang(d1, d2, d3):
  """
  Fungsi untuk menentukan apakah minimal dua dari tiga parameter memiliki digit paling kanan yang sama.

  Parameter:
    d1: Bilangan pertama.
    d2: Bilangan kedua.
    d3: Bilangan ketiga.

  Return:
    True jika minimal dua dari tiga parameter memiliki digit paling kanan yang sama, False jika tidak.
  """
  # Mendapatkan digit paling kanan dari setiap bilangan
  digit_bil1 = d1 % 10
  digit_bil2 = d2 % 10
  digit_bil3 = d3 % 10

  # Mengecek apakah dua dari tiga digit sama
  if digit_bil1 == digit_bil2:
    return True
  elif digit_bil1 == digit_bil3:
    return True
  elif digit_bil2 == digit_bil3:
    return True
  else:
    return False

# Membaca input dari pengguna
d1 = int(input("Masukkan nilai pertama: "))
d2 = int(input("Masukkan nilai kedua: "))
d3 = int(input("Masukkan nilai ketiga: "))

# Menggunakan fungsi cek_digit_belakang untuk menguji input
output = cek_digit_belakang(d1, d2, d3)
print("Output yang diharapkan =", output)
