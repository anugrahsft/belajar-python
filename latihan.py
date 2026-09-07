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
if umur < 30:
    sisa_tahun = 30 - umur
    print(f"{sisa_tahun} tahun lagi kamu akan berumur 30 tahun.")
else:
    print("Kamu sudah berumur 30 tahun atau lebih.")
