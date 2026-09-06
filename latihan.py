# latihan.py - Program sederhana kalkulator biodata

nama = input("Siapa nama kamu? ")
umur = int(input("Berapa umur kamu? "))

# Variable & operator praktek
tahun_lahir = 2026 - umur
pesan_sapaan = f"Halo, {nama}! Kamu lahir sekitar tahun {tahun_lahir}."

print(pesan_sapaan)

# Praktek conditional pakai comparison operator
if umur >= 18:
    print("Kamu sudah dewasa.")
else:
    print("Kamu masih di bawah umur.")
