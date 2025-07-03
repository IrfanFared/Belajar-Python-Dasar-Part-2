"""
try except adalah sebuah blok kode yang digunakan untuk menagani error atau exception yang munkin terjadi
dalam program dengan cara yang lebih terstruktur.dengan mengunakan block try except,
kita dapa menangkap error yang munkin terjadi dan memberikan penanganan yang sesuai,
sehingga progam tetap dapa berjalan meskipun terjadi error


ada beberapa jenis exception yang umum muncuk di data sains, atara lain:
# 1. ZeroDivisionError: Terjadi ketika ada upaya untuk membagi dengan nol.
# 2. ValueError: Terjadi ketika ada upaya untuk mengonversi tipe data yang tidak sesuai, seperti mengonversi string ke integer.
# 3. IndexError: Terjadi ketika mencoba mengakses indeks yang tidak ada dalam sebuah list atau array.
# 4. KeyError: Terjadi ketika mencoba mengakses kunci yang tidak ada dalam sebuah dictionary.
# 5. TypeError: Terjadi ketika ada operasi yang tidak valid untuk tipe data tertentu, seperti mencoba menggabungkan string dengan integer.
# 6. FileNotFoundError: Terjadi ketika mencoba membuka file yang tidak ada.


"""

try:
    a = 10
    b = 0
    error = a / b
    print(error)

except ZeroDivisionError:
    print("tidak bisa membagi 0")

else:
    print("pada block ini akan di jalankan jika tidak ada error")

finally: # finaly adalaha kata kunci yang dimana ada erro atau tidak akan di jalankan setelah kata kunci finaly
    print("block ini akan di pritn terlepasa dari erro atau tidak")