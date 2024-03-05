def cek_angka(n1, n2, n3):
  """
  Fungsi ini untuk menentukan apakah ketiga parameter memenuhi semua ketentuan:
  • Ketiga parameter tersebut nilainya berbeda semua.
  • Ada kemungkinan jika diambil dua parameter dan dijumlahkan hasilnya sama dengan 
    parameter lainnya (yang tersisa).

  Fungsi ini akan menghasilkan nilai True jika semua ketentuan tersebut dipenuhi. 
  Jika tidak terpenuhi maka fungsi akan menghasilkan nilai False.
  """
  # Menentukan jika ketiga parameter tersebut tidak ada yang sama/nilainya berbeda-beda
  syarat1 = (n1 != n2) & (n1 != n3) & (n2 != n3)

  # Menentukan apakah jika ada 2 paramater yang dijumlahkan hasilnya adalah parameter yang lainnya
  syarat2 = (n1 + n2 == n3) | (n1 + n3 == n2) | (n2 + n3 == n1)

  return syarat1 & syarat2

# Contoh penggunaan
print(cek_angka(12, 5, 7))  
