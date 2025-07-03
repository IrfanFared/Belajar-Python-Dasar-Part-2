try:
    # Kode yang mungkin menimbulkan Exception
    # Contoh: operasi pembagian
    angka_atas = int(input("Masukkan angka pembilang: "))
    angka_bawah = int(input("Masukkan angka penyebut: "))
    hasil = angka_atas / angka_bawah
    print(f"Hasil pembagian: {hasil}")

except ZeroDivisionError:
    # Kode ini akan dijalankan jika terjadi ZeroDivisionError
    print("Kesalahan! Anda tidak bisa membagi dengan nol.")

except ValueError:
    # Kode ini akan dijalankan jika terjadi ValueError (misal, input bukan angka)
    print("Kesalahan! Mohon masukkan angka yang valid.")

except Exception as e:
    # Ini akan menangkap semua Exception lain yang tidak disebutkan di atas
    # dan mencetak pesan error spesifiknya.
    print(f"Terjadi kesalahan tak terduga: {e}")

else:
    # Blok ini (opsional) akan dijalankan jika TIDAK ADA Exception di blok try
    print("Operasi berhasil tanpa ada masalah.")

finally:
    # Blok ini (opsional) akan SELALU dijalankan, terlepas dari ada Exception atau tidak.
    # Berguna untuk membersihkan resource, seperti menutup file.
    print("Program selesai menjalankan operasi pembagian.")

print("\nProgram terus berjalan setelah blok try-except.")