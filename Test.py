# Kalkulator Sederhana dengan Mode & Penjelasan

print("=== KALKULATOR CERDAS ===")
print("Pilih mode:")
print("1. Light Mode")
print("2. Dark Mode")

mode = input("Masukkan pilihan (1/2): ")

if mode == "1":
    tema = "LIGHT MODE"
elif mode == "2":
    tema = "DARK MODE"
else:
    tema = "MODE TIDAK DIKENAL"

print("\nMode aktif:", tema)

angka1 = float(input("\nMasukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

print("\n=== HASIL PERHITUNGAN ===")

if operator == "+":
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
    print(
        "Penjelasan: Penjumlahan berarti menggabungkan dua nilai.\n"
        f"Angka {angka1} ditambah {angka2} menghasilkan total {hasil}."
    )

elif operator == "-":
    hasil = angka1 - angka2
    print(f"{angka1} - {angka2} = {hasil}")
    print(
        "Penjelasan: Pengurangan berarti mengambil sebagian nilai.\n"
        f"Dari {angka1} dikurangi {angka2}, tersisa {hasil}."
    )

elif operator == "*":
    hasil = angka1 * angka2
    print(f"{angka1} × {angka2} = {hasil}")
    print(
        "Penjelasan: Perkalian adalah penjumlahan berulang.\n"
        f"{angka1} dikalikan {angka2} berarti menjumlahkan {angka1} sebanyak {angka2} kali."
    )

elif operator == "/":
    if angka2 == 0:
        print("Error: Tidak bisa membagi dengan nol.")
    else:
        hasil = angka1 / angka2
        print(f"{angka1} ÷ {angka2} = {hasil}")
        print(
            "Penjelasan: Pembagian berarti membagi nilai menjadi beberapa bagian sama besar.\n"
            f"{angka1} dibagi {angka2} menghasilkan {hasil}."
        )

else:
    print("Operator tidak valid.")