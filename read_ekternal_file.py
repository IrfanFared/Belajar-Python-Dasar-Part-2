"""
membaca ekternal file di python berguna untuk mengambil data dari file yang berada di luar progam python
membaca ekterna file harus dipelajari untuk data sains karena data sains membutuhkan data yang banyak
"""

# fungsi open() digunakan untuk membuka file
# fungsi ini menerima dua argume yaitu nama file dan mode
# mode cara membuka file ada beberapa macam yaitu:
# "r" unutuk membaca file
# "w" untuk menulis file
# "a" untuk menambahakan data ke file
# "x" untuk membuat file baru
# "b" untuk membuka file biner
# "t" untuk membuka file teks
# "r+" untuk membca dan menulis file

# syntax fungsi open()
# open(nama_file,mode)

# -nama file adalah nama file yang akan dibuka
# jika file tidak ada maka akan terjadi error

mode_membaca = open("dumb.txt", 'r')
membaca_file = mode_membaca.read()
print(membaca_file)

#lebih baik mengunnakan try except unuk menagan error jika file tidak ada akan diterankan di file selajutnya
