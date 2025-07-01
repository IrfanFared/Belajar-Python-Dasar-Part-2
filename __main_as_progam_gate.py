def sapa_dunia():
    print("halo dunia")

def lampu_merah():
    print("nyalakan lampu merah")


if __name__ == "__name__":

    #kode setalah block ini akan dijalankan ketika file ini  ini adalah progamam utama
    # jadi ketika file lain impor module file ini maka kode ini tidak akan jalan di file terebut
    print("tombol rahasia di tekan")


sapa_dunia()
lampu_merah()


"""
Blok if __name__ == "__main__": itu seperti tombol "START" utama untuk program Anda. Kode di dalamnya hanya akan berjalan jika Anda "menekan tombol START" dengan menjalankan file tersebut secara langsung. Jika file itu hanya diimpor oleh file lain, tombol START-nya tidak akan ditekan, dan kode di dalamnya akan dilewati.

Ini sangat berguna agar file Python Anda bisa fleksibel: bisa jadi program mandiri, atau bisa jadi "kumpulan alat" (modul) yang fungsinya bisa dipakai oleh program lain tanpa menjalankan semua hal di dalamnya.

"""