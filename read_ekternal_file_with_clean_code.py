# ini adalah contoh pengunaan read ekternal dengan kata kunci with yang lebi direkomendasikan 
# karena dengan kata kunci with kita tidak perlu menutup file secara manual
# # dengan kata kunci with file akan ditutup secara otomatis setelah selesai digunakan

# Pastikan berkas 'catatan_rahasia.txt' ada di direktori yang sama
# dengan skrip Python Anda, atau sediakan path lengkapnya.

try:
    # 'r' adalah mode baca (read). 'f' adalah variabel yang akan menampung objek berkas.
    with open('catatan_rahasia.txt', 'r') as f:
        isi_berkas = f.read() # Membaca seluruh konten berkas
        print("Isi dari catatan_rahasia.txt:")
        print(isi_berkas)
    # Begitu keluar dari blok 'with', berkas 'f' otomatis ditutup.
    print("\n--- Berkas berhasil dibaca dan ditutup otomatis. ---")

except FileNotFoundError:
    print("Error: Berkas 'catatan_rahasia.txt' tidak ditemukan. Pastikan namanya benar dan lokasinya.")
except Exception as e:
    print(f"Terjadi kesalahan lain saat membaca berkas: {e}")