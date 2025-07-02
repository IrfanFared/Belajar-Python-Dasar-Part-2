with open("dumb.txt", "r") as f:
   for i in f:
      print(f"{i}")

# ada bebrapa cata metode lajutan pembacaan file read()
# - f.read() untuk membca seluruh isi file
# - f.readline() untuk memabaca satu baris file
# - f.readlines() untuk membaca seluruh isi file dan mengebalika setiap baris sebagai elemen list
# - f.seek(0) untuk mengembalikan posisi bca ke awal file
# - f.tell() untuk mengetahui posisi baca saat ini
# - f.truncate() untuk menghapus sisa file dari posisi baca saat ini
# - f.close() untuk menutup file setelah selesai digunakan
# - f.flush() untuk membersihakan buffer file
# - f.write() untu menulis data ke file
# - f.writelines() untuk menulis beberapa baris ke file
# - f.readable() untuk mengecek apakah file dapat dibaca
# - f.writable() untuk mengecek apakah file dapat ditulis
# - f.seekable() untuk mengecek apakah file dapat diubah posisi baca    
# - f.encoding untuk mengetahui encoding file
# - f.errors untuk mengetahui jenis error yang terjadi saat membaca file